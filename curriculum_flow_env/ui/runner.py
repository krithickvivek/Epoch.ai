"""SimulationRunner — manages env + agents + history, independent of UI."""

from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.simulation.curriculum import NUM_TOPICS, TOPIC_NAMES, TOPIC_GROUPS
from curriculum_flow_env.agents import (
    TopicSequencerAgent, DifficultyAdaptAgent, AssessmentTimingAgent,
)
from curriculum_flow_env.ui.formatting import obs_to_json


class SimulationRunner:
    """Encapsulates simulation state for the dashboard."""

    def __init__(self):
        self.env: CurriculumFlowEnv | None = None
        self.obs: dict | None = None
        self.sequencer = TopicSequencerAgent()
        self.diff_agent = DifficultyAdaptAgent()
        self.assess_agent = AssessmentTimingAgent()
        self.mastery_history: list[list[float]] = []
        self.decisions: list[list] = []
        self.episode_log: list[list] = []
        self.episode_rewards_agg: list[dict] = []
        self.episode_count: int = 0

    @property
    def is_ready(self) -> bool:
        return self.env is not None and self.obs is not None

    @property
    def is_done(self) -> bool:
        if not self.is_ready:
            return True
        return self.env.step_count >= self.env.max_steps

    def reset(self, archetype: str = "steady", max_steps: int = 200):
        self.env = CurriculumFlowEnv(archetype=archetype, max_steps=max_steps)
        obs, info = self.env.reset()
        self.obs = obs
        self.sequencer.reset()
        self.diff_agent.reset()
        self.assess_agent.reset()
        self.mastery_history = [obs["mastery"].tolist()]
        self.decisions = []

    def step(self) -> dict | None:
        """Run one step. Returns info dict or None if done."""
        if not self.is_ready or self.is_done:
            return None

        obs_dict = obs_to_json(self.obs)
        info_dict = {"unlocked_mask": obs_dict["unlocked_mask"]}

        topic = self.sequencer.select_action(obs_dict, info_dict)
        difficulty = self.diff_agent.select_action(obs_dict, info_dict) - 1
        assess = self.assess_agent.select_action(obs_dict, info_dict)

        action = {"topic": topic, "difficulty": difficulty, "assess": assess}
        obs, reward, terminated, truncated, info = self.env.step(action)

        self.sequencer.update(obs_dict, reward, terminated or truncated)
        self.diff_agent.update(obs_dict, reward, terminated or truncated)
        self.assess_agent.update(obs_dict, reward, terminated or truncated)

        self.obs = obs
        self.mastery_history.append(obs["mastery"].tolist())
        self.decisions.append([
            info["step"], info.get("topic_name", ""),
            info.get("difficulty", 0),
            "Yes" if info.get("assessed", False) else "No",
            f"{reward:.1f}",
        ])

        if terminated or truncated:
            self._log_episode(info)

        return info

    def run_episode(self) -> dict | None:
        """Run a full episode. Returns final info."""
        if not self.is_ready:
            return None
        info = None
        while not self.is_done:
            result = self.step()
            if result is not None:
                info = result
            comp = self.env.topic_graph.completion_rate(self.env.student.mastery)
            if comp >= 0.95:
                break
        return info

    def run_batch(self, n: int, archetype: str = "steady", max_steps: int = 200):
        """Run n full episodes."""
        for _ in range(n):
            self.reset(archetype, max_steps)
            self.run_episode()

    def _log_episode(self, info: dict):
        self.episode_count += 1
        self.episode_log = (self.episode_log + [[
            self.episode_count, info["student_archetype"],
            info["step"], info["topics_mastered"],
            f"{info['completion_rate']:.1%}", f"{info['episode_reward']:.1f}",
        ]])[-50:]
        total_comps = {}
        for comp_log in self.env.reward_components_log:
            for k, v in comp_log.items():
                total_comps[k] = total_comps.get(k, 0) + v
        self.episode_rewards_agg = (self.episode_rewards_agg + [total_comps])[-10:]

    def get_mastery(self) -> list[float]:
        if not self.is_ready:
            return [0.0] * NUM_TOPICS
        return self.obs["mastery"].tolist()

    def get_unlocked_mask(self) -> list[int]:
        if not self.is_ready:
            return [1, 1, 1] + [0] * 17
        return self.obs["unlocked_mask"].tolist()

    def get_engagement(self) -> float:
        if not self.is_ready:
            return 0.8
        return float(self.obs["engagement"][0])

    def get_recent_accuracy(self) -> float:
        if not self.is_ready:
            return 0.0
        recent = self.obs["recent_accuracy"].tolist()
        nonzero = [r for r in recent if r > 0]
        return sum(nonzero) / len(nonzero) if nonzero else 0.0

    def get_topics_mastered(self) -> int:
        if not self.is_ready:
            return 0
        return sum(
            1 for t in range(NUM_TOPICS)
            if self.env.topic_graph.is_mastered(t, self.env.student.mastery)
        )

    def get_completion_rate(self) -> float:
        if not self.is_ready:
            return 0.0
        return self.env.topic_graph.completion_rate(self.env.student.mastery)

    def get_cumulative_reward(self) -> float:
        if not self.is_ready:
            return 0.0
        return self.env.cumulative_reward

    def get_archetype(self) -> str:
        if not self.is_ready:
            return "steady"
        return self.env.student.archetype

    def get_current_topic_name(self) -> str:
        if not self.is_ready:
            return "counting"
        return TOPIC_NAMES[self.env.student.current_topic]

    def get_step_count(self) -> int:
        if not self.is_ready:
            return 0
        return self.env.step_count

    def get_max_steps(self) -> int:
        if not self.is_ready:
            return 200
        return self.env.max_steps

    def get_group_mastery(self) -> dict[str, float]:
        mastery = self.get_mastery()
        result = {}
        for group, ids in TOPIC_GROUPS.items():
            result[group] = sum(mastery[t] for t in ids) / len(ids)
        return result
