"""
CurriculumFlowENV — OpenEnv Client

Provides type-safe client for connecting to a CurriculumFlowENV server.

Example (async):
    >>> import asyncio
    >>> from client import CurriculumEnv
    >>> from models import CurriculumAction
    >>>
    >>> async def main():
    ...     async with CurriculumEnv(base_url="http://localhost:8000") as env:
    ...         obs = await env.reset()
    ...         print(f"Topics: {len(obs.mastery)}, Archetype: {obs.student_archetype}")
    ...
    ...         obs = await env.step(CurriculumAction(topic=0, difficulty=2, assess=0))
    ...         print(f"Reward: {obs.reward}, Done: {obs.done}")
    >>>
    >>> asyncio.run(main())

Example (sync):
    >>> with CurriculumEnv(base_url="http://localhost:8000").sync() as env:
    ...     obs = env.reset()
    ...     obs = env.step(CurriculumAction(topic=0, difficulty=2, assess=0))
    ...     print(f"Reward: {obs.reward}")

Example (from HuggingFace Space):
    >>> env = CurriculumEnv.from_env("krithickvivek/epoch-ai")
"""

from openenv.core import EnvClient

from models import CurriculumAction, CurriculumObservation, CurriculumState


class CurriculumEnv(
    EnvClient[CurriculumAction, CurriculumObservation, CurriculumState]
):
    """Client for the CurriculumFlowENV adaptive learning environment.

    Connects via WebSocket for efficient multi-step RL episodes.
    Each connection gets an isolated environment instance server-side.
    """

    pass  # EnvClient provides all needed functionality
