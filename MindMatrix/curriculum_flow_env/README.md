# CurriculumFlowENV

![Python 3.11](https://img.shields.io/badge/python-3.11-blue)
![OpenENV 0.1](https://img.shields.io/badge/OpenENV-0.1-green)
![License](https://img.shields.io/badge/license-Apache--2.0-orange)
![HF Spaces](https://img.shields.io/badge/%F0%9F%A4%97-Spaces-yellow)

**Multi-agent reinforcement learning environment for adaptive learning path optimization.**

## Problem Statement

Benjamin Bloom's landmark 1984 study showed that students receiving 1-on-1 tutoring performed two standard deviations above conventionally taught peers — the so-called **2 Sigma Problem**. The challenge: how do we replicate these outcomes at scale?

CurriculumFlowENV tackles this by creating a simulation where three specialized AI agents collaboratively design personalized learning paths. The environment models student cognition using Ebbinghaus forgetting curves, prerequisite mastery gating, and engagement dynamics across a 20-topic mathematics curriculum spanning arithmetic through calculus.

## Architecture

```
                    +-------------------+
                    |   Student Model   |
                    |  (5 archetypes)   |
                    +--------+----------+
                             |
                    observe  |  mastery, engagement,
                             |  recent_accuracy, ...
                             v
              +------------------------------+
              |      CurriculumFlowEnv       |
              |   (Gymnasium environment)    |
              +---+--------+--------+-------+
                  |        |        |
           topic  | diff   | assess |
                  v        v        v
          +-------+  +-----+  +--------+
          | Topic |  |Diff |  |Assess  |
          | Seqr  |  |Adapt|  |Timer   |
          +-------+  +-----+  +--------+
                  |        |        |
                  +---+----+---+----+
                      |        |
                      v        v
               reward signal   next observation
```

## Quick Start

```bash
# Clone
git clone https://github.com/your-username/curriculum-flow-env
cd curriculum-flow-env

# Install
pip install -r requirements.txt

# Run Gradio demo
python demo/app.py

# Or run API server
uvicorn curriculum_flow_env.server:app --host 0.0.0.0 --port 7860

# Or use Docker
docker build -t curriculum-flow-env .
docker run -p 7860:7860 curriculum-flow-env
```

## API Reference

| Endpoint | Method | Body | Response |
|----------|--------|------|----------|
| `/reset` | POST | `{"archetype": str\|null, "seed": int\|null}` | `{"observation": dict, "info": dict}` |
| `/step` | POST | `{"action": {"topic": int, "difficulty": int, "assess": int}}` | `{"observation": dict, "reward": float, "terminated": bool, "truncated": bool, "info": dict}` |
| `/state` | GET | — | `{"state": dict}` |
| `/health` | GET | — | `{"status": "ok", "env": "CurriculumFlowENV", "version": "0.1.0", "step": int}` |
| `/spec` | GET | — | OpenENV spec JSON |

## Observation Space

| Key | Type | Shape | Range | Description |
|-----|------|-------|-------|-------------|
| `mastery` | Box | (20,) | [0, 1] | Per-topic mastery level |
| `engagement` | Box | (1,) | [0, 1] | Student engagement |
| `recent_accuracy` | Box | (10,) | [0, 1] | Last 10 response outcomes |
| `time_since_review` | Box | (20,) | [0, 50] | Steps since last practice per topic |
| `current_topic` | Discrete | — | [0, 19] | Currently active topic |
| `unlocked_mask` | MultiBinary | (20,) | {0, 1} | Which topics are unlocked |

## Action Space

| Key | Type | Range | Description |
|-----|------|-------|-------------|
| `topic` | Discrete(20) | [0, 19] | Topic to present |
| `difficulty` | Discrete(5) | [0, 4] | Difficulty level (mapped to 1-5) |
| `assess` | Discrete(2) | {0, 1} | 0=practice, 1=assess |

## Student Archetypes

| Archetype | Learning Rate | Forgetting Rate | Engagement Decay | Profile |
|-----------|:---:|:---:|:---:|---------|
| **fast** | 0.22 | 0.015 | 0.01 | Quick learner, retains well |
| **steady** | 0.14 | 0.02 | 0.005 | Consistent, slow and steady |
| **struggling** | 0.08 | 0.04 | 0.02 | Needs extra support |
| **bursty** | 0.18 | 0.035 | 0.015 | Learns fast, forgets fast |
| **anxious** | 0.11 | 0.025 | 0.03 | Capable but easily discouraged |

## Reward Function

| Component | Value | Trigger |
|-----------|------:|---------|
| Milestone bonus | +25.0 | Topic crosses 0.8 mastery |
| Learning gain | +2.0 | Per 0.05 mastery increase |
| Stretch reward | +10.0 | Correct on difficulty >= 4 |
| Assessment reward | +5.0 | Assessment score >= 0.8 |
| Assessment penalty | -3.0 | Assessment score < 0.4 |
| Dropout penalty | -8.0 | Engagement < 0.2 |
| Opportunity cost | -4.0 | Practicing mastered topic |
| Retention penalty | -2.0 | Previously-mastered topic decays |
| Completion bonus | +50.0 | 95% curriculum completion |

## Training with Stable-Baselines3

```python
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from curriculum_flow_env import CurriculumFlowEnv

# Note: SB3 requires flat action/obs spaces — use a wrapper
env = CurriculumFlowEnv(archetype="steady", max_steps=200)
# model = PPO("MultiInputPolicy", env, verbose=1)
# model.learn(total_timesteps=100_000)
```

## Running Tests

```bash
pytest tests/ -v --tb=short
```

## Hackathon

Built for the **Meta x HuggingFace OpenENV Hackathon 2026**.

## License

Apache-2.0
