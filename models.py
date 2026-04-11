"""
CurriculumFlowENV — OpenEnv Type-Safe Models

Defines the typed Action, Observation, and State contracts for the
adaptive curriculum RL environment.
"""

from typing import Any, Dict, List, Optional

from openenv.core import Action, Observation, State


class CurriculumAction(Action):
    """Action for the curriculum environment.

    Agents choose a topic to study, a difficulty level, and whether to assess.
    """

    topic: int = 0  # Topic index (0 .. NUM_TOPICS-1)
    difficulty: int = 0  # Difficulty level (0-4, mapped to 1-5 internally)
    assess: int = 0  # 0 = study, 1 = take assessment


class CurriculumObservation(Observation):
    """Observation returned by the curriculum environment."""

    mastery: List[float] = []  # Per-topic mastery levels
    engagement: List[float] = []  # Student engagement [single value list]
    recent_accuracy: List[float] = []  # Last 10 accuracy scores
    time_since_review: List[float] = []  # Steps since each topic was reviewed
    current_topic: int = 0  # Currently selected topic index
    unlocked_mask: List[int] = []  # 1 if topic is unlocked, 0 otherwise

    # Episode progress
    step: int = 0
    episode_reward: float = 0.0
    topics_mastered: int = 0
    completion_rate: float = 0.0
    student_archetype: str = ""

    # Step details (populated after step, empty on reset)
    topic_name: str = ""
    difficulty_level: int = 0
    assessed: bool = False
    assessment_result: Optional[float] = None
    correct: Optional[bool] = None
    reward_components: Dict[str, Any] = {}


class CurriculumState(State):
    """Full internal state of the curriculum environment."""

    student_archetype: str = ""
    mastery: Dict[str, float] = {}
    engagement: float = 0.0
    completion_rate: float = 0.0
    topics_mastered: int = 0
    cumulative_reward: float = 0.0
    max_steps: int = 200
