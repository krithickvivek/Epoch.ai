"""
Epoch.ai — OpenEnv Inference Script
CurriculumFlowENV: Multi-agent RL environment for adaptive learning path optimization.

This module provides:
  - Environment loading and reset
  - A `predict()` function that accepts an action and returns the next observation
  - A self-test that validates end-to-end operation
"""

import json
import sys

from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.simulation.curriculum import NUM_TOPICS


def load_environment(archetype: str = "steady", seed: int = 42) -> CurriculumFlowEnv:
    """Load and reset the CurriculumFlowENV gymnasium environment."""
    env = CurriculumFlowEnv(archetype=archetype, max_steps=200, seed=seed)
    env.reset(seed=seed)
    return env


# Global environment instance
_env = load_environment()


def predict(input_text: str) -> str:
    """
    Accept a JSON-encoded action (or plain text command) and return
    the environment's next observation, reward, and status.

    Supported inputs:
      - JSON action: '{"topic": 0, "difficulty": 2, "assess": 0}'
      - "reset"  : reset the environment
      - "state"  : return current state
      - "spec"   : return environment spec
      - Any other text: run one agent-recommended step

    Returns:
      JSON string with observation, reward, terminated, truncated, info.
    """
    global _env
    text = input_text.strip().lower()

    try:
        # Handle text commands
        if text == "reset":
            obs, info = _env.reset()
            return json.dumps({
                "command": "reset",
                "observation": _obs_to_dict(obs),
                "info": info,
            }, default=str)

        if text == "state":
            return json.dumps({
                "command": "state",
                "state": _env.state(),
            }, default=str)

        if text == "spec":
            return json.dumps({
                "command": "spec",
                "name": "CurriculumFlowENV",
                "num_topics": NUM_TOPICS,
                "max_steps": _env.max_steps,
                "action_space": {"topic": NUM_TOPICS, "difficulty": 5, "assess": 2},
            })

        # Try parsing as JSON action
        action = None
        if text not in ("step", "auto", "next"):
            try:
                action = json.loads(input_text)
            except (json.JSONDecodeError, ValueError):
                pass

        # If no explicit action, let agents decide
        if action is None:
            obs = _env._get_obs()
            info = _env.state()
            topic = _env.sequencer.select_action(obs, info)
            diff = _env.difficulty_agent.select_action(obs, info)
            assess = _env.assessment_agent.select_action(obs, info)
            action = {"topic": int(topic), "difficulty": int(diff), "assess": int(assess)}

        obs, reward, terminated, truncated, info = _env.step(action)

        result = {
            "action": action,
            "observation": _obs_to_dict(obs),
            "reward": float(reward),
            "terminated": bool(terminated),
            "truncated": bool(truncated),
            "info": info,
        }
        return json.dumps(result, default=str)

    except Exception as e:
        return json.dumps({"error": str(e)})


def _obs_to_dict(obs: dict) -> dict:
    """Convert numpy arrays in observation to JSON-serializable types."""
    out = {}
    for k, v in obs.items():
        try:
            out[k] = v.tolist()
        except AttributeError:
            out[k] = int(v) if hasattr(v, 'item') else v
    return out


# ---------------------------------------------------------------------------
# Self-test: validates that the environment runs end-to-end
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Epoch.ai / CurriculumFlowENV — Inference Self-Test")
    print("=" * 60)

    # 1. Reset
    print("\n[1] Reset environment")
    result = json.loads(predict("reset"))
    assert "observation" in result, "Reset must return an observation"
    print(f"    OK — observation keys: {list(result['observation'].keys())}")

    # 2. Agent-recommended step
    print("\n[2] Agent-recommended step")
    result = json.loads(predict("step"))
    assert "reward" in result, "Step must return a reward"
    print(f"    OK — reward={result['reward']:.4f}, terminated={result['terminated']}")

    # 3. Explicit action
    print("\n[3] Explicit action {topic:1, difficulty:2, assess:0}")
    result = json.loads(predict('{"topic": 1, "difficulty": 2, "assess": 0}'))
    assert "observation" in result, "Explicit action must return observation"
    print(f"    OK — reward={result['reward']:.4f}")

    # 4. State query
    print("\n[4] Query state")
    result = json.loads(predict("state"))
    assert "state" in result
    print(f"    OK — step_count={result['state'].get('step_count', 'N/A')}")

    # 5. Spec query
    print("\n[5] Query spec")
    result = json.loads(predict("spec"))
    assert result["name"] == "CurriculumFlowENV"
    print(f"    OK — {result['name']}, {result['num_topics']} topics")

    # 6. Multi-step rollout
    print("\n[6] Running 10-step rollout...")
    predict("reset")
    total_reward = 0.0
    for i in range(10):
        r = json.loads(predict("auto"))
        total_reward += r["reward"]
        if r["terminated"] or r["truncated"]:
            print(f"    Episode ended at step {i+1}")
            break
    print(f"    OK — total reward over rollout: {total_reward:.4f}")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)
    sys.exit(0)
