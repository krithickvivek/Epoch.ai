"""Analytics tab — reward decomposition, episode history, archetype comparison."""

import gradio as gr

from curriculum_flow_env.ui.charts import (
    make_reward_decomposition, make_episode_comparison, empty_fig,
)


def build_analytics_tab():
    """Build the Analytics tab. Returns dict of component references."""
    components = {}

    gr.Markdown("### Reward Analysis")
    gr.Markdown(
        "See how different reward components contribute to the overall score. "
        "Positive components (green/blue) reward good teaching decisions; "
        "negative components (red) penalize suboptimal choices."
    )
    components["reward_chart"] = gr.Plot(
        label="Reward Breakdown", value=make_reward_decomposition([]),
    )

    components["reward_summary"] = gr.Markdown(
        value="*Run an episode to see reward analysis.*"
    )

    gr.Markdown("---")
    gr.Markdown("### Archetype Comparison")
    gr.Markdown("Run episodes with different archetypes to see how they compare.")
    components["comparison_chart"] = gr.Plot(
        label="Archetype Performance",
        value=empty_fig("Run multiple episodes to see comparisons", 300),
    )

    gr.Markdown("---")
    gr.Markdown("### Episode History")
    components["episode_df"] = gr.Dataframe(
        headers=["Episode", "Student Type", "Steps", "Mastered", "Completion", "Reward"],
        label="All Episodes", row_count=10,
    )

    return components
