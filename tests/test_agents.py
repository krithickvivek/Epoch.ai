"""Tests for heuristic baseline agents."""

import pytest
import numpy as np

from curriculum_flow_env.agents import (
    TopicSequencerAgent, DifficultyAdaptAgent, AssessmentTimingAgent,
)


def _make_obs(mastery=None, engagement=0.8, unlocked_mask=None, current_topic=0,
              recent_accuracy=None, time_since_review=None):
    if mastery is None:
        mastery = [0.0] * 20
    if unlocked_mask is None:
        unlocked_mask = [1, 1, 1] + [0] * 17  # first 3 unlocked
    if recent_accuracy is None:
        recent_accuracy = [0.5] * 10
    if time_since_review is None:
        time_since_review = [0] * 20
    return {
        "mastery": mastery,
        "engagement": engagement,
        "recent_accuracy": recent_accuracy,
        "time_since_review": time_since_review,
        "current_topic": current_topic,
        "unlocked_mask": unlocked_mask,
    }


def test_sequencer_picks_unlocked_topic():
    agent = TopicSequencerAgent()
    agent.reset()
    obs = _make_obs(unlocked_mask=[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    action = agent.select_action(obs, {})
    assert action in [0, 1, 2]


def test_difficulty_in_range():
    agent = DifficultyAdaptAgent()
    agent.reset()
    for mastery_val in [0.0, 0.2, 0.5, 0.8, 1.0]:
        obs = _make_obs(mastery=[mastery_val] * 20, current_topic=0)
        action = agent.select_action(obs, {})
        assert 1 <= action <= 5


def test_assessment_timer_binary():
    agent = AssessmentTimingAgent()
    agent.reset()
    obs = _make_obs()
    action = agent.select_action(obs, {})
    assert action in [0, 1]


def test_all_agents_survive_edge_cases():
    seq = TopicSequencerAgent()
    diff = DifficultyAdaptAgent()
    assess = AssessmentTimingAgent()

    # Zero mastery
    obs = _make_obs(mastery=[0.0] * 20, unlocked_mask=[1] * 20)
    seq.select_action(obs, {})
    diff.select_action(obs, {})
    assess.select_action(obs, {})

    # Full mastery
    obs = _make_obs(mastery=[1.0] * 20, unlocked_mask=[1] * 20)
    seq.select_action(obs, {})
    diff.select_action(obs, {})
    assess.select_action(obs, {})

    # Single topic unlocked
    obs = _make_obs(mastery=[0.5] * 20, unlocked_mask=[1] + [0] * 19)
    action = seq.select_action(obs, {})
    assert action == 0
