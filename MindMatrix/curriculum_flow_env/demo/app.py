"""Gradio dashboard for CurriculumFlowENV."""

import time
import random

import gradio as gr
import numpy as np
import plotly.graph_objects as go

from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.simulation.curriculum import (
    TOPIC_NAMES, TOPIC_GROUPS, NUM_TOPICS, TOPIC_DIFFICULTIES,
)
from curriculum_flow_env.agents import (
    TopicSequencerAgent, DifficultyAdaptAgent, AssessmentTimingAgent,
)


TOPIC_ABBREV = [
    "CNT", "ADD", "SUB", "MUL", "DIV", "FRC", "DEC", "PCT", "INT", "ALG",
    "LIN", "INQ", "FUN", "POL", "GEO", "A&P", "TRG", "STA", "PRB", "CAL",
]


def make_heatmap(mastery, unlocked_mask):
    """Create topic mastery heatmap."""
    colors = []
    for i in range(NUM_TOPICS):
        if unlocked_mask[i] == 0:
            colors.append(None)  # will show as gray
        else:
            colors.append(mastery[i])

    z = [mastery]
    text = [[f"{TOPIC_ABBREV[i]}<br>{mastery[i]:.2f}" for i in range(NUM_TOPICS)]]

    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=TOPIC_ABBREV,
        y=["Mastery"],
        text=text,
        texttemplate="%{text}",
        colorscale=[
            [0.0, "#d32f2f"], [0.4, "#ff9800"],
            [0.7, "#fdd835"], [0.8, "#4caf50"], [1.0, "#1b5e20"],
        ],
        zmin=0, zmax=1,
        colorbar=dict(title="Mastery"),
    ))

    # Gray out locked topics
    for i in range(NUM_TOPICS):
        if unlocked_mask[i] == 0:
            fig.add_shape(
                type="rect",
                x0=i - 0.5, x1=i + 0.5, y0=-0.5, y1=0.5,
                fillcolor="rgba(158,158,158,0.7)", line=dict(width=0),
            )

    fig.update_layout(
        template="simple_white", height=150, margin=dict(l=60, r=20, t=20, b=40),
    )
    return fig


def make_learning_curves(history):
    """Create learning curves per topic group."""
    if not history:
        fig = go.Figure()
        fig.update_layout(template="simple_white", height=350, title="Learning Curves")
        return fig

    fig = go.Figure()
    colors = {"arithmetic": "#2196f3", "algebra": "#ff9800", "geometry": "#4caf50",
              "statistics": "#9c27b0", "calculus": "#f44336"}

    for group_name, topic_ids in TOPIC_GROUPS.items():
        steps = list(range(len(history)))
        means = [
            np.mean([history[s][t] for t in topic_ids])
            for s in steps
        ]
        fig.add_trace(go.Scatter(
            x=steps, y=means, mode="lines", name=group_name,
            line=dict(color=colors[group_name], width=2),
        ))

    fig.update_layout(
        template="simple_white", height=350,
        xaxis_title="Step", yaxis_title="Mean Mastery",
        yaxis=dict(range=[0, 1]), title="Learning Curves by Topic Group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def make_reward_decomposition(episode_rewards):
    """Create stacked bar chart of reward components."""
    if not episode_rewards:
        fig = go.Figure()
        fig.update_layout(template="simple_white", height=350, title="Reward Decomposition")
        return fig

    last_n = episode_rewards[-10:]
    components = ["milestone_bonus", "learning_gain", "stretch_reward",
                  "assessment_reward", "dropout_penalty", "opportunity_cost",
                  "retention_penalty", "completion_bonus"]
    colors_map = {
        "milestone_bonus": "#4caf50", "learning_gain": "#2196f3",
        "stretch_reward": "#ff9800", "assessment_reward": "#9c27b0",
        "dropout_penalty": "#f44336", "opportunity_cost": "#ff5722",
        "retention_penalty": "#d32f2f", "completion_bonus": "#1b5e20",
    }

    fig = go.Figure()
    episodes = list(range(len(last_n)))

    for comp in components:
        vals = [ep.get(comp, 0) for ep in last_n]
        if any(v != 0 for v in vals):
            fig.add_trace(go.Bar(
                x=episodes, y=vals, name=comp.replace("_", " ").title(),
                marker_color=colors_map[comp],
            ))

    fig.update_layout(
        template="simple_white", height=350, barmode="relative",
        title="Reward Decomposition (Last 10 Episodes)",
        xaxis_title="Episode", yaxis_title="Reward",
    )
    return fig


def run_env_step(env, sequencer, diff_agent, assess_agent, obs):
    """Run one step using heuristic agents."""
    obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}
    info_dict = {"unlocked_mask": obs_dict["unlocked_mask"]}

    topic = sequencer.select_action(obs_dict, info_dict)
    difficulty = diff_agent.select_action(obs_dict, info_dict) - 1  # map 1-5 to 0-4 for action space
    assess = assess_agent.select_action(obs_dict, info_dict)

    action = {"topic": topic, "difficulty": difficulty, "assess": assess}
    obs, reward, terminated, truncated, info = env.step(action)

    sequencer.update(obs_dict, reward, terminated or truncated)
    diff_agent.update(obs_dict, reward, terminated or truncated)
    assess_agent.update(obs_dict, reward, terminated or truncated)

    return obs, reward, terminated, truncated, info


def create_demo():
    with gr.Blocks(title="CurriculumFlowENV", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# CurriculumFlowENV\n**Multi-Agent RL for Adaptive Learning Path Optimization**")

        # State
        state = gr.State({
            "env": None, "obs": None, "sequencer": None, "diff_agent": None,
            "assess_agent": None, "mastery_history": [], "decisions": [],
            "episode_log": [], "episode_rewards_agg": [], "episode_count": 0,
        })

        # ROW 1 - Controls
        with gr.Row():
            archetype_radio = gr.Radio(
                ["fast", "steady", "struggling", "bursty", "anxious"],
                value="steady", label="Student Archetype",
            )
            max_steps_slider = gr.Slider(50, 500, value=200, step=10, label="Max Steps")
            reset_btn = gr.Button("Reset & Start", variant="primary")
            step_btn = gr.Button("Step Once")
            run_btn = gr.Button("Run Full Episode", variant="secondary")
            batch_btn = gr.Button("Run 10 Episodes")

        # ROW 2 - Metrics
        with gr.Row():
            step_display = gr.Textbox(label="Step", value="0 / 200", interactive=False)
            mastered_display = gr.Textbox(label="Topics Mastered", value="0 / 20", interactive=False)
            completion_display = gr.Textbox(label="Completion %", value="0.0%", interactive=False)
            reward_display = gr.Textbox(label="Episode Reward", value="0.0", interactive=False)

        # ROW 3 - Main viz
        with gr.Row():
            with gr.Column(scale=2):
                heatmap_plot = gr.Plot(label="Topic Mastery Heatmap")
            with gr.Column(scale=1):
                engagement_slider = gr.Slider(0, 1, value=0.8, label="Engagement", interactive=False)
                student_info = gr.Textbox(label="Student State", lines=3, interactive=False)
                decisions_df = gr.Dataframe(
                    headers=["step", "topic", "difficulty", "assessed", "reward"],
                    label="Last 5 Decisions", row_count=5,
                )

        # ROW 4 - Learning curves
        with gr.Row():
            learning_plot = gr.Plot(label="Learning Curves")

        # ROW 5 - Reward decomposition
        with gr.Row():
            reward_plot = gr.Plot(label="Reward Decomposition")

        # ROW 6 - Episode log
        with gr.Row():
            episode_df = gr.Dataframe(
                headers=["episode", "archetype", "steps", "topics_mastered", "completion_%", "total_reward"],
                label="Episode Log", row_count=10,
            )

        def reset_env(archetype, max_steps, st):
            env = CurriculumFlowEnv(archetype=archetype, max_steps=max_steps)
            obs, info = env.reset()
            seq = TopicSequencerAgent()
            diff = DifficultyAdaptAgent()
            assess = AssessmentTimingAgent()
            seq.reset()
            diff.reset()
            assess.reset()

            mastery = obs["mastery"].tolist()
            mask = obs["unlocked_mask"].tolist()

            st = {
                "env": env, "obs": obs, "sequencer": seq, "diff_agent": diff,
                "assess_agent": assess, "mastery_history": [mastery],
                "decisions": [], "episode_log": st.get("episode_log", []),
                "episode_rewards_agg": st.get("episode_rewards_agg", []),
                "episode_count": st.get("episode_count", 0),
            }

            hm = make_heatmap(mastery, mask)
            lc = make_learning_curves(st["mastery_history"])
            recent_acc = sum(obs["recent_accuracy"].tolist()) / 10
            info_text = f"Archetype: {archetype}\nTopic: {TOPIC_NAMES[0]}\nAccuracy: {recent_acc:.0%}"

            return (
                st,
                "0 / " + str(max_steps),
                "0 / 20",
                "0.0%",
                "0.0",
                hm,
                0.8,
                info_text,
                [],
                lc,
                make_reward_decomposition(st["episode_rewards_agg"]),
                st["episode_log"],
            )

        def do_step(st):
            if st["env"] is None:
                return st, "0/200", "0/20", "0%", "0", None, 0.8, "", [], None, None, st.get("episode_log", [])

            env = st["env"]
            obs, reward, terminated, truncated, info = run_env_step(
                env, st["sequencer"], st["diff_agent"], st["assess_agent"], st["obs"],
            )
            st["obs"] = obs
            mastery = obs["mastery"].tolist()
            mask = obs["unlocked_mask"].tolist()
            st["mastery_history"].append(mastery)

            decision = [
                info["step"],
                info.get("topic_name", ""),
                info.get("difficulty", 0),
                "Yes" if info.get("assessed", False) else "No",
                f"{reward:.1f}",
            ]
            st["decisions"].append(decision)

            done = terminated or truncated
            if done:
                st["episode_count"] += 1
                ep_entry = [
                    st["episode_count"],
                    info["student_archetype"],
                    info["step"],
                    info["topics_mastered"],
                    f"{info['completion_rate']:.1%}",
                    f"{info['episode_reward']:.1f}",
                ]
                st["episode_log"] = (st.get("episode_log", []) + [ep_entry])[-50:]

                # Aggregate reward components
                total_comps = {}
                for comp_log in env.reward_components_log:
                    for k, v in comp_log.items():
                        total_comps[k] = total_comps.get(k, 0) + v
                st["episode_rewards_agg"] = (st.get("episode_rewards_agg", []) + [total_comps])[-10:]

            hm = make_heatmap(mastery, mask)
            lc = make_learning_curves(st["mastery_history"])
            rd = make_reward_decomposition(st.get("episode_rewards_agg", []))

            recent = obs["recent_accuracy"].tolist()
            recent_acc = sum(recent) / max(len([r for r in recent if r > 0]), 1) if any(r > 0 for r in recent) else 0
            info_text = f"Archetype: {info['student_archetype']}\nTopic: {info.get('topic_name','')}\nAccuracy: {recent_acc:.0%}"

            return (
                st,
                f"{info['step']} / {env.max_steps}",
                f"{info['topics_mastered']} / 20",
                f"{info['completion_rate']:.1%}",
                f"{info['episode_reward']:.1f}",
                hm,
                obs["engagement"][0],
                info_text,
                st["decisions"][-5:],
                lc,
                rd,
                st.get("episode_log", []),
            )

        def run_full(archetype, max_steps, st):
            # Reset first
            result = reset_env(archetype, max_steps, st)
            st = result[0]

            while True:
                result = do_step(st)
                st = result[0]
                env = st["env"]
                if env.step_count >= env.max_steps or st["obs"] is None:
                    break
                comp_rate = env.topic_graph.completion_rate(env.student.mastery)
                if comp_rate >= 0.95:
                    break

            return result

        def run_batch(archetype, max_steps, st):
            for _ in range(10):
                result = run_full(archetype, max_steps, st)
                st = result[0]
            return result

        outputs = [
            state, step_display, mastered_display, completion_display,
            reward_display, heatmap_plot, engagement_slider, student_info,
            decisions_df, learning_plot, reward_plot, episode_df,
        ]

        reset_btn.click(reset_env, [archetype_radio, max_steps_slider, state], outputs)
        step_btn.click(do_step, [state], outputs)
        run_btn.click(run_full, [archetype_radio, max_steps_slider, state], outputs)
        batch_btn.click(run_batch, [archetype_radio, max_steps_slider, state], outputs)

    return demo


demo = create_demo()

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
