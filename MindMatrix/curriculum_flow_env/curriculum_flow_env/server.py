"""FastAPI server — routes, auth, templates, and OpenENV API."""

import json
import logging
import asyncio
from pathlib import Path

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from curriculum_flow_env.database import (
    init_db, get_user_by_email, create_user, verify_password, update_user,
    get_user_progress, update_topic_mastery, record_quiz_attempt,
    get_quiz_history, get_growth_data,
    record_chapter_pass, get_chapter_passes, is_main_quiz_unlocked,
    get_all_unlocked_main_quizzes,
)
from curriculum_flow_env.auth import (
    create_session, get_current_user, login_user, logout_user,
)
from curriculum_flow_env.simulation.curriculum import (
    TOPIC_NAMES, TOPIC_DISPLAY_NAMES, TOPIC_DIFFICULTIES, TOPIC_GROUPS,
    GROUP_DISPLAY_NAMES, GROUP_COLORS, NUM_TOPICS, MASTERY_THRESHOLD,
    UNLOCK_THRESHOLD, PREREQUISITE_EDGES,
)
from curriculum_flow_env.env import CurriculumFlowEnv
from curriculum_flow_env.ui.formatting import (
    mastery_to_label, engagement_to_label, obs_to_json,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s")
logger = logging.getLogger(__name__)

# Initialize database
init_db()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="CurriculumFlowENV", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=str(STATIC_DIR), html=False), name="static")

# Disable caching for static files during development
from starlette.middleware.base import BaseHTTPMiddleware
class NoCacheStaticMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if request.url.path.startswith("/static/"):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
        return response
app.add_middleware(NoCacheStaticMiddleware)
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# OpenENV instance
env = CurriculumFlowEnv()
env_lock = asyncio.Lock()


# ━━━ HELPERS ━━━

def _get_topic_graph_data():
    """Build prerequisite lookup."""
    from curriculum_flow_env.simulation.topic_graph import TopicGraph
    return TopicGraph()


def _sync_mastery_from_chapters(user_id: int):
    """Recalculate mastery for all topics based on chapter passes and quiz history.
    Each chapter pass = 15% mastery (max 75% from chapters).
    Main quiz pass (>=80%) adds up to 25% more.
    Ensures mastery is never lower than what chapter data implies."""
    all_ch = get_chapter_passes(user_id)
    quiz_hist = get_quiz_history(user_id)
    progress = get_user_progress(user_id)
    current_mastery = {}
    for p in progress:
        tid = p["topic_id"]
        current_mastery[tid] = p["mastery_level"]

    # Build chapter counts per topic
    topic_ch_counts = {}
    for ch in all_ch:
        tid = ch["topic_id"]
        if ch["score"] >= 0.8:
            if tid not in topic_ch_counts:
                topic_ch_counts[tid] = set()
            topic_ch_counts[tid].add(ch["chapter_num"])

    # Build best main quiz score per topic
    main_quiz_best = {}
    for q in quiz_hist:
        tid = q["topic_id"]
        tid = int(tid) if isinstance(tid, str) else tid
        score = q["score"]
        if score >= 0.8:
            if tid not in main_quiz_best or score > main_quiz_best[tid]:
                main_quiz_best[tid] = score

    # Recalculate and update where needed
    for tid, chs in topic_ch_counts.items():
        ch_mastery = len(chs) * 0.15  # 0 to 0.75
        main_score = main_quiz_best.get(tid, 0)
        main_bonus = main_score * 0.25 if main_score >= 0.8 else 0
        calculated = min(1.0, ch_mastery + main_bonus)
        current = current_mastery.get(tid, 0.0)
        if calculated > current:
            update_topic_mastery(user_id, tid, calculated)


def _build_category_progress(user_id: int, progress: dict = None):
    """Build category progress data for templates."""
    if progress is None:
        progress = get_user_progress(user_id)

    mastery_dict = {}
    for row in progress:
        tid = row["topic_id"]
        tid = int(tid) if isinstance(tid, str) else tid
        mastery_dict[tid] = row["mastery_level"]

    tg = _get_topic_graph_data()
    unlocked = tg.get_unlocked_topics(mastery_dict)

    categories = {}
    for group_name, topic_ids in TOPIC_GROUPS.items():
        topics = []
        mastered_count = 0
        for tid in topic_ids:
            m = mastery_dict.get(tid, 0.0)
            is_mastered = m >= MASTERY_THRESHOLD
            if is_mastered:
                mastered_count += 1
            is_locked = tid not in unlocked

            prereqs = tg.get_prerequisites(tid)
            prereq_names = ", ".join(TOPIC_DISPLAY_NAMES[p] for p in prereqs if mastery_dict.get(p, 0) < UNLOCK_THRESHOLD)

            topics.append({
                "id": tid,
                "display_name": TOPIC_DISPLAY_NAMES[tid],
                "mastery": m,
                "mastery_label": mastery_to_label(m),
                "mastered": is_mastered,
                "locked": is_locked,
                "difficulty": TOPIC_DIFFICULTIES[tid],
                "prereq_names": prereq_names or "None",
            })

        total = len(topic_ids)
        categories[group_name] = {
            "display_name": GROUP_DISPLAY_NAMES[group_name],
            "color": GROUP_COLORS[group_name],
            "topics": topics,
            "mastered": mastered_count,
            "total": total,
            "pct": round(mastered_count / total * 100) if total > 0 else 0,
        }
    return categories


def render(request: Request, name: str, ctx: dict = None):
    """Helper to render a Jinja2 template compatible with Starlette 1.0."""
    return templates.TemplateResponse(request, name, context=ctx or {})


# ━━━ PUBLIC ROUTES (no auth) ━━━

@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    user = get_current_user(request)
    if user:
        return RedirectResponse("/home", status_code=302)
    return render(request, "landing.html")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    user = get_current_user(request)
    if user:
        return RedirectResponse("/home", status_code=302)
    return render(request, "login.html", {"error": None})


@app.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, email: str = Form(...), password: str = Form(...)):
    user = verify_password(email, password)
    if not user:
        return render(request, "login.html", {"error": "Invalid email or password"})
    response = RedirectResponse("/home", status_code=302)
    login_user(response, user["id"])
    return response


@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return render(request, "signup.html", {"error": None})


@app.post("/signup", response_class=HTMLResponse)
async def signup_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    role: str = Form(""),
    experience_level: str = Form(""),
    organization: str = Form(""),
    bio: str = Form(""),
):
    if password != confirm_password:
        return render(request, "signup.html", {"error": "Passwords don't match"})
    if len(password) < 6:
        return render(request, "signup.html", {"error": "Password must be at least 6 characters"})
    existing = get_user_by_email(email)
    if existing:
        return render(request, "signup.html", {"error": "Email already registered"})

    new_user = create_user(email, password, name, role, experience_level, organization, bio)
    response = RedirectResponse("/home", status_code=302)
    login_user(response, new_user["id"])
    return response


@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse("/", status_code=302)
    logout_user(response, request)
    return response


# ━━━ AUTH-REQUIRED ROUTES ━━━

def _require_auth(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=302, headers={"Location": "/login"})
    return user


@app.get("/home", response_class=HTMLResponse)
async def home_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    progress = get_user_progress(user["id"])
    recent_topics = []
    for row in sorted(progress, key=lambda r: r.get("last_practiced", ""), reverse=True):
        if row["mastery_level"] > 0 and row["mastery_level"] < MASTERY_THRESHOLD and len(recent_topics) < 4:
            tid = int(row["topic_id"]) if isinstance(row["topic_id"], str) else row["topic_id"]
            group_name = ""
            group_color = "#1E54B7"
            for gn, tids in TOPIC_GROUPS.items():
                if tid in tids:
                    group_name = GROUP_DISPLAY_NAMES[gn]
                    group_color = GROUP_COLORS[gn]
                    break
            recent_topics.append({
                "id": tid,
                "display_name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}"),
                "mastery": row["mastery_level"],
                "group": group_name,
                "color": group_color,
            })

    return render(request, "home.html", {
        "user": user, "active_page": "home",
        "recent_topics": recent_topics,
    })


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    progress = get_user_progress(user["id"])
    categories = _build_category_progress(user["id"], progress)

    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}
    topics_mastered = sum(1 for v in mastery_dict.values() if v >= MASTERY_THRESHOLD)

    quiz_hist = get_quiz_history(user["id"])
    quizzes_taken = len(quiz_hist)
    avg_quiz = round(sum(q["score"] for q in quiz_hist) / max(len(quiz_hist), 1) * 100)
    completion_pct = round(topics_mastered / NUM_TOPICS * 100)

    return render(request, "dashboard.html", {
        "user": user, "active_page": "dashboard",
        "topics_mastered": topics_mastered,
        "quizzes_taken": quizzes_taken,
        "avg_quiz_score": avg_quiz,
        "completion_pct": completion_pct,
        "category_progress": categories,
        "engagement_label": engagement_to_label(0.8),
        "archetype": "steady",
        "current_topic": "Numbers",
        "recent_sessions": [],
    })


@app.get("/learning", response_class=HTMLResponse)
async def learning_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    categories = _build_category_progress(user["id"])
    return render(request, "learning.html", {
        "user": user, "active_page": "learning",
        "categories": categories,
    })


@app.get("/learning/study", response_class=HTMLResponse)
async def study_topic(request: Request, topic: int = 0, practice: int = 0):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    topic = min(max(topic, 0), NUM_TOPICS - 1)

    # Get user mastery data
    progress = get_user_progress(user["id"])
    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}
    current_mastery = mastery_dict.get(topic, 0.0)

    # Build observation for agents
    tg = _get_topic_graph_data()
    unlocked = tg.get_unlocked_topics(mastery_dict)
    mastery_list = [mastery_dict.get(i, 0.0) for i in range(NUM_TOPICS)]
    mask = [1 if i in unlocked else 0 for i in range(NUM_TOPICS)]
    obs = {
        "mastery": mastery_list,
        "engagement": [0.8],
        "recent_accuracy": [0.5] * 10,
        "time_since_review": [20] * NUM_TOPICS,
        "current_topic": topic,
        "unlocked_mask": mask,
    }

    # Ask Difficulty Adapter agent for optimal difficulty
    difficulty = env.difficulty_agent.select_action(obs, {"unlocked_mask": mask})

    # If practice=1, run OpenENV simulation and update mastery, then redirect back
    if practice:
        async with env_lock:
            env.reset(options={"archetype": "steady"})
            rewards = []
            for _ in range(5):
                _, reward, _, _, info = env.step({
                    "topic": topic, "difficulty": max(0, difficulty - 1), "assess": 0,
                })
                rewards.append(reward)
            mastery_gain = env.student.mastery.get(topic, 0.0)

        new_mastery = min(1.0, current_mastery + mastery_gain * 0.3)
        update_topic_mastery(user["id"], topic, new_mastery)
        logger.info(
            f"OpenENV practice: user={user['id']} topic={topic} difficulty={difficulty} "
            f"mastery {current_mastery:.2f}->{new_mastery:.2f} reward={sum(rewards):.1f}"
        )
        return RedirectResponse(f"/learning/study?topic={topic}", status_code=302)

    # Load study content
    from curriculum_flow_env.study_content import STUDY_CONTENT
    content = STUDY_CONTENT.get(topic, {})

    # Find group name for this topic
    group_name = ""
    for gn, tids in TOPIC_GROUPS.items():
        if topic in tids:
            group_name = GROUP_DISPLAY_NAMES[gn]
            break

    topic_data = {
        "title": TOPIC_DISPLAY_NAMES.get(topic, "Topic"),
        "overview": content.get("overview", "Study materials for this topic."),
        "chapters": content.get("chapters", []),
        "key_concepts": content.get("key_concepts", []),
        "formulas": content.get("formulas", []),
        "solved_examples": content.get("solved_examples", []),
        "tips": content.get("tips", []),
        "difficulty": TOPIC_DIFFICULTIES.get(topic, 1),
        "group": group_name,
    }

    # Build sidebar topics for the same category
    sidebar_topics = []
    for gn, tids in TOPIC_GROUPS.items():
        if topic in tids:
            for tid in tids:
                sidebar_topics.append({
                    "id": tid,
                    "display_name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}"),
                    "mastery": round(mastery_dict.get(tid, 0.0) * 100),
                    "is_current": tid == topic,
                })
            break

    # Get chapter pass status for this topic
    ch_passes = get_chapter_passes(user["id"], topic)
    passed_chapters = {p["chapter_num"]: round(p["score"] * 100) for p in ch_passes if p["score"] >= 0.8}
    main_unlocked = len(passed_chapters) >= 5

    return render(request, "study.html", {
        "user": user, "active_page": "learning",
        "topic": topic_data,
        "topic_id": topic,
        "mastery_pct": round(current_mastery * 100),
        "agent_difficulty": difficulty,
        "sidebar_topics": sidebar_topics,
        "passed_chapters": passed_chapters,
        "main_quiz_unlocked": main_unlocked,
    })


@app.get("/learning/{category_slug}", response_class=HTMLResponse)
async def learning_category_page(request: Request, category_slug: str):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    # Validate slug
    if category_slug not in TOPIC_GROUPS:
        return RedirectResponse("/learning", status_code=302)

    categories = _build_category_progress(user["id"])
    cat_data = categories[category_slug]

    return render(request, "learning_category.html", {
        "user": user, "active_page": "learning",
        "category_slug": category_slug,
        "category": cat_data,
        "all_categories": categories,
    })


@app.get("/quiz", response_class=HTMLResponse)
async def quiz_select_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    try:
        from curriculum_flow_env.quiz import get_available_topics
        available = get_available_topics()
    except ImportError:
        available = [{"id": i, "display_name": TOPIC_DISPLAY_NAMES[i], "group": "", "question_count": 5, "best_score": None} for i in range(NUM_TOPICS)]

    # Add group names and best scores
    quiz_hist = get_quiz_history(user["id"])
    best_scores = {}
    for q in quiz_hist:
        tid = q["topic_id"]
        score = round(q["score"] * 100)
        if tid not in best_scores or score > best_scores[tid]:
            best_scores[tid] = score

    unlocked_mains = get_all_unlocked_main_quizzes(user["id"])

    for t in available:
        for gn, tids in TOPIC_GROUPS.items():
            if t["id"] in tids:
                t["group"] = GROUP_DISPLAY_NAMES[gn]
                t["group_color"] = GROUP_COLORS[gn]
                break
        t["display_name"] = TOPIC_DISPLAY_NAMES.get(t["id"], t.get("name", ""))
        t["best_score"] = best_scores.get(t["id"])
        t["unlocked"] = t["id"] in unlocked_mains

    return render(request, "quiz.html", {
        "user": user, "active_page": "quiz",
        "mode": "select", "available_topics": available,
    })


@app.get("/quiz/start", response_class=HTMLResponse)
async def quiz_start(request: Request, topic: int = 0, count: int = 5, chapter: int = 0):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    try:
        from curriculum_flow_env.quiz import generate_quiz
        questions = generate_quiz(topic, count)
    except (ImportError, Exception):
        # Fallback: generate simple questions
        questions = [
            {"question": f"Sample question {i+1} for {TOPIC_DISPLAY_NAMES.get(topic, 'topic')}",
             "options": ["Option A", "Option B", "Option C", "Option D"],
             "correct": 0, "explanation": "This is a sample question."}
            for i in range(count)
        ]

    # Add index to each question
    for i, q in enumerate(questions):
        q["idx"] = i

    question_data_json = json.dumps([{
        "question": q["question"], "options": q["options"],
        "correct": q["correct"], "explanation": q["explanation"]
    } for q in questions])

    quiz_label = TOPIC_DISPLAY_NAMES.get(topic, "Topic")
    if chapter > 0:
        quiz_label += f" — Chapter {chapter}"

    return render(request, "quiz.html", {
        "user": user, "active_page": "quiz",
        "mode": "active",
        "topic_id": topic,
        "topic_name": quiz_label,
        "chapter": chapter,
        "questions": questions,
        "question_data_json": question_data_json,
        "pass_rate": 80,
    })


@app.post("/quiz/submit", response_class=HTMLResponse)
async def quiz_submit(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    form = await request.form()
    topic_id = int(form.get("topic_id", 0))
    chapter_num = int(form.get("chapter", 0))
    question_data = json.loads(form.get("question_data", "[]"))

    # Collect answers
    answers = []
    for i in range(len(question_data)):
        ans = form.get(f"answer_{i}")
        answers.append(int(ans) if ans is not None else -1)

    # Grade
    correct_count = 0
    results = []
    for i, q in enumerate(question_data):
        user_ans = answers[i] if i < len(answers) else -1
        is_correct = user_ans == q["correct"]
        if is_correct:
            correct_count += 1
        results.append({
            "question": q["question"],
            "your_answer": q["options"][user_ans] if 0 <= user_ans < 4 else "No answer",
            "correct_answer": q["options"][q["correct"]],
            "is_correct": is_correct,
            "explanation": q.get("explanation", ""),
        })

    total = len(question_data)
    score = correct_count / max(total, 1)
    score_pct = round(score * 100)

    # Record in database (with per-question results for review)
    record_quiz_attempt(user["id"], topic_id, score, total, correct_count, json.dumps(results))

    # Use OpenENV Assessment pipeline: run assessment in env and get reward signal
    assessment_reward = 0.0
    env_feedback = ""
    async with env_lock:
        env.reset(options={"archetype": "steady"})
        # Run assessment in OpenENV
        _, reward, _, _, env_info = env.step({
            "topic": min(topic_id, NUM_TOPICS - 1), "difficulty": 2, "assess": 1,
        })
        assessment_reward = reward
        components = env_info.get("reward_components", {})
        if components.get("assessment_reward", 0) > 0:
            env_feedback = "Validated mastery — the Assessment Timer confirms strong understanding."
        elif components.get("assessment_reward", 0) < 0:
            env_feedback = "The Assessment Timer suggests more practice before retesting this topic."
        else:
            env_feedback = "Good attempt — the Difficulty Adapter will adjust future problems."

    # Update mastery based on quiz type and score
    progress = get_user_progress(user["id"])
    current = 0.0
    for p in progress:
        if p["topic_id"] == topic_id:
            current = p["mastery_level"]
            break
    passed = score_pct >= 80

    # Record chapter pass first (needed for mastery calculation)
    if chapter_num > 0 and passed:
        record_chapter_pass(user["id"], topic_id, chapter_num, score)

    # Calculate mastery based on progress:
    # Each chapter quiz passed = 15% mastery (5 chapters = 75%)
    # Main quiz passed = remaining 25% (total = 100%)
    ch_passes = get_chapter_passes(user["id"], topic_id)
    chapters_passed = len({p["chapter_num"] for p in ch_passes if p["score"] >= 0.8})
    chapter_mastery = chapters_passed * 0.15  # 0 to 0.75

    if chapter_num == 0 and passed:
        # Main quiz pass: set mastery to chapter_mastery + score * 0.25
        new_mastery = min(1.0, chapter_mastery + score * 0.25)
    elif chapter_num > 0 and passed:
        # Chapter quiz pass: recalculate from chapters
        new_mastery = max(current, chapter_mastery)
    else:
        # Failed attempt: tiny boost for effort
        new_mastery = min(1.0, current + score * 0.02)

    update_topic_mastery(user["id"], topic_id, new_mastery)

    logger.info(
        f"OpenENV quiz: user={user['id']} topic={topic_id} ch={chapter_num} score={score_pct}% "
        f"env_reward={assessment_reward:.1f} feedback={env_feedback}"
    )

    # Build AI agent decisions for the decision log
    updated_progress = get_user_progress(user["id"])
    mastery_dict_updated = {r["topic_id"]: r["mastery_level"] for r in updated_progress}
    tg = _get_topic_graph_data()
    unlocked_updated = tg.get_unlocked_topics(mastery_dict_updated)
    mastery_list_updated = [mastery_dict_updated.get(i, 0.0) for i in range(NUM_TOPICS)]
    mask_updated = [1 if i in unlocked_updated else 0 for i in range(NUM_TOPICS)]
    obs_updated = {
        "mastery": mastery_list_updated, "engagement": [0.8],
        "recent_accuracy": [score] * 10,
        "time_since_review": [20] * NUM_TOPICS,
        "current_topic": topic_id, "unlocked_mask": mask_updated,
    }
    info_updated = {"unlocked_mask": mask_updated}
    next_topic = env.sequencer.select_action(obs_updated, info_updated)
    obs_updated["current_topic"] = next_topic
    next_diff = env.difficulty_agent.select_action(obs_updated, info_updated)
    next_assess = env.assessment_agent.select_action(obs_updated, info_updated)

    ai_decisions = {
        "mastery_before": round(current * 100),
        "mastery_after": round(new_mastery * 100),
        "next_topic_name": TOPIC_DISPLAY_NAMES.get(next_topic, "Unknown"),
        "next_topic_id": next_topic,
        "next_difficulty": next_diff,
        "assess_action": "Take a Quiz" if next_assess == 1 else "Keep Practicing",
        "sequencer_reason": f"Lowest mastery among {len(unlocked_updated)} unlocked topics" if mastery_dict_updated.get(next_topic, 0) < 0.3 else f"Building on your progress",
        "difficulty_reason": f"Matched to mastery level ({round(mastery_dict_updated.get(next_topic, 0)*100)}%)" if next_diff <= 3 else f"Challenging you — accuracy is high",
    }

    return render(request, "quiz.html", {
        "user": user, "active_page": "quiz",
        "mode": "results",
        "topic_id": topic_id,
        "chapter": chapter_num,
        "topic_name": TOPIC_DISPLAY_NAMES.get(topic_id, "Topic"),
        "score_pct": score_pct,
        "correct": correct_count,
        "total": total,
        "results": results,
        "env_feedback": env_feedback,
        "env_reward": round(assessment_reward, 1),
        "ai_decisions": ai_decisions,
    })


@app.get("/growth", response_class=HTMLResponse)
async def growth_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    progress = get_user_progress(user["id"])
    categories = _build_category_progress(user["id"], progress)
    quiz_hist = get_quiz_history(user["id"])
    # Build topic attempts summary from quiz history
    topic_attempts_map = {}
    for q in quiz_hist:
        tid_raw = q["topic_id"]
        tid = int(tid_raw) if isinstance(tid_raw, str) else tid_raw
        score_pct = round(q["score"] * 100)
        if tid not in topic_attempts_map:
            topic_attempts_map[tid] = {"topic_name": TOPIC_DISPLAY_NAMES.get(tid, ""), "attempts": 0, "best": 0, "latest": 0, "scores": []}
        topic_attempts_map[tid]["attempts"] += 1
        topic_attempts_map[tid]["latest"] = score_pct
        topic_attempts_map[tid]["scores"].append(score_pct)
        if score_pct > topic_attempts_map[tid]["best"]:
            topic_attempts_map[tid]["best"] = score_pct
    topic_attempts = []
    for tid, ta in topic_attempts_map.items():
        scores = ta["scores"]
        trend = "up" if len(scores) >= 2 and scores[-1] > scores[-2] else ("down" if len(scores) >= 2 and scores[-1] < scores[-2] else "flat")
        topic_attempts.append({**ta, "trend": trend})

    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}
    courses_completed = sum(1 for v in mastery_dict.values() if v >= MASTERY_THRESHOLD)
    total_quizzes = len(quiz_hist)

    # Topics with questions but no quiz taken
    topics_with_quizzes = set(q["topic_id"] for q in quiz_hist)
    quizzes_not_taken = NUM_TOPICS - len(topics_with_quizzes)
    avg_score = round(sum(q["score"] for q in quiz_hist) / max(len(quiz_hist), 1) * 100)

    # Growth data for chart — include group for filtering
    growth_data = []
    for i, q in enumerate(quiz_hist[-30:]):
        tid = int(q["topic_id"]) if isinstance(q["topic_id"], str) else q["topic_id"]
        topic_short = TOPIC_DISPLAY_NAMES.get(tid, "")[:12]
        topic_group = ""
        for gn, tids in TOPIC_GROUPS.items():
            if tid in tids:
                topic_group = gn
                break
        growth_data.append({
            "date": (q.get("attempted_at") or "")[:10],
            "score": round(q["score"] * 100),
            "score_pct": round(q["score"] * 100),
            "label": topic_short or f"Q{i+1}",
            "group": topic_group,
            "group_display": GROUP_DISPLAY_NAMES.get(topic_group, ""),
        })

    # Build category list for the filter dropdown
    category_filter_list = [{"slug": gn, "name": GROUP_DISPLAY_NAMES[gn]} for gn in TOPIC_GROUPS]

    # Category growth — use average mastery per category (not just fully-mastered count)
    category_growth = {}
    for gn, topic_ids in TOPIC_GROUPS.items():
        gdata = categories[gn]
        avg_mastery = 0
        if topic_ids:
            avg_mastery = round(sum(mastery_dict.get(tid, 0.0) for tid in topic_ids) / len(topic_ids) * 100)
        category_growth[gn] = {
            "display_name": gdata["display_name"],
            "color": gdata["color"],
            "current_pct": avg_mastery,
            "delta": avg_mastery,  # simplified: delta = current since starting from 0
        }

    return render(request, "growth.html", {
        "user": user, "active_page": "growth",
        "courses_completed": courses_completed,
        "total_quizzes": total_quizzes,
        "quizzes_not_taken": quizzes_not_taken,
        "avg_score": avg_score,
        "growth_data": growth_data,
        "category_filter_list": category_filter_list,
        "topic_attempts": topic_attempts,
        "category_growth": category_growth,
        "quiz_history": [{
            "date": (q.get("attempted_at") or "")[:10],
            "topic_name": TOPIC_DISPLAY_NAMES.get(
                int(q["topic_id"]) if isinstance(q["topic_id"], str) else q["topic_id"], ""
            ),
            "score": q["score"],
            "correct": q["correct_answers"],
            "total": q["total_questions"],
            "attempt_num": i + 1,
        } for i, q in enumerate(quiz_hist)],
    })


@app.get("/quiz/review", response_class=HTMLResponse)
async def quiz_review_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    quiz_hist = get_quiz_history(user["id"])
    progress = get_user_progress(user["id"])
    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}

    # Group quiz history by topic
    topic_reviews = {}
    for q in quiz_hist:
        tid_raw = q["topic_id"]
        tid = int(tid_raw) if isinstance(tid_raw, str) else tid_raw
        if tid not in topic_reviews:
            group_name = ""
            for gn, tids in TOPIC_GROUPS.items():
                if tid in tids:
                    group_name = GROUP_DISPLAY_NAMES[gn]
                    break
            topic_reviews[tid] = {
                "topic_id": tid,
                "topic_name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}"),
                "group": group_name,
                "mastery": round(mastery_dict.get(tid_raw, mastery_dict.get(tid, 0.0)) * 100),
                "attempts": [],
                "best_score": 0,
                "latest_score": 0,
                "total_attempts": 0,
            }
        score_pct = round(q["score"] * 100)
        results_data = []
        try:
            results_data = json.loads(q.get("results_json", "[]") or "[]")
        except (json.JSONDecodeError, TypeError):
            pass
        topic_reviews[tid]["attempts"].append({
            "date": q.get("attempted_at", q.get("date", "")),
            "score": score_pct,
            "correct": q["correct_answers"],
            "total": q["total_questions"],
            "attempt_id": q.get("id", 0),
            "results": results_data,
        })
        topic_reviews[tid]["total_attempts"] += 1
        if score_pct > topic_reviews[tid]["best_score"]:
            topic_reviews[tid]["best_score"] = score_pct
        topic_reviews[tid]["latest_score"] = score_pct

    # Sort by most recent attempt first
    reviews_list = sorted(topic_reviews.values(), key=lambda r: r["attempts"][0]["date"] if r["attempts"] else "", reverse=True)

    return render(request, "quiz_review.html", {
        "user": user, "active_page": "quiz",
        "reviews": reviews_list,
        "total_quizzes": len(quiz_hist),
    })


@app.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    _sync_mastery_from_chapters(user["id"])

    progress = get_user_progress(user["id"])
    categories = _build_category_progress(user["id"], progress)
    quiz_hist = get_quiz_history(user["id"])

    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}
    topics_mastered = sum(1 for v in mastery_dict.values() if v >= MASTERY_THRESHOLD)
    topics_in_progress = sum(1 for v in mastery_dict.values() if 0 < v < MASTERY_THRESHOLD)
    completion_pct = round(topics_mastered / NUM_TOPICS * 100)
    avg_mastery = round(sum(mastery_dict.values()) / max(len(mastery_dict), 1) * 100)
    total_quizzes = len(quiz_hist)
    avg_quiz_score = round(sum(q["score"] for q in quiz_hist) / max(len(quiz_hist), 1) * 100)

    quiz_display = [{
        "topic_name": TOPIC_DISPLAY_NAMES.get(
            int(q["topic_id"]) if isinstance(q["topic_id"], str) else q["topic_id"], ""
        ),
        "score": q["score"],
        "correct": q["correct_answers"],
        "total": q["total_questions"],
        "date": (q.get("attempted_at") or "")[:10],
    } for q in quiz_hist[:10]]

    # Build topic confidence data from chapter passes
    all_ch_passes = get_chapter_passes(user["id"])
    topic_confidence = {}
    for p in all_ch_passes:
        tid = p["topic_id"]
        if tid not in topic_confidence:
            topic_confidence[tid] = {"passed": set(), "name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}")}
        if p["score"] >= 0.8:
            topic_confidence[tid]["passed"].add(p["chapter_num"])

    confidence_list = []
    for tid, data in topic_confidence.items():
        ch_count = len(data["passed"])
        confidence_list.append({
            "topic_name": data["name"],
            "chapters_passed": ch_count,
            "main_unlocked": ch_count >= 5,
            "pct": round(ch_count / 5 * 100),
        })
    confidence_list.sort(key=lambda x: x["chapters_passed"], reverse=True)

    return render(request, "profile.html", {
        "user": user, "active_page": "profile",
        "category_progress": categories,
        "topics_mastered": topics_mastered,
        "topics_in_progress": topics_in_progress,
        "total_topics": NUM_TOPICS,
        "completion_pct": completion_pct,
        "avg_mastery": avg_mastery,
        "total_quizzes": total_quizzes,
        "avg_quiz_score": avg_quiz_score,
        "quiz_history": quiz_display,
        "topic_confidence": confidence_list,
    })


@app.get("/profile/edit", response_class=HTMLResponse)
async def profile_edit_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    return render(request, "profile_edit.html", {"user": user, "active_page": "profile", "success": None})


@app.post("/profile/edit", response_class=HTMLResponse)
async def profile_edit_submit(
    request: Request,
    name: str = Form(...),
    role: str = Form(""),
    experience_level: str = Form(""),
    organization: str = Form(""),
    bio: str = Form(""),
    profile_pic: str = Form(""),
):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    # Save base64 profile pic as a file if provided
    pic_path = user.get("profile_pic", "")
    if profile_pic and profile_pic.startswith("data:image"):
        import base64, uuid
        try:
            header, data = profile_pic.split(",", 1)
            ext = "png"
            if "jpeg" in header or "jpg" in header:
                ext = "jpg"
            elif "webp" in header:
                ext = "webp"
            filename = f"avatar_{user['id']}_{uuid.uuid4().hex[:8]}.{ext}"
            upload_dir = STATIC_DIR / "uploads"
            upload_dir.mkdir(exist_ok=True)
            filepath = upload_dir / filename
            filepath.write_bytes(base64.b64decode(data))
            pic_path = f"/static/uploads/{filename}"
        except Exception as e:
            logger.error(f"Failed to save profile pic: {e}")

    update_user(user["id"], name=name, role=role, experience_level=experience_level,
                organization=organization, bio=bio, profile_pic=pic_path)
    return RedirectResponse("/profile?saved=1", status_code=302)


# ━━━ SIMULATION PAGE (OpenENV Live Runner) ━━━

@app.get("/simulation", response_class=HTMLResponse)
async def simulation_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    return render(request, "simulation.html", {
        "user": user, "active_page": "simulation",
        "archetypes": ["fast", "steady", "struggling", "bursty", "anxious"],
        "topic_names": TOPIC_DISPLAY_NAMES,
    })


@app.get("/api-explorer", response_class=HTMLResponse)
async def api_explorer_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    spec_path = BASE_DIR / "openenv_spec.json"
    spec = json.loads(spec_path.read_text()) if spec_path.exists() else {}
    return render(request, "api_explorer.html", {
        "user": user, "active_page": "api_explorer",
        "spec": spec,
        "spec_json": json.dumps(spec, indent=2),
    })


# ━━━ SEARCH ENDPOINT ━━━

@app.get("/api/search")
async def search_topics(request: Request, q: str = ""):
    """Search topics and pages. Returns JSON results for the topbar search."""
    user = get_current_user(request)
    if not user:
        return JSONResponse({"results": []})

    query = q.strip().lower()
    if len(query) < 2:
        return JSONResponse({"results": []})

    results = []

    # Search topics
    for tid, name in TOPIC_DISPLAY_NAMES.items():
        if query in name.lower():
            group_name = ""
            for gn, tids in TOPIC_GROUPS.items():
                if tid in tids:
                    group_name = GROUP_DISPLAY_NAMES[gn]
                    break
            results.append({
                "type": "topic",
                "name": name,
                "group": group_name,
                "url": f"/learning/study?topic={tid}",
                "quiz_url": f"/quiz/start?topic={tid}&count=5",
            })

    # Search pages
    pages = [
        {"name": "Dashboard", "url": "/dashboard", "keywords": "dashboard overview stats"},
        {"name": "Learning Hub", "url": "/learning", "keywords": "learning study topics curriculum"},
        {"name": "Quizzes", "url": "/quiz", "keywords": "quiz test assessment practice"},
        {"name": "Quiz Review", "url": "/quiz/review", "keywords": "quiz review history past attempts"},
        {"name": "Growth Analytics", "url": "/growth", "keywords": "growth analytics progress chart"},
        {"name": "AI Simulation", "url": "/simulation", "keywords": "simulation ai reinforcement learning"},
        {"name": "Profile", "url": "/profile", "keywords": "profile account settings"},
        {"name": "API Explorer", "url": "/api-explorer", "keywords": "api explorer endpoints"},
    ]
    for page in pages:
        if query in page["name"].lower() or query in page["keywords"]:
            results.append({"type": "page", "name": page["name"], "url": page["url"]})

    return JSONResponse({"results": results[:15]})


# ━━━ OPENENV CORE API ENDPOINTS ━━━

class ResetRequest(BaseModel):
    archetype: str | None = None
    seed: int | None = None

class ActionRequest(BaseModel):
    action: dict

@app.post("/api/reset")
async def api_reset(req: ResetRequest):
    async with env_lock:
        options = {"archetype": req.archetype} if req.archetype else None
        obs, info = env.reset(seed=req.seed, options=options)
        return {"observation": obs_to_json(obs), "info": info}

@app.post("/api/step")
async def api_step(req: ActionRequest):
    async with env_lock:
        obs, reward, terminated, truncated, info = env.step(req.action)
        return {
            "observation": obs_to_json(obs), "reward": reward,
            "terminated": terminated, "truncated": truncated, "info": info,
        }

@app.get("/api/state")
async def api_state():
    async with env_lock:
        return {"state": env.state()}

@app.get("/health")
async def health():
    return {"status": "ok", "env": "CurriculumFlowENV", "version": "0.1.0", "step": env.step_count}

@app.get("/spec")
async def get_spec():
    spec_path = BASE_DIR / "openenv_spec.json"
    if spec_path.exists():
        return json.loads(spec_path.read_text())
    return {"error": "spec not found"}


# ━━━ OPENENV-POWERED RECOMMENDATION ENDPOINTS ━━━

@app.get("/api/agent/recommend")
async def agent_recommend(request: Request):
    """Use OpenENV agents to recommend next learning action for current user."""
    user = get_current_user(request)
    if not user:
        return JSONResponse({"error": "Not authenticated"}, status_code=401)

    progress = get_user_progress(user["id"])
    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}

    # Build observation from real user data
    tg = _get_topic_graph_data()
    unlocked = tg.get_unlocked_topics(mastery_dict)
    mastery_list = [mastery_dict.get(i, 0.0) for i in range(NUM_TOPICS)]
    mask = [1 if i in unlocked else 0 for i in range(NUM_TOPICS)]

    quiz_hist = get_quiz_history(user["id"])
    recent_correct = [1.0 if q["score"] >= 0.6 else 0.0 for q in quiz_hist[-10:]]
    while len(recent_correct) < 10:
        recent_correct.append(0.0)

    time_since = [min(50, 20) for _ in range(NUM_TOPICS)]  # default
    current_topic = 0
    if progress:
        best = max(progress, key=lambda r: r.get("last_practiced", ""))
        current_topic = best["topic_id"]

    obs = {
        "mastery": mastery_list,
        "engagement": [0.8],
        "recent_accuracy": recent_correct,
        "time_since_review": time_since,
        "current_topic": current_topic,
        "unlocked_mask": mask,
    }

    # Ask each agent
    info = {"unlocked_mask": mask}
    topic_rec = env.sequencer.select_action(obs, info)
    obs_for_diff = dict(obs)
    obs_for_diff["current_topic"] = topic_rec
    diff_rec = env.difficulty_agent.select_action(obs_for_diff, info)
    assess_rec = env.assessment_agent.select_action(obs_for_diff, info)

    # Build human-readable explanation
    topic_name = TOPIC_DISPLAY_NAMES.get(topic_rec, "Unknown")
    topic_mastery = mastery_dict.get(topic_rec, 0.0)

    sequencer_reason = f"Selected '{topic_name}' — lowest mastery ({topic_mastery:.0%}) among {len(unlocked)} unlocked topics"
    difficulty_reason = f"Difficulty {diff_rec}/5 — matched to your current mastery level (Zone of Proximal Development)"
    assess_reason = "Assessment recommended — time to validate your knowledge" if assess_rec == 1 else "Continue practicing — build more confidence before testing"

    return {
        "agents": {
            "topic_sequencer": {
                "action": topic_rec,
                "topic_name": topic_name,
                "reason": sequencer_reason,
            },
            "difficulty_adapter": {
                "action": diff_rec,
                "reason": difficulty_reason,
            },
            "assessment_timer": {
                "action": assess_rec,
                "action_label": "Take Quiz" if assess_rec == 1 else "Keep Practicing",
                "reason": assess_reason,
            },
        },
        "unlocked_count": len(unlocked),
        "total_mastery": round(sum(mastery_list) / NUM_TOPICS * 100, 1),
    }


@app.post("/api/simulation/run-episode")
async def run_simulation_episode(request: Request):
    """Run a full OpenENV episode and return step-by-step data for visualization."""
    body = await request.json()
    archetype = body.get("archetype", "steady")
    max_steps = min(body.get("max_steps", 200), 500)

    sim_env = CurriculumFlowEnv(archetype=archetype, max_steps=max_steps)
    obs, info = sim_env.reset()

    steps_data = []
    obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}

    for step_num in range(max_steps):
        # Agents decide
        agent_info = {"unlocked_mask": obs_dict["unlocked_mask"]}
        topic = sim_env.sequencer.select_action(obs_dict, agent_info)
        obs_dict["current_topic"] = topic
        difficulty = sim_env.difficulty_agent.select_action(obs_dict, agent_info)
        assess = sim_env.assessment_agent.select_action(obs_dict, agent_info)

        action = {"topic": topic, "difficulty": max(0, difficulty - 1), "assess": assess}
        obs, reward, terminated, truncated, info = sim_env.step(action)
        obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}

        steps_data.append({
            "step": step_num + 1,
            "topic_id": info["topic_id"],
            "topic_name": info["topic_name"],
            "difficulty": info["difficulty"],
            "assessed": info["assessed"],
            "correct": info.get("correct"),
            "assessment_result": info.get("assessment_result"),
            "reward": round(reward, 2),
            "cumulative_reward": round(info["episode_reward"], 2),
            "engagement": round(obs_dict["engagement"][0], 3),
            "completion_rate": round(info["completion_rate"], 3),
            "topics_mastered": info["topics_mastered"],
            "mastery": [round(m, 3) for m in obs_dict["mastery"]],
            "reward_components": {k: round(v, 2) for k, v in info["reward_components"].items()},
        })

        if terminated or truncated:
            break

    final_state = sim_env.state()
    return {
        "episode": {
            "archetype": archetype,
            "total_steps": len(steps_data),
            "final_reward": round(final_state["cumulative_reward"], 2),
            "completion_rate": round(final_state["completion_rate"], 3),
            "topics_mastered": final_state["topics_mastered"],
            "terminated": terminated if 'terminated' in dir() else False,
        },
        "steps": steps_data,
        "topic_names": {str(k): v for k, v in TOPIC_DISPLAY_NAMES.items()},
    }


@app.post("/api/simulation/step-by-step")
async def simulation_step(request: Request):
    """Single step through the global OpenENV instance — for interactive mode."""
    body = await request.json()
    use_agents = body.get("use_agents", True)

    async with env_lock:
        obs = env._get_obs()
        obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}
        agent_info = {"unlocked_mask": obs_dict["unlocked_mask"]}

        if use_agents:
            topic = env.sequencer.select_action(obs_dict, agent_info)
            obs_dict["current_topic"] = topic
            difficulty = env.difficulty_agent.select_action(obs_dict, agent_info)
            assess = env.assessment_agent.select_action(obs_dict, agent_info)
        else:
            topic = body.get("topic", 0)
            difficulty = body.get("difficulty", 1)
            assess = body.get("assess", 0)

        action = {"topic": topic, "difficulty": max(0, difficulty - 1), "assess": assess}
        obs, reward, terminated, truncated, info = env.step(action)
        obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs.items()}

        return {
            "observation": obs_dict,
            "reward": round(reward, 2),
            "terminated": terminated,
            "truncated": truncated,
            "info": info,
            "agent_decisions": {
                "topic_sequencer": {"chose": topic, "name": TOPIC_DISPLAY_NAMES.get(topic, "?")},
                "difficulty_adapter": {"chose": difficulty},
                "assessment_timer": {"chose": assess, "label": "Assess" if assess else "Practice"},
            },
        }


@app.get("/api/reward-breakdown")
async def reward_breakdown():
    """Get cumulative reward component breakdown from current episode."""
    async with env_lock:
        state = env.state()
        log = state.get("reward_components_log", [])
        totals = {}
        for entry in log:
            for k, v in entry.items():
                totals[k] = totals.get(k, 0.0) + v
        return {
            "step_count": state["step_count"],
            "cumulative_reward": round(state["cumulative_reward"], 2),
            "components": {k: round(v, 2) for k, v in totals.items()},
        }
