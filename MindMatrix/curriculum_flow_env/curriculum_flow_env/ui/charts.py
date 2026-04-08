"""All Plotly chart builders for the dashboard."""

import numpy as np
import plotly.graph_objects as go

from curriculum_flow_env.simulation.curriculum import (
    TOPIC_NAMES, TOPIC_GROUPS, TOPIC_DIFFICULTIES, NUM_TOPICS,
)
from curriculum_flow_env.ui.formatting import mastery_to_label, difficulty_to_label

TOPIC_ABBREV = [
    "CNT", "ADD", "SUB", "MUL", "DIV", "FRC", "DEC", "PCT", "INT", "ALG",
    "LIN", "INQ", "FUN", "POL", "GEO", "A&P", "TRG", "STA", "PRB", "CAL",
]

GROUP_COLORS = {
    "arithmetic": "#2196f3", "algebra": "#ff9800", "geometry": "#4caf50",
    "statistics": "#9c27b0", "calculus": "#f44336",
}

LAYOUT_DEFAULTS = dict(
    template="simple_white",
    margin=dict(l=50, r=20, t=50, b=40),
    font=dict(size=11),
)


def empty_fig(title: str = "", height: int = 300) -> go.Figure:
    fig = go.Figure()
    fig.update_layout(**LAYOUT_DEFAULTS, height=height, title=title)
    return fig


def make_heatmap(mastery: list[float], unlocked_mask: list[int]) -> go.Figure:
    hover = [
        f"<b>{TOPIC_NAMES[i].replace('_', ' ').title()}</b><br>"
        f"{mastery_to_label(mastery[i])}<br>"
        f"Difficulty: {difficulty_to_label(TOPIC_DIFFICULTIES[i])}"
        for i in range(NUM_TOPICS)
    ]
    fig = go.Figure(data=go.Heatmap(
        z=[mastery], x=TOPIC_ABBREV, y=["Mastery"],
        text=[[f"{TOPIC_ABBREV[i]}<br>{round(mastery[i]*100)}%" for i in range(NUM_TOPICS)]],
        texttemplate="%{text}",
        hovertext=[hover], hoverinfo="text",
        colorscale=[
            [0.0, "#d32f2f"], [0.3, "#ff9800"],
            [0.6, "#fdd835"], [0.8, "#4caf50"], [1.0, "#1b5e20"],
        ],
        zmin=0, zmax=1, colorbar=dict(title="Mastery"),
    ))
    for i in range(NUM_TOPICS):
        if unlocked_mask[i] == 0:
            fig.add_shape(
                type="rect", x0=i - 0.5, x1=i + 0.5, y0=-0.5, y1=0.5,
                fillcolor="rgba(158,158,158,0.7)", line=dict(width=0),
            )
    fig.update_layout(**LAYOUT_DEFAULTS, height=180)
    return fig


def make_learning_curves_overview(history: list[list[float]]) -> go.Figure:
    fig = go.Figure()
    if not history:
        fig.update_layout(**LAYOUT_DEFAULTS, height=300, title="Learning Curves — Overview")
        return fig
    for group_name, topic_ids in TOPIC_GROUPS.items():
        steps = list(range(len(history)))
        means = [np.mean([history[s][t] for t in topic_ids]) for s in steps]
        fig.add_trace(go.Scatter(
            x=steps, y=means, mode="lines", name=group_name.title(),
            line=dict(color=GROUP_COLORS[group_name], width=2),
        ))
    fig.update_layout(
        **LAYOUT_DEFAULTS, height=300,
        title="Learning Curves — All Groups",
        xaxis_title="Step", yaxis_title="Mean Mastery",
        yaxis=dict(range=[0, 1]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def make_learning_curves_group(history: list[list[float]], group_name: str,
                                topic_ids: list[int]) -> go.Figure:
    """Per-topic learning curves within a single group."""
    fig = go.Figure()
    if not history:
        fig.update_layout(**LAYOUT_DEFAULTS, height=280,
                          title=f"{group_name.title()} — Per-Topic Progress")
        return fig

    colors = ["#1565c0", "#e65100", "#2e7d32", "#6a1b9a", "#c62828",
              "#00838f", "#4e342e", "#37474f"]
    steps = list(range(len(history)))
    for idx, tid in enumerate(topic_ids):
        name = TOPIC_NAMES[tid].replace("_", " ").title()
        vals = [history[s][tid] for s in steps]
        fig.add_trace(go.Scatter(
            x=steps, y=vals, mode="lines", name=name,
            line=dict(color=colors[idx % len(colors)], width=2),
        ))
    # Add mastery threshold line
    fig.add_hline(y=0.8, line_dash="dash", line_color="gray",
                  annotation_text="Mastery threshold", annotation_position="top right")
    fig.update_layout(
        **LAYOUT_DEFAULTS, height=280,
        title=f"{group_name.title()} — Per-Topic Progress",
        xaxis_title="Step", yaxis_title="Mastery",
        yaxis=dict(range=[0, 1]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def make_reward_decomposition(episode_rewards: list[dict]) -> go.Figure:
    fig = go.Figure()
    if not episode_rewards:
        fig.update_layout(**LAYOUT_DEFAULTS, height=300, title="Reward Breakdown")
        return fig
    last_n = episode_rewards[-10:]
    components = [
        ("milestone_bonus", "#4caf50", "Milestone Bonus"),
        ("learning_gain", "#2196f3", "Learning Gain"),
        ("stretch_reward", "#ff9800", "Stretch Reward"),
        ("assessment_reward", "#9c27b0", "Assessment"),
        ("dropout_penalty", "#f44336", "Dropout Penalty"),
        ("opportunity_cost", "#ff5722", "Opportunity Cost"),
        ("retention_penalty", "#d32f2f", "Retention Penalty"),
        ("completion_bonus", "#1b5e20", "Completion Bonus"),
    ]
    episodes = list(range(1, len(last_n) + 1))
    for key, color, label in components:
        vals = [ep.get(key, 0) for ep in last_n]
        if any(v != 0 for v in vals):
            fig.add_trace(go.Bar(x=episodes, y=vals, name=label, marker_color=color))
    fig.update_layout(
        **LAYOUT_DEFAULTS, height=300, barmode="relative",
        title="Reward Breakdown (Last 10 Episodes)",
        xaxis_title="Episode", yaxis_title="Reward Points",
    )
    return fig


def make_mastery_radar(group_mastery: dict[str, float]) -> go.Figure:
    """Radar chart of mastery per topic group."""
    categories = [g.title() for g in group_mastery.keys()]
    values = list(group_mastery.values())
    # Close the radar
    categories.append(categories[0])
    values.append(values[0])
    fig = go.Figure(data=go.Scatterpolar(
        r=[v * 100 for v in values],
        theta=categories,
        fill="toself",
        fillcolor="rgba(33, 150, 243, 0.2)",
        line=dict(color="#2196f3", width=2),
        text=[f"{v:.0%}" for v in values],
        hoverinfo="text+theta",
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], ticksuffix="%"),
        ),
        title="Mastery by Subject Area",
        height=350,
        margin=dict(l=60, r=60, t=60, b=40),
        font=dict(size=11),
    )
    return fig


def make_strengths_chart(mastery: list[float]) -> go.Figure:
    """Horizontal bar chart sorted by mastery."""
    topics_with_progress = [
        (TOPIC_NAMES[i].replace("_", " ").title(), mastery[i])
        for i in range(NUM_TOPICS) if mastery[i] > 0.01
    ]
    if not topics_with_progress:
        return empty_fig("No topics started yet", 300)

    topics_with_progress.sort(key=lambda x: x[1], reverse=True)
    names = [t[0] for t in topics_with_progress]
    vals = [t[1] for t in topics_with_progress]
    colors = [
        "#1b5e20" if v >= 0.8 else "#4caf50" if v >= 0.7 else
        "#fdd835" if v >= 0.5 else "#ff9800" if v >= 0.3 else "#d32f2f"
        for v in vals
    ]
    fig = go.Figure(data=go.Bar(
        x=[v * 100 for v in vals], y=names,
        orientation="h", marker_color=colors,
        text=[mastery_to_label(v) for v in vals],
        textposition="auto",
    ))
    fig.add_vline(x=80, line_dash="dash", line_color="gray",
                  annotation_text="Mastery", annotation_position="top")
    fig.update_layout(
        **LAYOUT_DEFAULTS, height=max(250, len(names) * 35),
        title="Topic Progress — All Active Topics",
        xaxis=dict(title="Mastery %", range=[0, 100]),
        yaxis=dict(autorange="reversed"),
    )
    return fig


def make_episode_comparison(episode_log: list[list]) -> go.Figure:
    """Compare episodes by archetype."""
    if not episode_log or len(episode_log) < 2:
        return empty_fig("Run multiple episodes to see comparisons", 300)

    archetypes = {}
    for ep in episode_log:
        arch = ep[1]
        reward = float(ep[5])
        mastered = int(ep[3])
        if arch not in archetypes:
            archetypes[arch] = {"rewards": [], "mastered": []}
        archetypes[arch]["rewards"].append(reward)
        archetypes[arch]["mastered"].append(mastered)

    names = list(archetypes.keys())
    avg_rewards = [np.mean(archetypes[a]["rewards"]) for a in names]
    avg_mastered = [np.mean(archetypes[a]["mastered"]) for a in names]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Avg Reward", x=[n.title() for n in names], y=avg_rewards,
        marker_color="#2196f3", yaxis="y",
    ))
    fig.add_trace(go.Bar(
        name="Avg Topics Mastered", x=[n.title() for n in names], y=avg_mastered,
        marker_color="#4caf50", yaxis="y2",
    ))
    fig.update_layout(
        **LAYOUT_DEFAULTS, height=300,
        title="Archetype Comparison",
        yaxis=dict(title="Avg Reward", side="left"),
        yaxis2=dict(title="Avg Mastered", side="right", overlaying="y"),
        barmode="group",
    )
    return fig
