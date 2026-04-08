"""Learning Curves tab — detailed per-group and per-topic learning curves."""

import gradio as gr

from curriculum_flow_env.ui.charts import (
    make_learning_curves_overview, make_learning_curves_group, empty_fig,
)
from curriculum_flow_env.simulation.curriculum import TOPIC_GROUPS, TOPIC_NAMES
from curriculum_flow_env.ui.formatting import mastery_to_label


def build_learning_curves_tab():
    """Build the Learning Curves tab. Returns dict of component references."""
    components = {}

    gr.Markdown(
        "### Learning Curves\n"
        "Track how mastery evolves over time across all topic groups. "
        "Each section below shows individual topic progress within that group."
    )

    components["overview"] = gr.Plot(
        label="All Groups Overview", value=make_learning_curves_overview([]),
    )

    gr.Markdown("---")
    gr.Markdown("### Detailed Breakdown by Subject Area")

    group_descriptions = {
        "arithmetic": "Foundation skills: counting, basic operations, fractions, decimals, percentages",
        "algebra": "Abstract reasoning: variables, equations, functions, polynomials",
        "geometry": "Spatial understanding: shapes, area, perimeter, trigonometry",
        "statistics": "Data analysis: basic statistics and probability",
        "calculus": "Advanced math: introduction to calculus concepts",
    }

    components["group_charts"] = {}
    components["group_tables"] = {}

    for group_name, topic_ids in TOPIC_GROUPS.items():
        with gr.Accordion(f"{group_name.title()} — {group_descriptions[group_name]}", open=False):
            components["group_charts"][group_name] = gr.Plot(
                label=f"{group_name.title()} Progress",
                value=make_learning_curves_group([], group_name, topic_ids),
            )
            # Per-topic mastery table
            headers = ["Topic", "Mastery Level", "Status"]
            default_rows = [
                [TOPIC_NAMES[t].replace("_", " ").title(), "Not started", "Locked"]
                for t in topic_ids
            ]
            components["group_tables"][group_name] = gr.Dataframe(
                headers=headers, value=default_rows,
                label=f"{group_name.title()} Topic Details",
            )

    return components
