"""
Epoch.ai / CurriculumFlowENV — OpenENV Inference Script

This module provides:
  - A global RL environment instance
  - A `predict(input_data)` function for HF Spaces inference
  - Self-test validation when run directly

The predict() function is the entry point that OpenENV validation calls.
It also backs the POST /predict API endpoint in the main FastAPI server.
"""

import json
import sys

from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.simulation.curriculum import NUM_TOPICS, TOPIC_NAMES


def load_environment(archetype: str = "steady", seed: int = 42) -> CurriculumFlowEnv:
    """Load and reset the CurriculumFlowENV gymnasium environment."""
    env = CurriculumFlowEnv(archetype=archetype, max_steps=200, seed=seed)
    env.reset(seed=seed)
    return env


# Global environment instance (lazy-loaded on first predict call)
_env: CurriculumFlowEnv = None


def _get_env() -> CurriculumFlowEnv:
    global _env
    if _env is None:
        _env = load_environment()
    return _env


def _obs_to_dict(obs: dict) -> dict:
    """Convert numpy arrays in observation to JSON-serializable types."""
    out = {}
    for k, v in obs.items():
        try:
            out[k] = v.tolist()
        except AttributeError:
            out[k] = int(v) if hasattr(v, "item") else v
    return out


def predict(input_data) -> str:
    """
    OpenENV-compatible predict function.

    Args:
        input_data: Can be:
          - A string: "reset", "state", "spec", "step"/"auto"/"next",
            or a JSON-encoded action like '{"topic":0,"difficulty":2,"assess":0}'
          - A dict: {"topic": 0, "difficulty": 2, "assess": 0}
                    or {"command": "reset"} etc.

    Returns:
        JSON string with status, observation, reward, and human-readable fields.
    """
    env = _get_env()

    try:
        command = None
        action = None

        # Parse input
        if isinstance(input_data, str):
            text = input_data.strip().lower()
            if text in ("reset", "state", "spec", "step", "auto", "next"):
                command = text
            else:
                try:
                    parsed = json.loads(input_data)
                    if isinstance(parsed, dict):
                        if "command" in parsed:
                            command = parsed["command"]
                        elif "action" in parsed:
                            action = parsed["action"]
                        elif "topic" in parsed:
                            action = parsed
                        else:
                            command = "step"
                    else:
                        command = "step"
                except (json.JSONDecodeError, ValueError):
                    command = "step"
        elif isinstance(input_data, dict):
            if "command" in input_data:
                command = input_data["command"]
            elif "action" in input_data:
                action = input_data["action"]
            elif "topic" in input_data:
                action = input_data
            else:
                command = "step"
        else:
            command = "step"

        # Normalize step-like commands
        if command in ("step", "auto", "next"):
            command = "step"

        # --- RESET ---
        if command == "reset":
            obs, info = env.reset()
            return json.dumps({
                "status": "success",
                "command": "reset",
                "observation": _obs_to_dict(obs),
                "info": info,
            }, default=str)

        # --- STATE ---
        if command == "state":
            return json.dumps({
                "status": "success",
                "command": "state",
                "state": env.state(),
            }, default=str)

        # --- SPEC ---
        if command == "spec":
            return json.dumps({
                "status": "success",
                "command": "spec",
                "name": "CurriculumFlowENV",
                "num_topics": NUM_TOPICS,
                "max_steps": env.max_steps,
                "action_space": {"topic": NUM_TOPICS, "difficulty": 5, "assess": 2},
            })

        # --- STEP ---
        if action is None:
            # Agent-recommended action
            obs_raw = env._get_obs()
            info_raw = env.state()
            obs_dict = {k: v.tolist() if hasattr(v, "tolist") else v for k, v in obs_raw.items()}
            topic = env.sequencer.select_action(obs_dict, info_raw)
            diff = env.difficulty_agent.select_action(obs_dict, info_raw)
            assess = env.assessment_agent.select_action(obs_dict, info_raw)
            action = {"topic": int(topic), "difficulty": int(diff), "assess": int(assess)}

        obs, reward, terminated, truncated, info = env.step(action)
        obs_dict = _obs_to_dict(obs)
        engagement = obs_dict.get("engagement", [0.0])
        eng_val = engagement[0] if isinstance(engagement, list) and engagement else 0.0

        return json.dumps({
            "status": "success",
            "action": action,
            "observation": obs_dict,
            "reward": float(reward),
            "terminated": bool(terminated),
            "truncated": bool(truncated),
            "done": bool(terminated or truncated),
            "info": info,
            # Human-readable summary
            "next_topic": info.get("topic_name", ""),
            "difficulty": ["easy", "medium", "hard", "advanced", "expert"][
                min(info.get("difficulty", 1) - 1, 4)
            ],
            "engagement_score": round(float(eng_val), 4),
            "topics_mastered": info.get("topics_mastered", 0),
            "completion_rate": info.get("completion_rate", 0.0),
        }, default=str)

    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})


# ---------------------------------------------------------------------------
# Self-test: validates that the environment + predict function work end-to-end
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Epoch.ai / CurriculumFlowENV — Inference Self-Test")
    print("=" * 60)
    errors = 0

    # 1. Reset
    print("\n[1] Reset environment")
    result = json.loads(predict("reset"))
    assert result["status"] == "success", f"Reset failed: {result}"
    assert "observation" in result, "Reset must return observation"
    print(f"    OK — keys: {list(result['observation'].keys())}")

    # 2. Agent-recommended step
    print("\n[2] Agent-recommended step (text: 'step')")
    result = json.loads(predict("step"))
    assert result["status"] == "success", f"Step failed: {result}"
    assert "reward" in result, "Step must return reward"
    print(f"    OK — reward={result['reward']:.4f}, topic={result.get('next_topic','')}")

    # 3. Explicit action (JSON string)
    print("\n[3] Explicit action via JSON string")
    result = json.loads(predict('{"topic": 1, "difficulty": 2, "assess": 0}'))
    assert result["status"] == "success", f"Explicit action failed: {result}"
    print(f"    OK — reward={result['reward']:.4f}")

    # 4. Explicit action (dict)
    print("\n[4] Explicit action via dict")
    result = json.loads(predict({"topic": 2, "difficulty": 1, "assess": 1}))
    assert result["status"] == "success", f"Dict action failed: {result}"
    print(f"    OK — reward={result['reward']:.4f}")

    # 5. State
    print("\n[5] Query state")
    result = json.loads(predict("state"))
    assert result["status"] == "success"
    assert "state" in result
    print(f"    OK — step_count={result['state'].get('step_count', 'N/A')}")

    # 6. Spec
    print("\n[6] Query spec")
    result = json.loads(predict("spec"))
    assert result["name"] == "CurriculumFlowENV"
    print(f"    OK — {result['name']}, {result['num_topics']} topics")

    # 7. Multi-step rollout
    print("\n[7] 10-step agent rollout")
    predict("reset")
    total_reward = 0.0
    for i in range(10):
        r = json.loads(predict("auto"))
        total_reward += r["reward"]
        if r.get("done"):
            print(f"    Episode ended at step {i+1}")
            break
    print(f"    OK — total reward: {total_reward:.4f}")

    # 8. Verify human-readable fields exist
    print("\n[8] Verify human-readable response fields")
    predict("reset")
    result = json.loads(predict("step"))
    for field in ("next_topic", "difficulty", "engagement_score", "status"):
        assert field in result, f"Missing field: {field}"
    print(f"    OK — next_topic={result['next_topic']}, difficulty={result['difficulty']}, engagement={result['engagement_score']}")

    print("\n" + "=" * 60)
    print("ALL 8 TESTS PASSED")
    print("=" * 60)
    sys.exit(0)
