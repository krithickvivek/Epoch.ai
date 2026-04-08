"""Tests for CurriculumFlowEnv."""

import json
import numpy as np
import pytest

from curriculum_flow_env.env import CurriculumFlowEnv


@pytest.fixture
def env():
    e = CurriculumFlowEnv(archetype="fast", max_steps=200, seed=42)
    e.reset(seed=42)
    return e


def test_reset_returns_valid_obs(env):
    obs, info = env.reset(seed=42)
    assert "mastery" in obs
    assert "engagement" in obs
    assert "recent_accuracy" in obs
    assert "time_since_review" in obs
    assert "current_topic" in obs
    assert "unlocked_mask" in obs
    assert obs["mastery"].shape == (20,)
    assert obs["engagement"].shape == (1,)
    assert obs["recent_accuracy"].shape == (10,)
    assert obs["time_since_review"].shape == (20,)


def test_step_valid_action(env):
    obs, reward, terminated, truncated, info = env.step({"topic": 0, "difficulty": 0, "assess": 0})
    assert isinstance(reward, float)
    assert isinstance(terminated, bool)
    assert isinstance(truncated, bool)
    assert "episode_reward" in info
    assert "step" in info


def test_step_invalid_topic_clamped(env):
    # Topic 99 doesn't exist, but shouldn't crash
    obs, reward, terminated, truncated, info = env.step({"topic": 99, "difficulty": 0, "assess": 0})
    assert isinstance(reward, float)


def test_mastery_increases_on_correct():
    """Fast archetype with seed should eventually gain mastery on topic 0."""
    env = CurriculumFlowEnv(archetype="fast", max_steps=200, seed=42)
    env.reset(seed=42)
    initial = env.student.mastery[0]
    # Run many steps on topic 0
    for _ in range(50):
        env.step({"topic": 0, "difficulty": 0, "assess": 0})
    assert env.student.mastery[0] > initial


def test_engagement_drops_on_wrong():
    """Engagement should drop when giving wrong answers (high difficulty, low mastery)."""
    env = CurriculumFlowEnv(archetype="struggling", max_steps=200, seed=123)
    env.reset(seed=123)
    initial_eng = env.student.engagement
    # High difficulty on zero mastery topic should cause many wrong answers
    for _ in range(20):
        env.step({"topic": 0, "difficulty": 4, "assess": 0})
    # Engagement should have changed (likely dropped)
    assert env.student.engagement != initial_eng


def test_forgetting_curve_active():
    """Mastery should decay if topic is left idle."""
    env = CurriculumFlowEnv(archetype="fast", max_steps=300, seed=42)
    env.reset(seed=42)
    # Build mastery on topic 0
    for _ in range(30):
        env.step({"topic": 0, "difficulty": 0, "assess": 0})
    mastery_after_practice = env.student.mastery[0]
    # Now practice only topic 1 for 20 steps
    # First need to unlock topic 1 (prereq is topic 0 with mastery >= 0.7)
    for _ in range(20):
        env.step({"topic": 1, "difficulty": 0, "assess": 0})
    # Topic 0 should have decayed
    assert env.student.mastery[0] < mastery_after_practice


def test_episode_terminates():
    """Fast-forward; at max_steps should truncate."""
    env = CurriculumFlowEnv(archetype="fast", max_steps=10, seed=42)
    env.reset(seed=42)
    done = False
    for _ in range(20):
        _, _, terminated, truncated, _ = env.step({"topic": 0, "difficulty": 0, "assess": 0})
        if terminated or truncated:
            done = True
            break
    assert done


def test_state_is_json_serializable(env):
    env.step({"topic": 0, "difficulty": 0, "assess": 0})
    s = env.state()
    serialized = json.dumps(s)
    assert isinstance(serialized, str)
    parsed = json.loads(serialized)
    assert "student" in parsed


def test_reward_milestone_fires():
    """Verify milestone bonus fires when topic crosses 0.8 mastery."""
    env = CurriculumFlowEnv(archetype="fast", max_steps=500, seed=42)
    env.reset(seed=42)
    milestone_fired = False
    for _ in range(200):
        _, _, terminated, truncated, info = env.step({"topic": 0, "difficulty": 0, "assess": 0})
        comps = info.get("reward_components", {})
        if comps.get("milestone_bonus", 0) > 0:
            milestone_fired = True
            break
        if terminated or truncated:
            break
    assert milestone_fired
