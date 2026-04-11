"""Tests for StudentModel simulation."""

import pytest

from curriculum_flow_env.simulation.topic_graph import TopicGraph
from curriculum_flow_env.simulation.student import StudentModel, ARCHETYPES


@pytest.fixture
def topic_graph():
    return TopicGraph()


def test_all_archetypes_construct(topic_graph):
    for archetype in ARCHETYPES:
        student = StudentModel(topic_graph, archetype=archetype)
        assert student.archetype == archetype
        assert student.engagement == 0.8
        assert all(v == 0.0 for v in student.mastery.values())


def test_mastery_clamped_01(topic_graph):
    student = StudentModel(topic_graph, archetype="fast")
    # Many attempts should never exceed 1.0 or go below 0.0
    for _ in range(100):
        student.attempt_problem(0, 1)
    for t in range(20):
        assert 0.0 <= student.mastery[t] <= 1.0


def test_assessment_returns_float(topic_graph):
    student = StudentModel(topic_graph, archetype="steady")
    score = student.take_assessment(0)
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_prerequisite_bonus_range(topic_graph):
    student = StudentModel(topic_graph, archetype="steady")
    for t in range(20):
        bonus = student.prerequisite_bonus(t)
        assert 1.0 <= bonus <= 1.5
