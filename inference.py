"""
Inference Script - CurriculumFlowENV
===================================
MANDATORY
- Before submitting, ensure the following variables are defined in your environment configuration:
    API_BASE_URL   The API endpoint for the LLM.
    MODEL_NAME     The model identifier to use for inference.
    HF_TOKEN       Your Hugging Face / API key.

- The inference script must be named `inference.py` and placed in the root directory of the project
- Participants must use OpenAI Client for all LLM calls using above variables

STDOUT FORMAT
    [START] task=<task_name> env=<benchmark> model=<model_name>
    [STEP]  step=<n> action=<action_str> reward=<0.00> done=<true|false> error=<msg|null>
    [END]   success=<true|false> steps=<n> score=<score> rewards=<r1,r2,...,rn>

TASKS (3 graded tasks):
    1. topic_selection      - Optimize topic choice for maximum mastery gain
    2. difficulty_adaptation - Optimize difficulty for optimal engagement
    3. assessment_timing     - Optimize assessment timing for best completion
"""

import json
import os
import textwrap
from typing import Any, Dict, List, Optional

import requests
from openai import OpenAI

# -- Environment configuration ------------------------------------------------
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")
API_KEY = HF_TOKEN or os.getenv("API_KEY")

# Space URL — connect directly via HTTP (no Docker needed)
SPACE_URL = os.getenv(
    "SPACE_URL", "https://krithickvivek-epochai.hf.space"
)

BENCHMARK = "curriculum_flow_env"
STEPS_PER_TASK = 30
TEMPERATURE = 0.7
MAX_TOKENS = 256
NUM_TOPICS = 66


# -- Simple HTTP Environment Client (no Docker) ------------------------------
class EnvHTTPClient:
    """Connects to a running OpenEnv Space via HTTP. No Docker required."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def reset(self) -> Dict[str, Any]:
        resp = self.session.post(f"{self.base_url}/reset", timeout=30)
        resp.raise_for_status()
        return resp.json()

    def step(self, action: Dict[str, Any]) -> Dict[str, Any]:
        resp = self.session.post(
            f"{self.base_url}/step",
            json={"action": action},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def state(self) -> Dict[str, Any]:
        resp = self.session.get(f"{self.base_url}/state", timeout=30)
        resp.raise_for_status()
        return resp.json()

    def close(self):
        self.session.close()


# -- Observation wrapper for LLM prompts -------------------------------------
class Obs:
    """Lightweight observation wrapper parsed from JSON response."""

    def __init__(self, data: Dict[str, Any]):
        info = data.get("info", {})
        self.topics_mastered = info.get("topics_mastered", 0)
        self.completion_rate = info.get("completion_rate", 0.0)
        self.episode_reward = info.get("episode_reward", 0.0)
        self.student_archetype = info.get("student_archetype", "")
        self.step = info.get("step", 0)

        # These come from the raw observation in /step's info or from a
        # separate /state call; provide safe defaults from info
        self.mastery = info.get("mastery", [0.0] * NUM_TOPICS)
        self.engagement = info.get("engagement", [0.8])
        self.time_since_review = info.get("time_since_review", [0.0] * NUM_TOPICS)
        self.unlocked_mask = info.get("unlocked_mask", [1] * NUM_TOPICS)

        # Try to extract richer data from a state response
        student = info.get("student", {})
        if student:
            self._load_from_student(student)

    def _load_from_student(self, student: Dict[str, Any]):
        if "mastery" in student and isinstance(student["mastery"], dict):
            self.mastery = [student["mastery"].get(str(i), 0.0) for i in range(NUM_TOPICS)]
        if "engagement" in student:
            eng = student["engagement"]
            self.engagement = [eng] if isinstance(eng, (int, float)) else eng
        if "time_since_review" in student and isinstance(student["time_since_review"], dict):
            self.time_since_review = [
                student["time_since_review"].get(str(i), 0.0) for i in range(NUM_TOPICS)
            ]


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
def build_user_prompt(obs: Obs, step: int, last_reward: float, task: str) -> str:
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
    client: OpenAI, obs: Obs, step: int, last_reward: float, task: str
) -> Dict[str, int]:
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

        # Parse JSON (handle markdown code blocks)
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip()
        parsed = json.loads(text)

        return {
            "topic": max(0, min(65, int(parsed.get("topic", 0)))),
            "difficulty": max(0, min(4, int(parsed.get("difficulty", 0)))),
            "assess": 1 if parsed.get("assess", 0) else 0,
        }

    except Exception as exc:
        print(f"[DEBUG] LLM parse failed: {exc}", flush=True)
        unlocked = [i for i, u in enumerate(obs.unlocked_mask) if u == 1]
        best = min(unlocked, key=lambda i: obs.mastery[i]) if unlocked else 0
        return {"topic": best, "difficulty": 1, "assess": 0}


# -- Run a single task -------------------------------------------------------
def run_task(env: EnvHTTPClient, llm: OpenAI, task_name: str) -> float:
    rewards: List[float] = []
    steps_taken = 0
    score = 0.0
    success = False
    obs = None

    log_start(task=task_name, env=BENCHMARK, model=MODEL_NAME)

    try:
        # Reset environment
        reset_data = env.reset()
        obs = Obs(reset_data)

        # Fetch full state to get mastery/engagement arrays
        try:
            state_data = env.state()
            obs = Obs(state_data)
        except Exception:
            pass

        last_reward = 0.0
        done = False

        for step in range(1, STEPS_PER_TASK + 1):
            if done:
                break

            action = get_llm_action(llm, obs, step, last_reward, task_name)

            # Step environment
            step_data = env.step(action)
            reward = float(step_data.get("reward", 0.0))
            done = bool(step_data.get("done", False))
            error = step_data.get("info", {}).get("error")

            # Update observation from step response
            obs = Obs(step_data)

            # If step response lacks mastery arrays, fetch state
            if not any(m > 0 for m in obs.mastery):
                try:
                    state_data = env.state()
                    state_obs = Obs(state_data)
                    # Merge: keep step info but use state for arrays
                    state_obs.topics_mastered = obs.topics_mastered or state_obs.topics_mastered
                    state_obs.completion_rate = obs.completion_rate or state_obs.completion_rate
                    state_obs.episode_reward = obs.episode_reward or state_obs.episode_reward
                    obs = state_obs
                except Exception:
                    pass

            rewards.append(reward)
            steps_taken = step
            last_reward = reward

            action_str = (
                f"study(topic={action['topic']},"
                f"diff={action['difficulty']},"
                f"assess={action['assess']})"
            )
            log_step(step=step, action=action_str, reward=reward, done=done, error=error)

            if done:
                break

        # Task-specific score clamped to [0, 1]
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
def main() -> None:
    llm = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    env = EnvHTTPClient(SPACE_URL)

    tasks = ["topic_selection", "difficulty_adaptation", "assessment_timing"]
    scores = []

    try:
        for task_name in tasks:
            score = run_task(env, llm, task_name)
            scores.append(score)
            print(f"[DEBUG] {task_name} score: {score:.3f}", flush=True)

        avg_score = sum(scores) / len(scores)
        print(f"[DEBUG] Average score across {len(tasks)} tasks: {avg_score:.3f}", flush=True)

    finally:
        env.close()


if __name__ == "__main__":
    main()
