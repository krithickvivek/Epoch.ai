"""
Inference Script - CurriculumFlowENV
===================================
MANDATORY
- Before submitting, ensure the following variables are defined in your environment configuration:
    API_BASE_URL   The API endpoint for the LLM.
    MODEL_NAME     The model identifier to use for inference.
    HF_TOKEN       Your Hugging Face / API key.
    LOCAL_IMAGE_NAME The name of the local image to use for the environment if you are using
                     from_docker_image() method

- Defaults are set only for API_BASE_URL and MODEL_NAME
    (and should reflect your active inference setup):
    API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
    MODEL_NAME   = os.getenv("MODEL_NAME",   "Qwen/Qwen2.5-72B-Instruct")

- The inference script must be named `inference.py` and placed in the root directory of the project
- Participants must use OpenAI Client for all LLM calls using above variables

STDOUT FORMAT
- The script must emit exactly three line types to stdout, in this order:

    [START] task=<task_name> env=<benchmark> model=<model_name>
    [STEP]  step=<n> action=<action_str> reward=<0.00> done=<true|false> error=<msg|null>
    [END]   success=<true|false> steps=<n> score=<score> rewards=<r1,r2,...,rn>

  Rules:
    - One [START] line at episode begin.
    - One [STEP] line per step, immediately after env.step() returns.
    - One [END] line after env.close(), always emitted (even on exception).
    - reward and rewards are formatted to 2 decimal places.
    - done and success are lowercase booleans: true or false.
    - error is the raw last_action_error string, or null if none.
    - All fields on a single line with no newlines within a line.
    - Each tasks should return score in [0, 1]

TASKS (3 graded tasks):
    1. topic_selection     - Optimize which topics to study for maximum mastery gain
    2. difficulty_adaptation - Optimize difficulty levels for optimal engagement
    3. assessment_timing    - Optimize assessment timing for best completion rate
"""

import asyncio
import json
import os
import textwrap
from typing import List, Optional

from openai import OpenAI

from client import CurriculumEnv
from models import CurriculumAction, CurriculumObservation

# -- Environment configuration ------------------------------------------------
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

BENCHMARK = "curriculum_flow_env"
STEPS_PER_TASK = 30  # 3 tasks x 30 steps = ~90 steps total, well under 20min
TEMPERATURE = 0.7
MAX_TOKENS = 256
NUM_TOPICS = 66


# -- Structured stdout logging ------------------------------------------------
def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )


# -- Task-specific system prompts --------------------------------------------
PROMPTS = {
    "topic_selection": textwrap.dedent("""\
        You are an AI tutor optimizing TOPIC SELECTION for a student's placement
        preparation. Your goal: maximize the number of topics mastered.

        The curriculum has 66 topics. Pick unlocked topics with low mastery first.
        Prioritize topics that are stale (high time_since_review).
        Use moderate difficulty (1-2) and skip assessments (assess=0) to cover more ground.

        Reply with ONLY valid JSON: {"topic": <int 0-65>, "difficulty": <int 0-4>, "assess": <int 0 or 1>}
    """).strip(),

    "difficulty_adaptation": textwrap.dedent("""\
        You are an AI tutor optimizing DIFFICULTY ADAPTATION for a student.
        Your goal: keep engagement high by matching difficulty to the student's level.

        Rules:
        - Low mastery topics -> easy (0-1)
        - Medium mastery -> medium (2)
        - High mastery -> hard (3-4)
        - If engagement drops below 0.6, reduce difficulty immediately.
        - Assess occasionally (assess=1) to validate progress.

        Reply with ONLY valid JSON: {"topic": <int 0-65>, "difficulty": <int 0-4>, "assess": <int 0 or 1>}
    """).strip(),

    "assessment_timing": textwrap.dedent("""\
        You are an AI tutor optimizing ASSESSMENT TIMING for a student using
        spaced repetition principles (Ebbinghaus forgetting curve).

        Your goal: maximize the overall completion rate through well-timed assessments.

        Rules:
        - Study a topic first (assess=0) to build mastery above 0.4.
        - Then assess (assess=1) when mastery is between 0.5-0.8 for optimal retention.
        - Revisit topics before they decay (check time_since_review).
        - Balance coverage across topics.

        Reply with ONLY valid JSON: {"topic": <int 0-65>, "difficulty": <int 0-4>, "assess": <int 0 or 1>}
    """).strip(),
}

# -- Score extractors per task ------------------------------------------------
SCORE_EXTRACTORS = {
    "topic_selection": lambda obs: min(max(obs.topics_mastered / NUM_TOPICS, 0.0), 1.0),
    "difficulty_adaptation": lambda obs: min(max(obs.engagement[0] if obs.engagement else 0.0, 0.0), 1.0),
    "assessment_timing": lambda obs: min(max(obs.completion_rate, 0.0), 1.0),
}

SUCCESS_THRESHOLD = 0.01


# -- LLM action selection ----------------------------------------------------
def build_user_prompt(obs: CurriculumObservation, step: int, last_reward: float, task: str) -> str:
    unlocked = [i for i, u in enumerate(obs.unlocked_mask) if u == 1]
    mastery = obs.mastery
    low_mastery = sorted(unlocked, key=lambda i: mastery[i])[:10]
    review = obs.time_since_review
    stale = sorted(unlocked, key=lambda i: -review[i])[:5]

    return textwrap.dedent(f"""\
    Task: {task} | Step: {step}/{STEPS_PER_TASK}
    Engagement: {obs.engagement[0]:.2f}
    Topics mastered: {obs.topics_mastered}/{len(mastery)}
    Completion: {obs.completion_rate:.1%}
    Last reward: {last_reward:.2f}
    Episode reward: {obs.episode_reward:.2f}

    Unlocked topics ({len(unlocked)} of {len(mastery)}): {unlocked[:20]}...
    Lowest mastery (top 10): {[(i, round(mastery[i],2)) for i in low_mastery]}
    Most stale (top 5): {[(i, round(review[i],1)) for i in stale]}

    Choose the next action as JSON: {{"topic": <int>, "difficulty": <int 0-4>, "assess": <0 or 1>}}
    """).strip()


def get_llm_action(
    client: OpenAI,
    obs: CurriculumObservation,
    step: int,
    last_reward: float,
    task: str,
) -> CurriculumAction:
    system_prompt = PROMPTS[task]
    user_prompt = build_user_prompt(obs, step, last_reward, task)
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=False,
        )
        text = (completion.choices[0].message.content or "").strip()

        # Parse JSON from response (handle markdown code blocks)
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip()
        parsed = json.loads(text)

        topic = max(0, min(65, int(parsed.get("topic", 0))))
        difficulty = max(0, min(4, int(parsed.get("difficulty", 0))))
        assess = 1 if parsed.get("assess", 0) else 0

        return CurriculumAction(topic=topic, difficulty=difficulty, assess=assess)

    except Exception as exc:
        print(f"[DEBUG] LLM parse failed: {exc}", flush=True)
        unlocked = [i for i, u in enumerate(obs.unlocked_mask) if u == 1]
        best = min(unlocked, key=lambda i: obs.mastery[i]) if unlocked else 0
        return CurriculumAction(topic=best, difficulty=1, assess=0)


# -- Run a single task -------------------------------------------------------
async def run_task(env: CurriculumEnv, client: OpenAI, task_name: str) -> float:
    rewards: List[float] = []
    steps_taken = 0
    score = 0.0
    success = False

    log_start(task=task_name, env=BENCHMARK, model=MODEL_NAME)

    try:
        result = await env.reset()
        obs: CurriculumObservation = result.observation
        last_reward = 0.0

        for step in range(1, STEPS_PER_TASK + 1):
            if result.done:
                break

            action = get_llm_action(client, obs, step, last_reward, task_name)
            result = await env.step(action)
            obs = result.observation

            reward = result.reward or 0.0
            done = result.done
            error = None

            rewards.append(reward)
            steps_taken = step
            last_reward = reward

            action_str = f"study(topic={action.topic},diff={action.difficulty},assess={action.assess})"
            log_step(step=step, action=action_str, reward=reward, done=done, error=error)

            if done:
                break

        # Extract task-specific score (clamped to [0, 1])
        score_fn = SCORE_EXTRACTORS[task_name]
        score = score_fn(obs) if obs else 0.0
        score = min(max(score, 0.0), 1.0)
        success = score >= SUCCESS_THRESHOLD

    except Exception as exc:
        print(f"[DEBUG] Task {task_name} error: {exc}", flush=True)
        score = 0.0
        success = False

    finally:
        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)

    return score


# -- Main: run all 3 tasks ---------------------------------------------------
async def main() -> None:
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

    # Connect to environment
    if LOCAL_IMAGE_NAME:
        env = await CurriculumEnv.from_docker_image(LOCAL_IMAGE_NAME)
    else:
        env = await CurriculumEnv.from_env("krithickvivek/epochai")

    tasks = ["topic_selection", "difficulty_adaptation", "assessment_timing"]
    scores = []

    try:
        for task_name in tasks:
            score = await run_task(env, client, task_name)
            scores.append(score)
            print(f"[DEBUG] {task_name} score: {score:.3f}", flush=True)

        avg_score = sum(scores) / len(scores)
        print(f"[DEBUG] Average score across {len(tasks)} tasks: {avg_score:.3f}", flush=True)

    finally:
        try:
            await env.close()
        except Exception as e:
            print(f"[DEBUG] env.close() error: {e}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
