"""Human-readable label converters for all numerical data."""

from curriculum_flow_env.simulation.curriculum import TOPIC_NAMES, TOPIC_GROUPS, NUM_TOPICS


def mastery_to_label(value: float) -> str:
    pct = round(value * 100)
    if value < 0.05:
        return "Not started"
    elif value < 0.15:
        return f"Just started ({pct}%)"
    elif value < 0.30:
        return f"Beginning ({pct}%)"
    elif value < 0.50:
        return f"Developing ({pct}%)"
    elif value < 0.70:
        return f"Progressing ({pct}%)"
    elif value < 0.80:
        return f"Good understanding ({pct}%)"
    elif value < 0.90:
        return f"Strong understanding ({pct}%)"
    else:
        return f"Mastered ({pct}%)"


def mastery_to_emoji_label(value: float) -> str:
    pct = round(value * 100)
    if value < 0.05:
        return "-- Not started"
    elif value < 0.30:
        return f"Beginning - {pct}%"
    elif value < 0.50:
        return f"Developing - {pct}%"
    elif value < 0.70:
        return f"Progressing - {pct}%"
    elif value < 0.80:
        return f"Good - {pct}%"
    elif value < 0.90:
        return f"Strong - {pct}%"
    else:
        return f"Mastered! - {pct}%"


def engagement_to_label(value: float) -> str:
    pct = round(value * 100)
    if value >= 0.8:
        return f"Highly engaged ({pct}%)"
    elif value >= 0.6:
        return f"Engaged ({pct}%)"
    elif value >= 0.4:
        return f"Moderate focus ({pct}%)"
    elif value >= 0.2:
        return f"Losing focus ({pct}%)"
    else:
        return f"At risk of dropout ({pct}%)"


def reward_to_label(value: float) -> str:
    if value >= 200:
        return f"Excellent progress (+{value:.0f} pts)"
    elif value >= 50:
        return f"Good progress (+{value:.0f} pts)"
    elif value >= 0:
        return f"Slow progress (+{value:.0f} pts)"
    elif value >= -50:
        return f"Needs attention ({value:.0f} pts)"
    else:
        return f"Struggling ({value:.0f} pts)"


def difficulty_to_label(level: int) -> str:
    labels = {1: "Very Easy", 2: "Easy", 3: "Medium", 4: "Hard", 5: "Very Hard"}
    return labels.get(level, f"Level {level}")


def archetype_to_description(archetype: str) -> str:
    descriptions = {
        "fast": "Quick learner who picks up new concepts rapidly and retains them well. "
                "Thrives with challenging material and stays engaged throughout.",
        "steady": "Consistent and methodical learner. Makes reliable progress without rushing, "
                  "building a solid foundation step by step.",
        "struggling": "Learns at a slower pace and forgets more quickly. Benefits most from "
                      "repeated practice, simpler problems, and frequent review sessions.",
        "bursty": "Capable of rapid learning bursts but also forgets quickly. "
                  "Needs strategic review scheduling to lock in knowledge before it fades.",
        "anxious": "Has good learning potential but loses confidence easily after mistakes. "
                   "Needs careful difficulty calibration to stay in the comfort zone.",
    }
    return descriptions.get(archetype, "Unknown archetype")


def completion_to_label(rate: float, mastered: int, total: int = 20) -> str:
    pct = round(rate * 100)
    if rate >= 0.95:
        return f"Curriculum complete! ({mastered}/{total} topics)"
    elif rate >= 0.5:
        return f"Over halfway — {mastered}/{total} topics mastered ({pct}%)"
    elif rate > 0:
        return f"{mastered}/{total} topics mastered ({pct}%)"
    else:
        return "No topics mastered yet — keep going!"


def step_to_label(current: int, maximum: int) -> str:
    pct = round(current / maximum * 100) if maximum > 0 else 0
    if current == 0:
        return "Ready to begin"
    elif current >= maximum:
        return f"Episode complete ({maximum} steps)"
    else:
        return f"Step {current} of {maximum} ({pct}% through)"


def generate_profile_insights(mastery: list[float], engagement: float,
                               archetype: str, topics_mastered: int,
                               completion_rate: float) -> str:
    """Generate a human-readable paragraph summarizing the student's learning profile."""
    lines = []

    # Archetype intro
    lines.append(f"**Student type: {archetype.title()}** — {archetype_to_description(archetype)}")
    lines.append("")

    # Overall progress
    pct = round(completion_rate * 100)
    if topics_mastered == 0:
        lines.append(f"This learner has not yet mastered any topics ({pct}% overall completion). "
                     "The curriculum journey is just getting started.")
    elif completion_rate >= 0.95:
        lines.append(f"Outstanding! This learner has mastered {topics_mastered} of 20 topics "
                     f"and completed the curriculum!")
    else:
        lines.append(f"This learner has mastered **{topics_mastered} of 20** topics "
                     f"({pct}% completion).")

    # Strongest area
    group_masteries = {}
    for group_name, topic_ids in TOPIC_GROUPS.items():
        avg = sum(mastery[t] for t in topic_ids) / len(topic_ids)
        group_masteries[group_name] = avg

    if any(v > 0 for v in group_masteries.values()):
        strongest = max(group_masteries, key=group_masteries.get)
        weakest_active = min(
            (g for g, v in group_masteries.items() if v > 0.01),
            key=group_masteries.get,
            default=None,
        )
        strongest_pct = round(group_masteries[strongest] * 100)
        lines.append(f"Strongest area is **{strongest.title()}** (avg {strongest_pct}% mastery).")
        if weakest_active and weakest_active != strongest:
            weakest_pct = round(group_masteries[weakest_active] * 100)
            lines.append(f"Area needing most work: **{weakest_active.title()}** ({weakest_pct}%).")

    # Engagement
    lines.append("")
    lines.append(f"Current engagement: **{engagement_to_label(engagement)}**.")

    # Recommendations
    lines.append("")
    lines.append("### Recommendations")
    if engagement < 0.4:
        lines.append("- Engagement is low — try easier problems to rebuild confidence")
    if topics_mastered == 0:
        lines.append("- Focus on foundational topics (counting, addition, subtraction) first")
    elif completion_rate < 0.5:
        lines.append("- Continue building the foundation before advancing to harder topics")
    else:
        lines.append("- Good momentum — try increasing difficulty to reach mastery faster")

    # Find topics close to mastery
    almost = [t for t in range(NUM_TOPICS) if 0.65 <= mastery[t] < 0.80]
    if almost:
        names = [TOPIC_NAMES[t].replace("_", " ").title() for t in almost[:3]]
        lines.append(f"- Almost mastered: **{', '.join(names)}** — a few more practice sessions should do it!")

    return "\n".join(lines)


def obs_to_json(obs: dict) -> dict:
    """Convert numpy arrays in observation to JSON-safe types."""
    return {k: v.tolist() if hasattr(v, "tolist") else v for k, v in obs.items()}
