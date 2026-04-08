"""Agent interface — abstract base class for all curriculum agents."""

from abc import ABC, abstractmethod


class AgentInterface(ABC):
    """Base class for CurriculumFlowENV agents."""

    @abstractmethod
    def reset(self) -> None:
        """Reset agent state for a new episode."""

    @abstractmethod
    def select_action(self, obs: dict, info: dict) -> int:
        """Choose an action given the current observation."""

    @abstractmethod
    def update(self, obs: dict, reward: float, done: bool) -> None:
        """Update agent after environment step."""
