"""
CurriculumFlowENV — OpenEnv FastAPI Application

This is the OpenEnv-compatible server entry point. It uses create_app()
to provide WebSocket /ws, HTTP /reset /step /state, /health, /docs,
and the /web interactive interface.

The EXISTING web platform (login, quizzes, chatbot, etc.) runs via
curriculum_flow_env.server:app. This module is the OpenEnv RL interface.

Usage:
    # Development:
    uvicorn server.app:app --reload --host 0.0.0.0 --port 8000

    # Production:
    uvicorn server.app:app --host 0.0.0.0 --port 8000 --workers 4
"""

from openenv.core import create_app

from models import CurriculumAction, CurriculumObservation
from server.curriculum_environment import CurriculumEnvironment

app = create_app(
    CurriculumEnvironment,
    CurriculumAction,
    CurriculumObservation,
    env_name="curriculum_flow_env",
)


def main():
    """Entry point for direct execution."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
