"""Assessment Timing Agent — decides when to trigger assessments."""

from curriculum_flow_env.agents.base import AgentInterface


class AssessmentTimingAgent(AgentInterface):
    """Heuristic: assess if (idle > 10 AND accuracy > 0.7) OR (idle > 25)."""

    def reset(self):
        pass

    def select_action(self, obs: dict, info: dict) -> int:
        current_topic = obs["current_topic"]
        time_since = obs["time_since_review"][current_topic]
        recent = obs["recent_accuracy"]
        recent_acc = sum(recent) / max(len(recent), 1)

        if time_since > 25:
            return 1
        if time_since > 10 and recent_acc > 0.7:
            return 1
        return 0

    def update(self, obs: dict, reward: float, done: bool):
        pass
