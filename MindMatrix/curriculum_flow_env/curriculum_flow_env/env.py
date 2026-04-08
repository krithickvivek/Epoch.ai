"""Core Gymnasium environment for CurriculumFlowENV."""

import json
import random
from typing import Any

import gymnasium as gym
import numpy as np
from gymnasium import spaces

from curriculum_flow_env.simulation.topic_graph import TopicGraph
from curriculum_flow_env.simulation.student import StudentModel
from curriculum_flow_env.simulation.curriculum import NUM_TOPICS, TOPIC_NAMES
from curriculum_flow_env.agents.topic_sequencer import TopicSequencerAgent
from curriculum_flow_env.agents.difficulty_adapt import DifficultyAdaptAgent
from curriculum_flow_env.agents.assessment_timer import AssessmentTimingAgent
from curriculum_flow_env.rewards import compute_reward


class CurriculumFlowEnv(gym.Env):
    """Multi-agent RL environment for adaptive curriculum optimization."""

    metadata = {"render_modes": ["human"]}

    def __init__(self, archetype: str | None = None, max_steps: int = 200, seed: int | None = None):
        super().__init__()
        self.default_archetype = archetype
        self.max_steps = max_steps

        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

        self.topic_graph = TopicGraph()
        self.student = StudentModel(self.topic_graph, archetype)

        # Baseline agents
        self.sequencer = TopicSequencerAgent()
        self.difficulty_agent = DifficultyAdaptAgent()
        self.assessment_agent = AssessmentTimingAgent()

        # Spaces
        self.observation_space = spaces.Dict({
            "mastery": spaces.Box(0, 1, shape=(NUM_TOPICS,), dtype=np.float32),
            "engagement": spaces.Box(0, 1, shape=(1,), dtype=np.float32),
            "recent_accuracy": spaces.Box(0, 1, shape=(10,), dtype=np.float32),
            "time_since_review": spaces.Box(0, 50, shape=(NUM_TOPICS,), dtype=np.float32),
            "current_topic": spaces.Discrete(NUM_TOPICS),
            "unlocked_mask": spaces.MultiBinary(NUM_TOPICS),
        })
        self.action_space = spaces.Dict({
            "topic": spaces.Discrete(NUM_TOPICS),
            "difficulty": spaces.Discrete(5),
            "assess": spaces.Discrete(2),
        })

        self.step_count = 0
        self.cumulative_reward = 0.0
        self.reward_components_log: list[dict] = []

    def _get_obs(self) -> dict:
        raw = self.student.get_observation()
        unlocked = self.topic_graph.get_unlocked_topics(self.student.mastery)
        mask = [1 if i in unlocked else 0 for i in range(NUM_TOPICS)]
        return {
            "mastery": np.array(raw["mastery"], dtype=np.float32),
            "engagement": np.array([raw["engagement"]], dtype=np.float32),
            "recent_accuracy": np.array(raw["recent_accuracy"], dtype=np.float32),
            "time_since_review": np.array(raw["time_since_review"], dtype=np.float32),
            "current_topic": raw["current_topic"],
            "unlocked_mask": np.array(mask, dtype=np.int8),
        }

    def reset(self, seed: int | None = None, options: dict | None = None) -> tuple[dict, dict]:
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

        archetype = self.default_archetype
        if options and "archetype" in options:
            archetype = options["archetype"]

        self.student.reset(archetype)
        self.sequencer.reset()
        self.difficulty_agent.reset()
        self.assessment_agent.reset()
        self.step_count = 0
        self.cumulative_reward = 0.0
        self.reward_components_log = []

        obs = self._get_obs()
        info = {
            "episode_reward": 0.0,
            "topics_mastered": 0,
            "student_archetype": self.student.archetype,
            "completion_rate": 0.0,
            "step": 0,
        }
        return obs, info

    def step(self, action: dict[str, int]) -> tuple[dict, float, bool, bool, dict]:
        topic = action.get("topic", 0)
        difficulty = action.get("difficulty", 0) + 1  # Discrete(5) is 0-4, map to 1-5
        assess = action.get("assess", 0)

        # Validate topic
        unlocked = self.topic_graph.get_unlocked_topics(self.student.mastery)
        if topic not in unlocked:
            obs = self._get_obs()
            info_for_agent = {"unlocked_mask": obs["unlocked_mask"].tolist()}
            topic = self.sequencer.select_action(
                {**{k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}},
                info_for_agent,
            )

        # Clamp difficulty
        difficulty = max(1, min(5, difficulty))

        prev_mastery = dict(self.student.mastery)
        assessment_result = None
        correct = None

        if assess == 1:
            assessment_result = self.student.take_assessment(topic)
            # Assessment also updates mastery slightly based on performance
            if assessment_result >= 0.8:
                self.student.mastery[topic] = min(1.0, self.student.mastery[topic] + 0.05)
            elif assessment_result < 0.4:
                self.student.mastery[topic] = max(0.0, self.student.mastery[topic] - 0.02)
        else:
            correct = self.student.attempt_problem(topic, difficulty)

        # Compute reward
        reward, components = compute_reward(
            prev_mastery, self.student.mastery, self.student.engagement,
            assessment_result, topic, difficulty, self.topic_graph, self.step_count,
            correct=correct,
        )

        self.step_count += 1
        self.cumulative_reward += reward
        self.reward_components_log.append(components)

        obs = self._get_obs()
        completion = self.topic_graph.completion_rate(self.student.mastery)
        terminated = completion >= 0.95
        truncated = self.step_count >= self.max_steps

        topics_mastered = sum(
            1 for t in range(NUM_TOPICS)
            if self.topic_graph.is_mastered(t, self.student.mastery)
        )

        info = {
            "episode_reward": self.cumulative_reward,
            "topics_mastered": topics_mastered,
            "student_archetype": self.student.archetype,
            "completion_rate": completion,
            "step": self.step_count,
            "reward_components": components,
            "assessment_result": assessment_result,
            "correct": correct,
            "topic_name": TOPIC_NAMES[topic],
            "topic_id": topic,
            "difficulty": difficulty,
            "assessed": assess == 1,
        }

        # Update baseline agents
        obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}
        self.sequencer.update(obs_dict, reward, terminated or truncated)
        self.difficulty_agent.update(obs_dict, reward, terminated or truncated)
        self.assessment_agent.update(obs_dict, reward, terminated or truncated)

        return obs, reward, terminated, truncated, info

    def state(self) -> dict:
        """Full serializable state."""
        return {
            "student": {
                "archetype": self.student.archetype,
                "mastery": {str(k): v for k, v in self.student.mastery.items()},
                "engagement": self.student.engagement,
                "recent_responses": list(self.student.recent_responses),
                "time_since_review": {str(k): v for k, v in self.student.time_since_review.items()},
                "current_topic": self.student.current_topic,
            },
            "step_count": self.step_count,
            "max_steps": self.max_steps,
            "cumulative_reward": self.cumulative_reward,
            "completion_rate": self.topic_graph.completion_rate(self.student.mastery),
            "topics_mastered": sum(
                1 for t in range(NUM_TOPICS)
                if self.topic_graph.is_mastered(t, self.student.mastery)
            ),
            "reward_components_log": self.reward_components_log,
        }

    def render(self, mode: str = "human"):
        s = self.state()
        print(f"\n{'='*60}")
        print(f"CurriculumFlowENV | Step {s['step_count']}/{s['max_steps']}")
        print(f"Archetype: {s['student']['archetype']} | Engagement: {s['student']['engagement']:.2f}")
        print(f"Completion: {s['completion_rate']:.1%} | Reward: {s['cumulative_reward']:.1f}")
        print(f"Topics mastered: {s['topics_mastered']}/20")
        print(f"{'='*60}")
