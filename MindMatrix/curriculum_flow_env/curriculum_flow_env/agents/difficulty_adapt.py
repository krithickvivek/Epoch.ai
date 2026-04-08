"""Difficulty Adaptation Agent — sets problem difficulty level."""

from curriculum_flow_env.agents.base import AgentInterface


class DifficultyAdaptAgent(AgentInterface):
    """Heuristic: difficulty proportional to current mastery (zone of proximal development)."""

    def reset(self):
        pass

    def select_action(self, obs: dict, info: dict) -> int:
        current_topic = obs["current_topic"]
        mastery = obs["mastery"][current_topic]
        difficulty = max(1, min(5, round(mastery * 5)))
        return difficulty

    def update(self, obs: dict, reward: float, done: bool):
        pass
