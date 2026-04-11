"""Reward function for CurriculumFlowENV — isolated for easy tuning."""

from curriculum_flow_env.simulation.curriculum import NUM_TOPICS, MASTERY_THRESHOLD


def compute_reward(
    prev_mastery: dict[int, float],
    new_mastery: dict[int, float],
    engagement: float,
    assessment_result: float | None,
    topic_id: int,
    difficulty: int,
    topic_graph,
    step: int,
    correct: bool | None = None,
) -> tuple[float, dict[str, float]]:
    """Compute reward and return (total_reward, component_breakdown)."""
    components = {
        "milestone_bonus": 0.0,
        "learning_gain": 0.0,
        "stretch_reward": 0.0,
        "assessment_reward": 0.0,
        "dropout_penalty": 0.0,
        "opportunity_cost": 0.0,
        "retention_penalty": 0.0,
        "completion_bonus": 0.0,
    }

    # Milestone bonus: +25 per topic crossing mastery threshold 0.8
    for t in range(NUM_TOPICS):
        if prev_mastery.get(t, 0.0) < MASTERY_THRESHOLD <= new_mastery.get(t, 0.0):
            components["milestone_bonus"] += 25.0

    # Incremental learning: +2 per 0.05 mastery gain
    for t in range(NUM_TOPICS):
        gain = new_mastery.get(t, 0.0) - prev_mastery.get(t, 0.0)
        if gain > 0:
            components["learning_gain"] += 2.0 * (gain / 0.05)

    # Stretch challenge: +10 if correct on difficulty >= 4
    if correct and difficulty >= 4:
        components["stretch_reward"] = 10.0

    # Assessment rewards/penalties
    if assessment_result is not None:
        if assessment_result >= 0.8:
            components["assessment_reward"] = 5.0
        elif assessment_result < 0.4:
            components["assessment_reward"] = -3.0

    # Dropout risk: scaled penalty when engagement is critically low
    if engagement < 0.3:
        components["dropout_penalty"] = -2.0 * (0.3 - engagement) / 0.3  # max -2.0 at eng=0

    # Opportunity cost: -4 for practicing already-mastered topic
    if topic_graph.is_mastered(topic_id, prev_mastery):
        components["opportunity_cost"] = -4.0

    # Retention failure: -2 per previously-mastered topic that lost mastery
    for t in range(NUM_TOPICS):
        if (prev_mastery.get(t, 0.0) >= MASTERY_THRESHOLD and
                new_mastery.get(t, 0.0) < MASTERY_THRESHOLD):
            components["retention_penalty"] -= 2.0

    # Completion bonus
    if topic_graph.completion_rate(new_mastery) >= 0.95:
        components["completion_bonus"] = 50.0

    total = sum(components.values())
    return total, components
