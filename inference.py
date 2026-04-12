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
"""

import asyncio
import json
import os
import textwrap
from typing import List, Optional

from openai import OpenAI

from client import CurriculumEnv
from models import CurriculumAction, CurriculumObservation

# ── Environment configuration ────────────────────────────────────────────────
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

TASK_NAME = os.getenv("CURRICULUM_TASK", "adaptive_curriculum")
BENCHMARK = os.getenv("CURRICULUM_BENCHMARK", "curriculum_flow_env")
MAX_STEPS = 50
TEMPERATURE = 0.7
MAX_TOKENS = 256

# ── Scoring ──────────────────────────────────────────────────────────────────
# Score is completion_rate (0.0 to 1.0) — fraction of curriculum mastered
SUCCESS_SCORE_THRESHOLD = 0.05

# ── Prompts ──────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = textwrap.dedent("""\
You are an AI tutor optimizing a student's learning path through a placement
preparation curriculum. Each turn you choose which topic to study, the difficulty
level, and whether to test the student.

The environment has 66 topics across categories: Quantitative Aptitude, Logical
Reasoning, Verbal Ability, Data Interpretation, Programming & CS, DSA, Soft Skills,
and General Knowledge.

Your goal: maximize the student's mastery across all topics efficiently.

Rules:
- Pick unlocked topics (unlocked_mask[i] == 1).
- Match difficulty to mastery: low mastery -> easy, high mastery -> harder.
- Assess periodically to lock-in gains (assess=1 when mastery > 0.5).
- Revisit topics whose mastery is decaying (high time_since_review).

Reply with ONLY a valid JSON object, no explanation:
{"topic": <int 0-65>, "difficulty": <int 0-4>, "assess": <int 0 or 1>}
""").strip()


# ── Structured stdout logging ────────────────────────────────────────────────
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


# ── LLM action selection ────────────────────────────────────────────────────
def build_user_prompt(obs: CurriculumObservation, step: int, last_reward: float) -> str:
    """Build the prompt for the LLM from the current observation."""
    # Find top unlocked topics with lowest mastery (best candidates)
    unlocked = [i for i, u in enumerate(obs.unlocked_mask) if u == 1]
    mastery = obs.mastery
    low_mastery = sorted(unlocked, key=lambda i: mastery[i])[:10]
    # Topics needing review (high time_since_review)
    review = obs.time_since_review
    stale = sorted(unlocked, key=lambda i: -review[i])[:5]

    return textwrap.dedent(f"""\
    Step: {step}/{MAX_STEPS}
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
) -> CurriculumAction:
    """Ask the LLM to pick the next action given the observation."""
    user_prompt = build_user_prompt(obs, step, last_reward)
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
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

        topic = int(parsed.get("topic", 0))
        difficulty = int(parsed.get("difficulty", 0))
        assess = int(parsed.get("assess", 0))

        # Clamp values
        topic = max(0, min(65, topic))
        difficulty = max(0, min(4, difficulty))
        assess = 1 if assess else 0

        return CurriculumAction(topic=topic, difficulty=difficulty, assess=assess)

    except Exception as exc:
        print(f"[DEBUG] LLM action parse failed: {exc}", flush=True)
        # Fallback: pick a low-mastery unlocked topic
        unlocked = [i for i, u in enumerate(obs.unlocked_mask) if u == 1]
        if unlocked:
            best = min(unlocked, key=lambda i: obs.mastery[i])
        else:
            best = 0
        return CurriculumAction(topic=best, difficulty=1, assess=0)


# ── Main episode loop ────────────────────────────────────────────────────────
async def main() -> None:
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

    # Connect to environment
    if LOCAL_IMAGE_NAME:
        env = await CurriculumEnv.from_docker_image(LOCAL_IMAGE_NAME)
    else:
        env = await CurriculumEnv.from_env("krithickvivek/epoch-ai")

    rewards: List[float] = []
    steps_taken = 0
    score = 0.0
    success = False

    log_start(task=TASK_NAME, env=BENCHMARK, model=MODEL_NAME)

    try:
        result = await env.reset()
        obs: CurriculumObservation = result.observation
        last_reward = 0.0

        for step in range(1, MAX_STEPS + 1):
            if result.done:
                break

            # LLM decides the next action
            action = get_llm_action(client, obs, step, last_reward)

            # Step the environment
            result = await env.step(action)
            obs = result.observation

            reward = result.reward or 0.0
            done = result.done
            error = None

            rewards.append(reward)
            steps_taken = step
            last_reward = reward

            # Format action string for logging
            action_str = f"study(topic={action.topic},diff={action.difficulty},assess={action.assess})"
            log_step(step=step, action=action_str, reward=reward, done=done, error=error)

            if done:
                break

        # Score = completion_rate (already 0.0 to 1.0)
        score = obs.completion_rate if obs else 0.0
        score = min(max(score, 0.0), 1.0)
        success = score >= SUCCESS_SCORE_THRESHOLD

    except Exception as exc:
        print(f"[DEBUG] Episode error: {exc}", flush=True)
        score = 0.0
        success = False

    finally:
        try:
            await env.close()
        except Exception as e:
            print(f"[DEBUG] env.close() error: {e}", flush=True)
        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)


if __name__ == "__main__":
    asyncio.run(main())
