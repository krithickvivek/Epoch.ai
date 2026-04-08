# Epoch.ai
Epoch.ai — an AI-powered adaptive learning platform where reinforcement learning agents personalise your study path in real time. Three agents decide what to teach next, at what difficulty, and when to assess. Covering Aptitude, Reasoning, and Coding with quizzes, practice problems, and live growth tracking. Every session is a turning point.

![Python 3.11](https://img.shields.io/badge/python-3.11-blue)
![OpenENV 0.1](https://img.shields.io/badge/OpenENV-0.1-green)
![License](https://img.shields.io/badge/license-Apache--2.0-orange)

Multi-agent reinforcement learning environment and web app for adaptive placement preparation.

## Environment Description

`Epoch.ai` is a `gymnasium.Env` that simulates a learner moving through a prerequisite-aware curriculum.

- Topic space: 40 placement topics across quantitative aptitude, logical reasoning, verbal ability, data interpretation, and programming.
- Student model: engagement dynamics + forgetting over time + mastery progression.
- Baseline agents:
1. Topic Sequencer
2. Difficulty Adapter
3. Assessment Timer
- Episode objective: maximize mastery and completion while avoiding low-engagement and wasted practice.

Core implementation:
- Environment: `curriculum_flow_env/env.py`
- Student dynamics: `curriculum_flow_env/simulation/student.py`
- Reward function: `curriculum_flow_env/rewards.py`
- Curriculum graph/constants: `curriculum_flow_env/simulation/curriculum.py`

## Observation Space

The environment exposes a `spaces.Dict` observation:

| Key | Type | Shape | Range | Meaning |
|---|---|---|---|---|
| `mastery` | `Box` | `(40,)` | `[0, 1]` | Topic-wise mastery level |
| `engagement` | `Box` | `(1,)` | `[0, 1]` | Current engagement |
| `recent_accuracy` | `Box` | `(10,)` | `[0, 1]` | Last 10 response outcomes |
| `time_since_review` | `Box` | `(40,)` | `[0, 50]` | Steps since last review per topic (clipped) |
| `current_topic` | `Discrete(40)` | scalar | `[0, 39]` | Last/active topic id |
| `unlocked_mask` | `MultiBinary` | `(40,)` | `{0, 1}` | Which topics are currently unlocked |

## Action Space

The environment accepts a `spaces.Dict` action:

| Key | Type | Range | Meaning |
|---|---|---|---|
| `topic` | `Discrete(40)` | `[0, 39]` | Topic selected for next interaction |
| `difficulty` | `Discrete(5)` | `[0, 4]` | Mapped internally to difficulty levels `1..5` |
| `assess` | `Discrete(2)` | `{0, 1}` | `0 = practice`, `1 = assessment` |

## Episode End Conditions

- `terminated = True` when completion rate reaches `>= 95%`
- `truncated = True` when `max_steps` is reached (default `200`)

## Reward Overview

The reward is a weighted sum of components (see `curriculum_flow_env/rewards.py`):

- `milestone_bonus`: +25 when a topic crosses mastery threshold (`0.8`)
- `learning_gain`: positive reward for incremental mastery gain
- `stretch_reward`: +10 for correct high-difficulty attempts
- `assessment_reward`: +5 (strong assessment) or -3 (weak assessment)
- `dropout_penalty`: negative when engagement is critically low
- `opportunity_cost`: -4 for practicing already-mastered topics
- `retention_penalty`: negative when previously-mastered topics decay below threshold
- `completion_bonus`: +50 when curriculum completion reaches `95%`

## Student Archetypes

Available archetypes:

- `fast`
- `steady`
- `struggling`
- `bursty`
- `anxious`

Each archetype sets:
- `base_learning_rate`
- `forgetting_rate`
- `engagement_decay`

## Setup Instructions

### 1) Prerequisites

- Python `3.11+`
- `pip`

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Optional environment variables

If you use Hugging Face powered chat/quiz generation in the web app:

```bash
# Windows PowerShell
$env:HF_API_KEY="your_hf_api_key"
$env:HF_CHAT_MODEL="mistralai/Mistral-7B-Instruct-v0.3"
$env:HF_QUIZ_MODEL="Qwen/Qwen2.5-7B-Instruct"
```

```bash
# Linux/macOS
export HF_API_KEY="your_hf_api_key"
export HF_CHAT_MODEL="mistralai/Mistral-7B-Instruct-v0.3"
export HF_QUIZ_MODEL="Qwen/Qwen2.5-7B-Instruct"
```

### 4) Run the application

Option A (recommended in this repo):

```bash
python run.py
```

Option B (direct uvicorn):

```bash
uvicorn curriculum_flow_env.server:app --host 0.0.0.0 --port 7860 --reload
```

Open:
- Web app: `http://127.0.0.1:7860`
- API docs: `http://127.0.0.1:7860/docs`

### 5) Run tests

```bash
pytest tests/ -v --tb=short
```

## API Endpoints (Core)

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/reset` | `POST` | Reset environment (`archetype`, `seed`) |
| `/api/step` | `POST` | Apply action and get next transition |
| `/api/state` | `GET` | Full serializable environment state |
| `/health` | `GET` | Health/status |
| `/spec` | `GET` | OpenENV spec payload |

## Minimal Usage Example

```python
from curriculum_flow_env.env import CurriculumFlowEnv

env = CurriculumFlowEnv(archetype="steady", max_steps=200, seed=42)
obs, info = env.reset()

action = {"topic": 0, "difficulty": 2, "assess": 0}
obs, reward, terminated, truncated, info = env.step(action)
```

## License

Apache-2.0
