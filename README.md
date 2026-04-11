---
title: Epoch.ai
emoji: 📈
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: true
license: apache-2.0
short_description: AI-powered adaptive placement preparation platform
tags:
  - education
  - reinforcement-learning
  - placement-prep
  - fastapi
  - hackathon
---

# Epoch.ai — Learn. Adapt. Improve.

![Python 3.11](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green)
![License](https://img.shields.io/badge/license-Apache--2.0-orange)

**Epoch.ai** is an AI-powered adaptive learning platform built for Indian engineering students preparing for campus placements. It uses multi-agent reinforcement learning to personalize the learning path for each student.

## Features

- **Adaptive Learning** — 3 RL agents (Topic Sequencer, Difficulty Adapter, Assessment Timer) continuously optimize your study path
- **66 Topics** across 8 categories: Quantitative Aptitude, Logical Reasoning, Verbal Ability, Data Interpretation, Programming, DSA Deep Dive, Core CS, and Company-Specific prep
- **DSA Roadmap** — 170+ curated LeetCode problems organized by pattern with company tags
- **Company Prep** — Detailed strategies, exam patterns, and curated problems for 13+ companies (TCS, Infosys, Amazon, Google, Microsoft, etc.)
- **AI Quiz Generator** — Infinite practice quizzes powered by Qwen 2.5 via HuggingFace Inference
- **AI Chat Assistant** — Built-in Epoch AI chatbot for instant help with DSA, interviews, and study planning
- **Interview Simulator** — Practice mock interviews
- **Daily Planner** — Schedule and track your preparation
- **Growth Analytics** — Track mastery, quiz scores, and improvement trends
- **Dark/Light Mode** — Beautiful, responsive UI

## Tech Stack

- **Backend**: FastAPI + Gymnasium (RL environment)
- **Frontend**: Jinja2 + Custom CSS (glassmorphism design)
- **AI**: HuggingFace Inference API (Qwen 2.5-7B-Instruct)
- **Database**: SQLite
- **Deployment**: Docker on HuggingFace Spaces

## Architecture

The platform is built on a `gymnasium.Env` that simulates a learner moving through a prerequisite-aware curriculum:

- **Student Model**: Engagement dynamics + forgetting curves + mastery progression
- **Topic Graph**: 66 topics with prerequisite dependencies
- **Reward Function**: Weighted combination of learning gain, milestone bonuses, stretch rewards, and retention penalties
- **3 Baseline Agents**: Work together to select optimal topics, difficulty levels, and assessment timing

## Quick Start (Local)

```bash
pip install -r requirements.txt
python run.py
# Open http://localhost:7860
```

## Hackathon

Built for the **Scaler x HuggingFace x Meta Hackathon**.

## License

Apache-2.0
