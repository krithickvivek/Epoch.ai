"""
CurriculumFlowENV — OpenEnv Environment Implementation

Wraps the existing CurriculumFlowEnv (gymnasium) into an OpenEnv-compatible
Environment that works with create_app(), WebSocket sessions, and the
full OpenEnv ecosystem.
"""

import uuid
from typing import Any, Optional

from openenv.core import Environment

from models import CurriculumAction, CurriculumObservation, CurriculumState
from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.simulation.curriculum import TOPIC_NAMES


class CurriculumEnvironment(
    Environment[CurriculumAction, CurriculumObservation, CurriculumState]
):
    """OpenEnv wrapper around the gymnasium CurriculumFlowEnv.

    Each WebSocket session gets its own instance of this class,
    providing full isolation between concurrent users/agents.
    """

    SUPPORTS_CONCURRENT_SESSIONS = True

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self._env = CurriculumFlowEnv(archetype="steady", max_steps=200)
        self._episode_id: Optional[str] = None

    # ------------------------------------------------------------------
    # OpenEnv required: reset
    # ------------------------------------------------------------------
    def reset(
        self,
        seed: Optional[int] = None,
        episode_id: Optional[str] = None,
        **kwargs: Any,
    ) -> CurriculumObservation:
        self._episode_id = episode_id or str(uuid.uuid4())

        archetype = kwargs.get("archetype", None)
        options = {"archetype": archetype} if archetype else None
        obs, info = self._env.reset(seed=seed, options=options)

        return self._make_observation(obs, info, reward=0.0, done=False)

    # ------------------------------------------------------------------
    # OpenEnv required: step
    # ------------------------------------------------------------------
    def step(
        self,
        action: CurriculumAction,
        timeout_s: Optional[float] = None,
        **kwargs: Any,
    ) -> CurriculumObservation:
        gym_action = {
            "topic": action.topic,
            "difficulty": action.difficulty,
            "assess": action.assess,
        }
        obs, reward, terminated, truncated, info = self._env.step(gym_action)
        done = terminated or truncated
        return self._make_observation(obs, info, reward=reward, done=done)

    # ------------------------------------------------------------------
    # OpenEnv required: state (property)
    # ------------------------------------------------------------------
    @property
    def state(self) -> CurriculumState:
        s = self._env.state()
        return CurriculumState(
            episode_id=self._episode_id,
            step_count=s["step_count"],
            student_archetype=s["student"]["archetype"],
            mastery=s["student"]["mastery"],
            engagement=s["student"]["engagement"],
            completion_rate=s["completion_rate"],
            topics_mastered=s["topics_mastered"],
            cumulative_reward=s["cumulative_reward"],
            max_steps=s["max_steps"],
        )

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------
    def get_metadata(self):
        # Use the parent's EnvironmentMetadata via super() to find the correct class
        base_meta = super().get_metadata()
        meta_cls = type(base_meta)
        return meta_cls(
            name="CurriculumFlowENV",
            description=(
                "Multi-agent RL environment for adaptive curriculum optimization. "
                "Three agents (topic sequencer, difficulty adapter, assessment timer) "
                "jointly personalize education using Ebbinghaus forgetting curves."
            ),
            version="1.0.0",
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _obs_to_list(obs: dict) -> dict:
        """Convert numpy arrays to plain lists."""
        return {
            k: v.tolist() if hasattr(v, "tolist") else v
            for k, v in obs.items()
        }

    def _make_observation(
        self, obs: dict, info: dict, reward: float, done: bool
    ) -> CurriculumObservation:
        o = self._obs_to_list(obs)
        topic_id = info.get("topic_id", 0)
        return CurriculumObservation(
            mastery=o.get("mastery", []),
            engagement=o.get("engagement", []),
            recent_accuracy=o.get("recent_accuracy", []),
            time_since_review=o.get("time_since_review", []),
            current_topic=o.get("current_topic", 0),
            unlocked_mask=o.get("unlocked_mask", []),
            step=info.get("step", 0),
            episode_reward=info.get("episode_reward", 0.0),
            topics_mastered=info.get("topics_mastered", 0),
            completion_rate=info.get("completion_rate", 0.0),
            student_archetype=info.get("student_archetype", ""),
            topic_name=info.get("topic_name", TOPIC_NAMES[topic_id] if topic_id < len(TOPIC_NAMES) else ""),
            difficulty_level=info.get("difficulty", 0),
            assessed=info.get("assessed", False),
            assessment_result=info.get("assessment_result"),
            correct=info.get("correct"),
            reward_components=info.get("reward_components", {}),
            reward=reward,
            done=done,
        )
