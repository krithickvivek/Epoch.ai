"""Launch CurriculumFlowENV web application."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "curriculum_flow_env.server:app",
        host="0.0.0.0",
        port=7860,
        reload=True,
    )
