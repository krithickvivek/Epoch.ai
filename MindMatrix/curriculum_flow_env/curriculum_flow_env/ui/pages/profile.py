"""Profile tab — student learning results and insights."""

import gradio as gr

from curriculum_flow_env.ui.charts import make_mastery_radar, make_strengths_chart, empty_fig
from curriculum_flow_env.simulation.curriculum import TOPIC_GROUPS


def build_profile_tab():
    """Build the Profile tab. Returns dict of component references."""
    components = {}

    gr.Markdown("### Student Learning Profile")
    gr.Markdown("*Run a simulation to see your personalized learning profile and insights.*")

    with gr.Row():
        with gr.Column(scale=1):
            components["radar"] = gr.Plot(
                label="Subject Area Mastery",
                value=make_mastery_radar({g: 0.0 for g in TOPIC_GROUPS}),
            )
        with gr.Column(scale=1):
            components["insights"] = gr.Markdown(
                value="**No data yet.** Click *Reset & Start* on the Dashboard tab, "
                      "then run an episode to generate your learning profile."
            )

    gr.Markdown("---")
    gr.Markdown("### Topic Progress")
    components["strengths_chart"] = gr.Plot(
        label="All Topics Ranked by Mastery",
        value=empty_fig("No topics started yet", 300),
    )

    gr.Markdown("### Detailed Results")
    components["results_table"] = gr.Dataframe(
        headers=["Topic", "Group", "Mastery Level", "Prereq Status"],
        label="Full Topic Breakdown",
        row_count=20,
    )

    return components
