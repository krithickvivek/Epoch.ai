"""Topic Sequencer Agent — chooses next topic to present."""

from curriculum_flow_env.simulation.curriculum import TOPIC_DIFFICULTIES
from curriculum_flow_env.agents.base import AgentInterface


class TopicSequencerAgent(AgentInterface):
    """Heuristic: pick unlocked topic with lowest mastery, break ties by easiest first."""

    def reset(self):
        pass

    def select_action(self, obs: dict, info: dict) -> int:
        mastery = obs["mastery"]
        unlocked_mask = obs["unlocked_mask"]
        unlocked = [i for i, m in enumerate(unlocked_mask) if m == 1]
        if not unlocked:
            return 0

        # Sort by mastery ascending, then difficulty ascending for ties
        unlocked.sort(key=lambda t: (mastery[t], TOPIC_DIFFICULTIES[t]))
        return unlocked[0]

    def update(self, obs: dict, reward: float, done: bool):
        pass
