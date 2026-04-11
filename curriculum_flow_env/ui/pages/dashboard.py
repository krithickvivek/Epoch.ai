"""Dashboard tab — main simulation controls and live metrics."""

import gradio as gr

from curriculum_flow_env.ui.charts import make_heatmap, make_learning_curves_overview, empty_fig
from curriculum_flow_env.simulation.curriculum import NUM_TOPICS


def build_dashboard_tab():
    """Build the Dashboard tab components. Returns dict of component references."""
    components = {}

    with gr.Row():
        components["archetype"] = gr.Radio(
            ["fast", "steady", "struggling", "bursty", "anxious"],
            value="steady", label="Student Archetype",
        )
        components["max_steps"] = gr.Slider(50, 500, value=200, step=10, label="Max Steps")

    with gr.Row():
        components["reset_btn"] = gr.Button("Reset & Start", variant="primary", size="lg")
        components["step_btn"] = gr.Button("Step Once", size="lg")
        components["run_btn"] = gr.Button("Run Full Episode", variant="secondary", size="lg")
        components["batch_btn"] = gr.Button("Run 10 Episodes", size="lg")

    gr.Markdown("### Live Metrics")
    with gr.Row():
        components["step_text"] = gr.Textbox(label="Progress", value="Ready to begin", interactive=False)
        components["mastered_text"] = gr.Textbox(label="Topics Mastered", value="No topics mastered yet — keep going!", interactive=False)
        components["completion_text"] = gr.Textbox(label="Completion", value="0%", interactive=False)
        components["reward_text"] = gr.Textbox(label="Episode Performance", value="--", interactive=False)

    gr.Markdown("### Topic Mastery")
    with gr.Row():
        with gr.Column(scale=2):
            default_mastery = [0.0] * NUM_TOPICS
            default_mask = [1, 1, 1] + [0] * 17
            components["heatmap"] = gr.Plot(
                label="Topic Mastery Heatmap",
                value=make_heatmap(default_mastery, default_mask),
            )
        with gr.Column(scale=1):
            components["engagement_text"] = gr.Textbox(
                label="Engagement Level", value="Highly engaged (80%)", interactive=False,
            )
            components["student_info"] = gr.Textbox(
                label="Current Activity", lines=3, interactive=False,
                value="Archetype: Steady\nTopic: Counting\nRecent accuracy: 0%",
            )

    gr.Markdown("### Recent Decisions")
    components["decisions_df"] = gr.Dataframe(
        headers=["Step", "Topic", "Difficulty", "Assessed?", "Reward"],
        label="Agent Decisions (Last 5)", row_count=5,
    )

    gr.Markdown("### Overview")
    components["overview_chart"] = gr.Plot(
        label="Learning Progress", value=make_learning_curves_overview([]),
    )

    return components
