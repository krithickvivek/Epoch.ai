"""FastAPI server - routes, auth, templates, and OpenENV API."""

import json
import logging
import asyncio
from pathlib import Path

# Load .env file for local development (ignored in production/Docker)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from fastapi import FastAPI, Request, Form, HTTPException, WebSocket, WebSocketDisconnect
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
    record_mock_test, get_mock_test_history,
    get_daily_tasks, add_daily_task, complete_daily_task, delete_daily_task,
    get_weekly_tasks, add_bookmark, get_bookmarks, remove_bookmark,
    record_interview_session, get_interview_history,
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
from curriculum_flow_env.hf_ai import (
    HF_CHAT_MODEL,
    HF_QUIZ_MODEL,
    generate_quiz_with_ai,
    generate_support_chat_reply,
)
from curriculum_flow_env.ui.formatting import (
    mastery_to_label, engagement_to_label, obs_to_json,
)
from curriculum_flow_env.leetcode_data import DSA_PATTERNS, PROBLEMS_ROADMAP

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


# """ HELPERS """

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


def _sanitize_quiz_questions(questions: list[dict], desired_count: int | None = None) -> list[dict]:
    """Normalize quiz payload into a safe render/submit format."""
    safe: list[dict] = []
    target = desired_count if desired_count is not None else len(questions)
    for raw in questions:
        if not isinstance(raw, dict):
            continue
        question = str(raw.get("question", "")).strip()
        options_raw = raw.get("options", [])
        if isinstance(options_raw, dict):
            options_raw = list(options_raw.values())
        options = [str(opt).strip() for opt in options_raw if str(opt).strip()]
        if not question or len(options) < 4:
            continue
        options = options[:4]

        correct_raw = raw.get("correct", 0)
        try:
            correct = int(correct_raw)
        except (TypeError, ValueError):
            correct = 0
        correct = max(0, min(3, correct))

        safe.append({
            "question": question,
            "options": options,
            "correct": correct,
            "explanation": str(raw.get("explanation", "")).strip(),
        })
        if target and len(safe) >= target:
            break

    if not safe:
        safe = [{
            "question": "Sample question",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct": 0,
            "explanation": "This is a fallback question.",
        }]

    if desired_count is not None:
        while len(safe) < desired_count:
            base = dict(safe[len(safe) % len(safe)])
            base["question"] = f"{base['question']} (Practice variant {len(safe) + 1})"
            safe.append(base)
        safe = safe[:desired_count]

    return safe


def _serialize_quiz_questions(questions: list[dict]) -> tuple[list[dict], str]:
    indexed = []
    for i, q in enumerate(questions):
        row = dict(q)
        row["idx"] = i
        indexed.append(row)

    question_data_json = json.dumps([{
        "question": q["question"],
        "options": q["options"],
        "correct": q["correct"],
        "explanation": q.get("explanation", ""),
    } for q in indexed])
    return indexed, question_data_json


def _fallback_quiz_questions(topic: int, count: int) -> list[dict]:
    target = max(1, min(int(count or 5), 25))
    try:
        from curriculum_flow_env.quiz import generate_quiz
        base_questions = generate_quiz(topic, target)
    except Exception:
        base_questions = []

    if not base_questions:
        base_questions = [{
            "question": f"Sample question {i + 1} for {TOPIC_DISPLAY_NAMES.get(topic, 'topic')}",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct": 0,
            "explanation": "This is a fallback question.",
        } for i in range(max(3, target))]

    return _sanitize_quiz_questions(base_questions, desired_count=target)


class AIChatRequest(BaseModel):
    message: str
    history: list = []


def _local_support_chat_reply(user_message: str, user_context: str = "") -> str:
    """Concise fallback assistant (2-3 lines) when external AI is unavailable."""
    text = (user_message or "").strip()
    msg = text.lower()

    #  Greetings 
    if any(k in msg for k in ["hello", "hi ", "hi!", "hey", "good morning", "good evening", "good afternoon", "howdy"]) or msg in ("hi", "hey", "hello"):
        return "Hey! I'm Epoch AI, your placement prep buddy. Ask me about any topic - aptitude, verbal, DSA, interviews, companies, or study tips!"

    #  Thanks / Bye 
    if any(k in msg for k in ["thank", "thanks", "thx", "appreciate"]):
        return "You're welcome! Keep up the great work. Feel free to ask anytime!"
    if any(k in msg for k in ["bye", "goodbye", "see you", "later"]):
        return "See you! Remember - small daily progress adds up. Keep going!"

    #  Who are you 
    if any(k in msg for k in ["who are you", "what are you", "your name", "about you", "what can you do"]):
        return "I'm Epoch AI - your placement assistant. I help with aptitude, verbal, reasoning, DSA, programming, OS, DBMS, CN, interviews, and company-specific prep. Ask me anything!"

    #  Verbal Ability 
    if any(k in msg for k in ["verbal", "synonym", "antonym", "sentence completion", "reading comprehension",
                                "para jumble", "spotting error", "idiom", "phrase", "grammar",
                                "vocabulary", "english", "language", "word meaning", "passage"]):
        return (
            "Verbal ability is key for TCS, Infosys, Wipro, and most service company rounds. "
            "Focus on synonyms, antonyms, reading comprehension, and spotting errors. "
            "Practice daily on the Learning page under Verbal Ability - even 15 min/day helps!"
        )

    #  Quantitative Aptitude 
    if any(k in msg for k in ["aptitude", "quantitative", "percentage", "profit", "loss", "ratio",
                                "proportion", "time and work", "time and distance", "interest",
                                "average", "age", "hcf", "lcm", "permutation", "combination",
                                "speed", "train", "pipe", "cistern", "number system"]):
        return (
            "Quantitative aptitude appears in almost every placement exam. "
            "Master percentages, ratio, time & work, and number series first - they cover 60% of questions. "
            "Head to Learning > Quantitative Aptitude to practice with AI-tracked progress!"
        )

    #  Logical Reasoning 
    if any(k in msg for k in ["reasoning", "logical", "coding decoding", "blood relation", "direction",
                                "seating", "syllogism", "number series", "analogy", "deduction",
                                "puzzle", "pattern"]):
        return (
            "Logical reasoning tests your analytical thinking - common in TCS, Infosys, Accenture, and more. "
            "Practice coding-decoding, syllogism, and seating arrangement regularly. "
            "Go to Learning > Logical Reasoning to start building these skills!"
        )

    #  Data Interpretation 
    if any(k in msg for k in ["data interpretation", "bar graph", "pie chart", "line graph", "table",
                                "chart", "data analysis", "di "]):
        return (
            "Data interpretation is tested in most aptitude rounds - you'll see tables, bar/pie/line charts. "
            "Practice reading data quickly and doing mental math for speed. "
            "Check out Learning > Data Interpretation for structured practice!"
        )

    #  Programming & CS Basics 
    if any(k in msg for k in ["c programming", "c basic", "data type", "operator", "control flow",
                                "pointer", "reference", "oop", "object oriented", "sql", "database query"]):
        return (
            "Programming fundamentals are must-haves for coding rounds. "
            "Solidify C/C++ basics, OOP concepts, and SQL - they appear in both MCQs and interviews. "
            "Practice on Learning > Programming & CS!"
        )

    #  OS 
    if any(k in msg for k in ["operating system", " os ", "process", "thread", "memory management",
                                "scheduling", "deadlock", "paging", "virtual memory", "semaphore", "mutex"]):
        return (
            "OS concepts (processes, threads, scheduling, deadlocks, memory management) are frequently asked in interviews. "
            "Focus on process vs thread, deadlock conditions, and paging for placements. "
            "Study on Learning > Core CS Subjects!"
        )

    #  DBMS 
    if any(k in msg for k in ["dbms", "database", "normalization", "transaction", "indexing", "acid",
                                "sql", "join", "primary key", "foreign key", "relational"]):
        return (
            "DBMS is a hot interview topic - normalization, SQL joins, ACID properties, and indexing are most asked. "
            "Practice writing SQL queries and understanding transaction isolation levels. "
            "Go to Learning > Core CS Subjects for DBMS topics!"
        )

    #  Computer Networks 
    if any(k in msg for k in ["network", "osi", "tcp", "ip ", "protocol", "http", "dns", "subnet",
                                "routing", "firewall", "security", " cn "]):
        return (
            "Computer Networks: focus on OSI/TCP-IP layers, HTTP vs HTTPS, DNS, and subnetting. "
            "These come up in both written rounds and technical interviews. "
            "Practice on Learning > Core CS Subjects!"
        )

    #  DSA topics 
    if any(k in msg for k in ["array", "string", "linked list", "tree", "graph", "stack", "queue",
                                "heap", "hash", "dynamic programming", "dp ", "greedy", "backtrack",
                                "recursion", "sorting", "searching", "binary search", "bfs", "dfs",
                                "sliding window", "two pointer", "trie", "dsa", "data structure",
                                "algorithm", "leetcode", "bit manipulation"]):
        topic_map = {
            "array": "Arrays", "string": "Strings", "linked list": "Linked Lists",
            "tree": "Trees", "graph": "Graphs", "stack": "Stacks", "queue": "Queues",
            "heap": "Heaps", "hash": "Hashing", "dynamic programming": "DP",
            "dp ": "DP", "greedy": "Greedy", "backtrack": "Backtracking",
            "recursion": "Recursion", "sorting": "Sorting", "binary search": "Binary Search",
            "sliding window": "Sliding Window", "two pointer": "Two Pointers",
            "trie": "Tries", "bfs": "BFS", "dfs": "DFS", "bit manipulation": "Bit Manipulation",
        }
        topic = "DSA"
        for key, name in topic_map.items():
            if key in msg:
                topic = name
                break
        return (
            f"{topic} is essential for coding rounds at top companies. "
            f"Start with easy problems, understand the pattern, then move to medium/hard. "
            f"Head to the DSA Roadmap for curated problems with company tags!"
        )

    #  Company-specific 
    company_map = {
        "tcs": "TCS", "infosys": "Infosys", "wipro": "Wipro", "accenture": "Accenture",
        "amazon": "Amazon", "google": "Google", "microsoft": "Microsoft", "meta": "Meta",
        "apple": "Apple", "flipkart": "Flipkart", "adobe": "Adobe", "uber": "Uber",
        "samsung": "Samsung", "paytm": "Paytm", "de shaw": "DE Shaw",
        "morgan stanley": "Morgan Stanley", "intuit": "Intuit", "goldman": "Goldman Sachs",
        "oracle": "Oracle", "cognizant": "Cognizant", "capgemini": "Capgemini",
    }
    for key, name in company_map.items():
        if key in msg:
            return (
                f"For {name} prep, check Company Prep from the sidebar for their exam pattern and strategy. "
                f"The DSA Roadmap also has problems tagged by company. Focus on their most-asked topics!"
            )

    #  Interview prep 
    if any(k in msg for k in ["interview", "hr round", "technical round", "behavioral", "star method"]):
        return (
            "For interviews: revise your weak DSA topics, prepare STAR stories for HR rounds, "
            "and practice explaining your thought process out loud. "
            "Try the Interview Sim from the sidebar for hands-on practice!"
        )

    #  Quiz / MCQ / Mock 
    if any(k in msg for k in ["quiz", "mcq", "test", "mock", "practice test"]):
        return (
            "Use the AI Quiz Generator - pick a topic, set difficulty, and practice! "
            "Review explanations after each attempt and retry with higher difficulty. "
            "Head to Quizzes or Mock Tests from the sidebar!"
        )

    #  Study plan / Roadmap 
    if any(k in msg for k in ["roadmap", "plan", "schedule", "study", "routine", "how to start",
                                "where to start", "beginner", "timetable", "prepare"]):
        return (
            "Start with aptitude + verbal basics, then move to DSA and core CS. "
            "Spend 2-3 hours daily: 1 hr concepts, 1 hr practice, 30 min review. "
            "Use the Daily Planner from the sidebar to stay consistent!"
        )

    #  Layoffs / Job loss 
    if any(k in msg for k in ["layoff", "laid off", "job loss", "fired", "terminated"]):
        return (
            "That's tough, but you're already taking action by being here. "
            "Update your resume, practice 2 topics daily, and take 1 quiz per day. "
            "Consistency for 2 weeks can make a huge difference. You've got this!"
        )

    #  Motivation / Stress 
    if any(k in msg for k in ["motivat", "stress", "anxious", "nervous", "scared", "worried",
                                "pressure", "depress", "can't do", "give up", "impossible", "fail"]):
        return (
            "It's completely normal to feel this way. Every expert was once a beginner. "
            "Focus on just one small task today - solve one problem, read one topic. "
            "Small steps daily will get you there. You've got this!"
        )

    #  Resume / LinkedIn 
    if any(k in msg for k in ["resume", "cv ", "linkedin", "portfolio", "cover letter"]):
        return (
            "Keep your resume to 1 page: Education, Projects (with GitHub links), Skills. "
            "Quantify your achievements and tailor keywords to each job. "
            "For LinkedIn, add a strong headline and list key skills - recruiters search there!"
        )

    #  Time complexity 
    if any(k in msg for k in ["time complexity", "space complexity", "big o", "big-o", "complexity"]):
        return (
            "Common complexities: O(1) constant, O(log n) binary search, O(n) linear, O(n log n) merge sort, O(n^2) nested loops. "
            "Always analyze worst case and practice identifying complexity for every solution you write!"
        )

    #  Placement / Career 
    if any(k in msg for k in ["placement", "campus", "off campus", "job", "career", "hire", "recruit", "salary", "package"]):
        return (
            "For placement prep: master aptitude + verbal for service companies, DSA for product companies. "
            "Build 2-3 solid projects and practice company-specific questions. "
            "Use Company Prep and DSA Roadmap from the sidebar!"
        )

    #  Meaning / Definition / Explain / What is 
    if any(k in msg for k in ["meaning", "define", "definition", "what is", "what are", "explain",
                                "what does", "tell me about", "how does", "how to", "why is", "difference between"]):
        return (
            f"I'd love to help! I work best with placement topics - try asking about DSA concepts, "
            f"aptitude, verbal, reasoning, OS, DBMS, CN, or interview prep. "
            f"For example: 'Explain dynamic programming' or 'What is normalization in DBMS?'"
        )

    #  Numbers / Math 
    if any(k in msg for k in ["number", "math", "calculat", "formula"]):
        return (
            "Number concepts like GCD/LCM, primes, and modular arithmetic appear in aptitude rounds. "
            "Practice them under Learning > Quantitative Aptitude for structured prep!"
        )

    #  OOP / Design Patterns 
    if any(k in msg for k in ["oop", "object oriented", "design pattern", "solid", "inheritance",
                                "polymorphism", "encapsulation", "abstraction"]):
        return (
            "OOP is asked in almost every technical interview - know the 4 pillars (encapsulation, inheritance, polymorphism, abstraction). "
            "Practice SOLID principles and common design patterns. Check Learning > Core CS Subjects!"
        )

    #  Default: short, friendly, not robotic 
    return (
        "Hmm, I'm not sure about that one! I'm best with placement-related topics - "
        "DSA, aptitude, verbal, reasoning, OS, DBMS, CN, interviews, and company prep. "
        "Try asking me something in those areas and I'll give you a helpful answer!"
    )


# """ PUBLIC ROUTES (no auth) """

@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    user = get_current_user(request)
    if user:
        return RedirectResponse("/home", status_code=302)
    return render(request, "landing.html")


@app.get("/demo", response_class=HTMLResponse)
async def demo_page(request: Request):
    """Interactive AI demo — no login required."""
    return render(request, "demo.html")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    user = get_current_user(request)
    if user:
        return RedirectResponse("/home", status_code=302)
    return render(request, "login.html", {"error": None})


@app.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, email: str = Form(...), password: str = Form(...)):
    logger.info(f"Login attempt for email: {email}")
    user = verify_password(email, password)
    if not user:
        # Debug: check if user exists at all
        from curriculum_flow_env.database import get_user_by_email as _gube
        existing = _gube(email)
        if existing:
            logger.warning(f"Login failed: user {email} exists but password mismatch")
        else:
            logger.warning(f"Login failed: user {email} not found in database")
        return render(request, "login.html", {"error": "Invalid email or password"})
    logger.info(f"Login successful for user {email} (id={user['id']})")
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
    logger.info(f"Signup successful for {email} (id={new_user['id']})")
    # Verify the password works immediately after creation
    verify_check = verify_password(email, password)
    if verify_check:
        logger.info(f"Post-signup verify OK for {email}")
    else:
        logger.error(f"Post-signup verify FAILED for {email} - DB issue!")
    response = RedirectResponse("/home", status_code=302)
    login_user(response, new_user["id"])
    return response


@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse("/", status_code=302)
    logout_user(response, request)
    return response


# """ AUTH-REQUIRED ROUTES """

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

    # Get chapter pass data per topic for displaying chapter-wise quiz status
    all_chapter_passes = get_chapter_passes(user["id"])
    topic_chapter_passes = {}  # {topic_id: {chapter_num: score}}
    for p in all_chapter_passes:
        tid = p["topic_id"]
        if tid not in topic_chapter_passes:
            topic_chapter_passes[tid] = {}
        cnum = p["chapter_num"]
        topic_chapter_passes[tid][cnum] = round(p["score"] * 100)

    # Build per-chapter best scores from quiz history
    chapter_best_scores = {}  # {(topic_id, chapter_num): best_score_pct}
    for q in quiz_hist:
        tid = q["topic_id"]
        tid = int(tid) if isinstance(tid, str) else tid
        score_pct = round(q["score"] * 100)
        # Infer chapter from results_json or attempt context
        # For chapter quizzes recorded via record_quiz_attempt, we track per-topic best
        if tid not in chapter_best_scores:
            chapter_best_scores[tid] = score_pct
        elif score_pct > chapter_best_scores[tid]:
            chapter_best_scores[tid] = score_pct

    for t in available:
        for gn, tids in TOPIC_GROUPS.items():
            if t["id"] in tids:
                t["group"] = GROUP_DISPLAY_NAMES[gn]
                t["group_color"] = GROUP_COLORS[gn]
                t["group_slug"] = gn
                break
        t["display_name"] = TOPIC_DISPLAY_NAMES.get(t["id"], t.get("name", ""))
        t["best_score"] = best_scores.get(t["id"])
        t["unlocked"] = t["id"] in unlocked_mains
        # Chapter pass info: {1: score_pct, 2: score_pct, ...}
        t["chapter_passes"] = topic_chapter_passes.get(t["id"], {})
        t["chapters_passed_count"] = len([s for s in t["chapter_passes"].values() if s >= 80])

    return render(request, "quiz.html", {
        "user": user, "active_page": "quiz",
        "mode": "select", "available_topics": available,
    })


@app.api_route("/quiz/start", methods=["GET", "POST"], response_class=HTMLResponse)
async def quiz_start(
    request: Request,
    topic: int = 0,
    count: int = 5,
    chapter: int = 0,
    ai: int = 0,
    difficulty: str = "mixed",
    prompt: str = "",
):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    if request.method == "POST":
        form = await request.form()
        topic = int(form.get("topic", topic))
        count = int(form.get("count", count))
        chapter = int(form.get("chapter", chapter))
        ai = int(form.get("ai", ai))
        difficulty = str(form.get("difficulty", difficulty))
        prompt = str(form.get("prompt", prompt or "")).strip()

    topic = max(0, min(topic, NUM_TOPICS - 1))
    count = max(1, min(int(count or 5), 25))
    ai_mode = int(ai or 0) == 1
    difficulty = (difficulty or "mixed").strip().lower()
    if difficulty not in {"easy", "medium", "hard", "mixed"}:
        difficulty = "mixed"

    ai_note = ""
    model_used = ""

    if ai_mode:
        model_used = HF_QUIZ_MODEL
        try:
            ai_questions = await generate_quiz_with_ai(
                topic_name=TOPIC_DISPLAY_NAMES.get(topic, "General aptitude"),
                question_count=count,
                difficulty=difficulty,
                focus_prompt=prompt,
            )
            questions = _sanitize_quiz_questions(ai_questions, desired_count=count)
        except Exception as e:
            logger.error(f"AI quiz generation failed for topic={topic}: {e}")
            questions = _fallback_quiz_questions(topic, count)
            model_used = "fallback_question_bank"
            ai_note = "AI model was unavailable, so a randomized local quiz was loaded."
    else:
        try:
            from curriculum_flow_env.quiz import generate_quiz
            questions = generate_quiz(topic, count)
        except (ImportError, Exception):
            questions = _fallback_quiz_questions(topic, count)
        questions = _sanitize_quiz_questions(questions, desired_count=count)

    questions, question_data_json = _serialize_quiz_questions(questions)

    quiz_label = TOPIC_DISPLAY_NAMES.get(topic, "Topic")
    if ai_mode:
        quiz_label += " - AI Quiz"
    if chapter > 0:
        quiz_label += f" - Chapter {chapter}"

    return render(request, "quiz.html", {
        "user": user, "active_page": "quiz",
        "mode": "active",
        "topic_id": topic,
        "topic_name": quiz_label,
        "chapter": chapter,
        "questions": questions,
        "question_data_json": question_data_json,
        "pass_rate": 80,
        "ai_quiz": ai_mode,
        "ai_model": model_used,
        "ai_difficulty": difficulty,
        "ai_prompt": prompt,
        "ai_note": ai_note,
    })


@app.api_route("/quiz/start-ai", methods=["GET", "POST"], response_class=HTMLResponse)
async def quiz_start_ai(
    request: Request,
    topic: int = 0,
    count: int = 10,
    difficulty: str = "mixed",
    prompt: str = "",
):
    if request.method == "POST":
        form = await request.form()
        topic = int(form.get("topic", topic))
        count = int(form.get("count", count))
        difficulty = str(form.get("difficulty", difficulty))
        prompt = str(form.get("prompt", prompt or "")).strip()
    return await quiz_start(
        request,
        topic=topic,
        count=count,
        chapter=0,
        ai=1,
        difficulty=difficulty,
        prompt=prompt,
    )


@app.post("/quiz/submit", response_class=HTMLResponse)
async def quiz_submit(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    form = await request.form()
    topic_id = int(form.get("topic_id", 0))
    chapter_num = int(form.get("chapter", 0))
    question_data = json.loads(form.get("question_data", "[]"))
    is_ai_quiz = str(form.get("ai_quiz", "0")).strip() == "1"
    ai_difficulty = str(form.get("ai_difficulty", "mixed")).strip().lower()
    if ai_difficulty not in {"easy", "medium", "hard", "mixed"}:
        ai_difficulty = "mixed"

    # Collect answers - handle missing, empty, or non-numeric values gracefully
    answers = []
    for i in range(len(question_data)):
        ans = form.get(f"answer_{i}")
        try:
            answers.append(int(ans) if ans is not None and str(ans).strip() != "" else -1)
        except (ValueError, TypeError):
            answers.append(-1)

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
            env_feedback = "Validated mastery - the Assessment Timer confirms strong understanding."
        elif components.get("assessment_reward", 0) < 0:
            env_feedback = "The Assessment Timer suggests more practice before retesting this topic."
        else:
            env_feedback = "Good attempt - the Difficulty Adapter will adjust future problems."

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
        "difficulty_reason": f"Matched to mastery level ({round(mastery_dict_updated.get(next_topic, 0)*100)}%)" if next_diff <= 3 else f"Challenging you - accuracy is high",
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
        "ai_quiz": is_ai_quiz,
        "ai_difficulty": ai_difficulty,
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

    # Growth data for chart " include group for filtering
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

    # Category growth " use average mastery per category (not just fully-mastered count)
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

    # Get chapter pass data for chapter-wise progress display
    all_ch_passes = get_chapter_passes(user["id"])
    topic_ch_data = {}  # {tid: {ch_num: score_pct}}
    for p in all_ch_passes:
        tid = p["topic_id"]
        if tid not in topic_ch_data:
            topic_ch_data[tid] = {}
        topic_ch_data[tid][p["chapter_num"]] = round(p["score"] * 100)

    # Group quiz history by topic
    topic_reviews = {}
    for q in quiz_hist:
        tid_raw = q["topic_id"]
        tid = int(tid_raw) if isinstance(tid_raw, str) else tid_raw
        if tid not in topic_reviews:
            group_name = ""
            group_slug = ""
            group_color = "#4A8AFF"
            for gn, tids in TOPIC_GROUPS.items():
                if tid in tids:
                    group_name = GROUP_DISPLAY_NAMES[gn]
                    group_slug = gn
                    group_color = GROUP_COLORS[gn]
                    break
            topic_reviews[tid] = {
                "topic_id": tid,
                "topic_name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}"),
                "group": group_name,
                "group_slug": group_slug,
                "group_color": group_color,
                "mastery": round(mastery_dict.get(tid_raw, mastery_dict.get(tid, 0.0)) * 100),
                "attempts": [],
                "best_score": 0,
                "latest_score": 0,
                "total_attempts": 0,
                "chapter_passes": topic_ch_data.get(tid, {}),
                "chapters_passed_count": len([s for s in topic_ch_data.get(tid, {}).values() if s >= 80]),
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

    # Build category list for filtering
    category_list = [{"slug": gn, "name": GROUP_DISPLAY_NAMES[gn], "color": GROUP_COLORS[gn]} for gn in TOPIC_GROUPS]

    return render(request, "quiz_review.html", {
        "user": user, "active_page": "quiz",
        "reviews": reviews_list,
        "total_quizzes": len(quiz_hist),
        "categories": category_list,
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
    } for q in quiz_hist[:3]]

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


# """ SIMULATION PAGE (OpenENV Live Runner) """

#  DSA ROADMAP PAGE 
# DSA_PATTERNS and PROBLEMS_ROADMAP imported from curriculum_flow_env.leetcode_data


@app.get("/dsa-roadmap", response_class=HTMLResponse)
async def dsa_roadmap_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    progress = get_user_progress(user["id"])
    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}

    dsa_topic_ids = TOPIC_GROUPS.get("dsa_deep_dive", [])
    dsa_topics = []
    for tid in dsa_topic_ids:
        m = mastery_dict.get(tid, 0.0)
        dsa_topics.append({
            "id": tid,
            "display_name": TOPIC_DISPLAY_NAMES.get(tid, f"Topic {tid}"),
            "mastery": round(m * 100),
            "difficulty": TOPIC_DIFFICULTIES.get(tid, 3),
            "problem_count": len([p for p in PROBLEMS_ROADMAP if p.get("topic", "").lower().replace(" ", "_") in TOPIC_DISPLAY_NAMES.get(tid, "").lower().replace(" & ", "_").replace(" ", "_")]) or "-",
        })

    total_problems = len(PROBLEMS_ROADMAP)
    user_progress = {tid: round(mastery_dict.get(tid, 0.0) * 100) for tid in dsa_topic_ids}

    return render(request, "dsa_roadmap.html", {
        "user": user, "active_page": "dsa_roadmap",
        "dsa_topics": dsa_topics,
        "patterns": DSA_PATTERNS,
        "problems_roadmap": PROBLEMS_ROADMAP,
        "total_problems": total_problems,
        "user_progress": user_progress,
    })


#  COMPANY PREPARATION PAGE 

COMPANY_DATA = [
    {
        "name": "TCS", "color": "#1a73e8", "package_range": "3.3 - 7 LPA",
        "difficulty": "Easy-Medium", "hiring_months": "Aug-Oct",
        "sections": ["Verbal Ability", "Quantitative Aptitude", "Reasoning", "Programming Logic", "Coding"],
        "exam_name": "TCS NQT (National Qualifier Test)",
        "strategy": [
            "Focus heavily on Quantitative Aptitude -- 25-30 questions in exam",
            "Practice basic coding in C/Java/Python -- 1-2 coding questions",
            "Verbal section tests grammar, reading comprehension, sentence correction",
            "Reasoning is moderate difficulty -- practice seating arrangement and syllogism",
            "Time management is key: ~90 minutes for all sections",
        ],
        "sample_questions": [
            {"q": "A train running at 54 km/hr crosses a platform in 30 sec and a man standing on the platform in 18 sec. Find the length of the platform.", "type": "Quant"},
            {"q": "If DELHI is coded as 73541, how is HIDE coded?", "type": "Reasoning"},
            {"q": "Write a program to check if a number is a palindrome.", "type": "Coding"},
        ],
    },
    {
        "name": "Infosys", "color": "#007cc3", "package_range": "3.6 - 8 LPA",
        "difficulty": "Medium", "hiring_months": "Sep-Nov",
        "sections": ["Quantitative Aptitude", "Logical Reasoning", "Verbal", "Puzzle Solving", "Programming"],
        "exam_name": "Infosys InfyTQ / SP Assessment",
        "strategy": [
            "InfyTQ certification gives direct interview shortlist -- prioritize this",
            "Puzzle solving section is unique to Infosys -- practice grid puzzles and logical puzzles",
            "Programming section tests Python/Java fundamentals",
            "SP roles have harder coding with DSA questions",
            "Practice previous year InfyTQ papers extensively",
        ],
        "sample_questions": [
            {"q": "A and B can do a piece of work in 12 days, B and C in 15 days, A and C in 20 days. How long will they take together?", "type": "Quant"},
            {"q": "Complete the series: 2, 6, 12, 20, 30, ?", "type": "Reasoning"},
            {"q": "Write a function to find the second largest element in an array.", "type": "Coding"},
        ],
    },
    {
        "name": "Wipro", "color": "#5c2d91", "package_range": "3.5 - 6.5 LPA",
        "difficulty": "Easy-Medium", "hiring_months": "Jul-Sep",
        "sections": ["Aptitude", "Written Communication", "Technical MCQ", "Coding"],
        "exam_name": "Wipro NLTH (National Level Talent Hunt)",
        "strategy": [
            "Written communication section is unique -- practice essay writing",
            "Aptitude section has 20 questions in 20 minutes -- speed is crucial",
            "Technical MCQs cover CS fundamentals: OS, DBMS, Networking",
            "1-2 coding questions of easy-medium difficulty",
            "Focus on accuracy over speed in the coding section",
        ],
        "sample_questions": [
            {"q": "If the price of an item is increased by 20% and then decreased by 20%, what is the net change?", "type": "Quant"},
            {"q": "Write a program to reverse a string without using built-in functions.", "type": "Coding"},
            {"q": "What is normalization in DBMS? Explain 3NF.", "type": "Technical"},
        ],
    },
    {
        "name": "Accenture", "color": "#a100ff", "package_range": "4.5 - 8 LPA",
        "difficulty": "Medium", "hiring_months": "Aug-Dec",
        "sections": ["Cognitive Assessment", "Technical Assessment", "Coding"],
        "exam_name": "Accenture Assessment",
        "strategy": [
            "Cognitive section is adaptive -- questions get harder if you answer correctly",
            "Technical section covers DBMS, OS, OOP, Networking fundamentals",
            "Coding section has 2 problems -- one easy, one medium",
            "Focus on strong fundamentals in all CS subjects",
            "Communication assessment may include email writing tasks",
        ],
        "sample_questions": [
            {"q": "Three pipes A, B, C can fill a tank in 6, 8, 12 hours. If all three are opened together, in how much time will the tank be filled?", "type": "Quant"},
            {"q": "Explain the difference between process and thread.", "type": "Technical"},
            {"q": "Write a program to find the factorial of a number using recursion.", "type": "Coding"},
        ],
    },
    {
        "name": "Amazon", "color": "#ff9900", "package_range": "12 - 30+ LPA",
        "difficulty": "Hard", "hiring_months": "Jun-Aug, Jan-Mar",
        "sections": ["Online Assessment (2 coding)", "Technical Round 1", "Technical Round 2", "Hiring Manager / Bar Raiser"],
        "exam_name": "Amazon SDE Online Assessment",
        "strategy": [
            "Online Assessment has 2 coding problems -- target both correct with optimal solutions",
            "Technical rounds focus heavily on DSA: Trees, Graphs, DP, System Design",
            "Amazon Leadership Principles are critical -- prepare STAR method examples",
            "Practice on LeetCode medium-hard problems tagged Amazon",
            "System design basics expected even for SDE-1",
            "Behavioral questions carry equal weight -- never skip LP preparation",
        ],
        "sample_questions": [
            {"q": "Given a binary tree, find the lowest common ancestor of two nodes.", "type": "DSA"},
            {"q": "Design a URL shortening service like bit.ly.", "type": "System Design"},
            {"q": "Tell me about a time when you disagreed with your team. (Customer Obsession LP)", "type": "Behavioral"},
        ],
    },
    {
        "name": "Microsoft", "color": "#00a4ef", "package_range": "15 - 40+ LPA",
        "difficulty": "Hard", "hiring_months": "Jul-Sep, Jan-Feb",
        "sections": ["Online Assessment (3 coding)", "Group Fly Round", "Technical Round 1", "Technical Round 2", "AA/Hiring Manager"],
        "exam_name": "Microsoft Online Assessment",
        "strategy": [
            "Group fly round: solve 1-2 coding problems on paper in 1 hour with other candidates",
            "Technical rounds go deep into DSA: focus on Trees, Graphs, DP, String algorithms",
            "Microsoft values clean code and good communication of thought process",
            "Think aloud during interviews -- explain your approach before coding",
            "Practice writing code on paper/whiteboard -- no IDE during on-site",
        ],
        "sample_questions": [
            {"q": "Implement LRU Cache with O(1) get and put operations.", "type": "DSA"},
            {"q": "Given an array, find the maximum sum subarray (Kadane's algorithm).", "type": "DSA"},
            {"q": "Design a real-time collaborative text editor.", "type": "System Design"},
        ],
    },
]


@app.get("/company-prep", response_class=HTMLResponse)
async def company_prep_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    mock_hist = get_mock_test_history(user["id"])
    user_mock_scores = {}
    for m in mock_hist:
        comp = m.get("company", "")
        if comp and (comp not in user_mock_scores or m["score"] > user_mock_scores[comp]):
            user_mock_scores[comp] = round(m["score"] * 100)

    return render(request, "company_prep.html", {
        "user": user, "active_page": "company_prep",
        "companies": COMPANY_DATA,
        "user_mock_scores": user_mock_scores,
    })


#  MOCK TESTS PAGE 

MOCK_TEST_CATALOG = [
    {"id": "full_placement", "name": "Full Placement Test", "type": "full", "company": "",
     "duration": 90, "questions": 60, "sections": ["Quant", "Reasoning", "Verbal", "Technical", "Coding"],
     "difficulty": "Mixed"},
    {"id": "tcs_mock", "name": "TCS NQT Mock", "type": "company", "company": "TCS",
     "duration": 90, "questions": 50, "sections": ["Verbal", "Quant", "Reasoning", "Programming"],
     "difficulty": "Easy-Medium"},
    {"id": "infosys_mock", "name": "Infosys InfyTQ Mock", "type": "company", "company": "Infosys",
     "duration": 75, "questions": 45, "sections": ["Quant", "Reasoning", "Verbal", "Puzzle"],
     "difficulty": "Medium"},
    {"id": "wipro_mock", "name": "Wipro NLTH Mock", "type": "company", "company": "Wipro",
     "duration": 60, "questions": 40, "sections": ["Aptitude", "Technical", "Coding"],
     "difficulty": "Easy-Medium"},
    {"id": "accenture_mock", "name": "Accenture Mock", "type": "company", "company": "Accenture",
     "duration": 75, "questions": 45, "sections": ["Cognitive", "Technical", "Coding"],
     "difficulty": "Medium"},
    {"id": "amazon_mock", "name": "Amazon SDE Mock", "type": "company", "company": "Amazon",
     "duration": 70, "questions": 4, "sections": ["Coding (2)", "Workstyle Assessment"],
     "difficulty": "Hard"},
    {"id": "microsoft_mock", "name": "Microsoft Mock", "type": "company", "company": "Microsoft",
     "duration": 75, "questions": 3, "sections": ["Coding (3)"],
     "difficulty": "Hard"},
    {"id": "quant_only", "name": "Quant Practice Test", "type": "section", "company": "",
     "duration": 30, "questions": 25, "sections": ["Quantitative Aptitude"],
     "difficulty": "Mixed"},
    {"id": "reasoning_only", "name": "Reasoning Practice Test", "type": "section", "company": "",
     "duration": 25, "questions": 20, "sections": ["Logical Reasoning"],
     "difficulty": "Mixed"},
    {"id": "verbal_only", "name": "Verbal Practice Test", "type": "section", "company": "",
     "duration": 20, "questions": 20, "sections": ["Verbal Ability"],
     "difficulty": "Mixed"},
]


@app.get("/mock-tests", response_class=HTMLResponse)
async def mock_tests_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    test_history = get_mock_test_history(user["id"])
    best_scores = {}
    for t in test_history:
        key = t.get("test_type", "") + "_" + t.get("company", "")
        score = round(t["score"] * 100)
        if key not in best_scores or score > best_scores[key]:
            best_scores[key] = score

    for test in MOCK_TEST_CATALOG:
        key = test["type"] + "_" + test["company"]
        test["best_score"] = best_scores.get(key)

    return render(request, "mock_tests.html", {
        "user": user, "active_page": "mock_tests",
        "mode": "select",
        "available_tests": MOCK_TEST_CATALOG,
        "test_history": [{
            "test_name": t.get("test_type", "Test"),
            "company": t.get("company", ""),
            "score": round(t["score"] * 100),
            "date": (t.get("completed_at") or "")[:10],
            "questions": t["total_questions"],
        } for t in test_history[:10]],
    })


@app.post("/mock-tests/start", response_class=HTMLResponse)
async def mock_test_start(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    form = await request.form()
    test_id = form.get("test_id", "full_placement")
    test_info = next((t for t in MOCK_TEST_CATALOG if t["id"] == test_id), MOCK_TEST_CATALOG[0])

    question_count = min(test_info["questions"], 25)

    section_topics = {
        "Quant": list(range(0, 12)), "Quantitative Aptitude": list(range(0, 12)),
        "Reasoning": list(range(12, 20)), "Logical Reasoning": list(range(12, 20)),
        "Verbal": list(range(20, 27)), "Verbal Ability": list(range(20, 27)),
        "Technical": list(range(31, 40)), "Programming": list(range(31, 40)),
        "Coding": list(range(37, 40)), "Coding (2)": list(range(40, 52)),
        "Coding (3)": list(range(40, 52)), "Cognitive": list(range(0, 20)),
        "Puzzle": list(range(12, 20)), "Aptitude": list(range(0, 20)),
        "Workstyle Assessment": [],
    }

    import random as _rand
    all_questions = []
    questions_per_section = max(1, question_count // max(len(test_info["sections"]), 1))

    for section_name in test_info["sections"]:
        topic_ids = section_topics.get(section_name, list(range(0, 12)))
        if not topic_ids:
            continue
        for _ in range(questions_per_section):
            tid = _rand.choice(topic_ids)
            section_qs = _fallback_quiz_questions(tid, 1)
            for q in section_qs:
                q["section"] = section_name
                q["topic_id"] = tid
            all_questions.extend(section_qs)

    all_questions = _sanitize_quiz_questions(all_questions, desired_count=min(question_count, 25))
    questions, question_data_json = _serialize_quiz_questions(all_questions)

    return render(request, "mock_tests.html", {
        "user": user, "active_page": "mock_tests",
        "mode": "active",
        "test_name": test_info["name"],
        "test_id": test_id,
        "test_type": test_info["type"],
        "company": test_info["company"],
        "questions": questions,
        "question_data_json": question_data_json,
        "sections": test_info["sections"],
        "duration_mins": test_info["duration"],
    })


@app.post("/mock-tests/submit", response_class=HTMLResponse)
async def mock_test_submit(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    form = await request.form()
    test_type = form.get("test_type", "full")
    company = form.get("company", "")
    time_taken = int(form.get("time_taken", 0))
    question_data = json.loads(form.get("question_data", "[]"))

    answers = []
    for i in range(len(question_data)):
        ans = form.get(f"answer_{i}")
        answers.append(int(ans) if ans is not None else -1)

    correct_count = 0
    results = []
    section_correct = {}
    section_total = {}
    for i, q in enumerate(question_data):
        user_ans = answers[i] if i < len(answers) else -1
        is_correct = user_ans == q["correct"]
        if is_correct:
            correct_count += 1
        section = q.get("section", "General")
        section_total[section] = section_total.get(section, 0) + 1
        if is_correct:
            section_correct[section] = section_correct.get(section, 0) + 1
        results.append({
            "question": q["question"],
            "your_answer": q["options"][user_ans] if 0 <= user_ans < 4 else "No answer",
            "correct_answer": q["options"][q["correct"]],
            "is_correct": is_correct,
            "explanation": q.get("explanation", ""),
            "section": section,
        })

    total = len(question_data)
    score = correct_count / max(total, 1)
    score_pct = round(score * 100)

    section_scores = {}
    for sec in section_total:
        sec_total = section_total[sec]
        sec_correct = section_correct.get(sec, 0)
        section_scores[sec] = {"correct": sec_correct, "total": sec_total,
                               "pct": round(sec_correct / max(sec_total, 1) * 100)}

    weaknesses = [s for s, d in section_scores.items() if d["pct"] < 50]
    strengths = [s for s, d in section_scores.items() if d["pct"] >= 70]

    record_mock_test(user["id"], test_type, company, total, correct_count,
                     score, time_taken, json.dumps(section_scores), json.dumps(results))

    return render(request, "mock_tests.html", {
        "user": user, "active_page": "mock_tests",
        "mode": "results",
        "test_type": test_type, "company": company,
        "score_pct": score_pct, "correct": correct_count, "total": total,
        "results": results, "section_scores": section_scores,
        "weaknesses": weaknesses, "strengths": strengths, "time_taken": time_taken,
    })


#  DAILY PLANNER PAGE 

@app.get("/daily-planner", response_class=HTMLResponse)
async def daily_planner_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)

    from datetime import datetime, timedelta
    import calendar as cal_mod  # for monthly streak calendar

    # Support ?date=YYYY-MM-DD to view a specific day; default to today
    real_today = datetime.utcnow().strftime("%Y-%m-%d")
    selected_date = request.query_params.get("date", "").strip()
    # Validate date format
    if selected_date:
        try:
            datetime.strptime(selected_date, "%Y-%m-%d")
        except ValueError:
            selected_date = real_today
    else:
        selected_date = real_today

    # Parse selected date to compute its week
    sel_dt = datetime.strptime(selected_date, "%Y-%m-%d")

    # Get tasks for the selected day
    selected_tasks = get_daily_tasks(user["id"], selected_date)
    for t in selected_tasks:
        t["topic_name"] = TOPIC_DISPLAY_NAMES.get(t.get("topic_id"), "") if t.get("topic_id") is not None else ""

    # Build week calendar around the selected date's week (Mon-Sun)
    start = sel_dt - timedelta(days=sel_dt.weekday())
    week_data = {}
    for i in range(7):
        d = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        day_tasks = get_daily_tasks(user["id"], d)
        for t in day_tasks:
            t["topic_name"] = TOPIC_DISPLAY_NAMES.get(t.get("topic_id"), "") if t.get("topic_id") is not None else ""
        week_data[d] = day_tasks

    streak = 0
    check_date = datetime.utcnow() - timedelta(days=1)
    for _ in range(365):
        d = check_date.strftime("%Y-%m-%d")
        day_tasks = get_daily_tasks(user["id"], d)
        if day_tasks and all(t["is_completed"] for t in day_tasks):
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break

    week_tasks = [t for tasks in week_data.values() for t in tasks]
    tasks_completed = sum(1 for t in week_tasks if t["is_completed"])
    total_hours = round(sum(t["duration_mins"] for t in week_tasks if t["is_completed"]) / 60, 1)

    progress = get_user_progress(user["id"])
    mastery_dict = {(int(r["topic_id"]) if isinstance(r["topic_id"], str) else r["topic_id"]): r["mastery_level"] for r in progress}
    weak_topics = sorted(
        [{"id": tid, "display_name": TOPIC_DISPLAY_NAMES.get(tid, ""), "mastery": round(m * 100)}
         for tid, m in mastery_dict.items() if 0 < m < 0.5],
        key=lambda x: x["mastery"]
    )[:8]

    topic_options = [{"id": tid, "display_name": TOPIC_DISPLAY_NAMES[tid]} for tid in sorted(TOPIC_DISPLAY_NAMES.keys())]

    # Whether the selected date is in the past (read-only mode)
    is_past = selected_date < real_today

    # Build monthly streak calendar for the sidebar
    sel_year, sel_month = sel_dt.year, sel_dt.month
    first_weekday, days_in_month = cal_mod.monthrange(sel_year, sel_month)  # first_weekday: 0=Mon
    month_streak_data = []
    for day_num in range(1, days_in_month + 1):
        day_str = f"{sel_year}-{sel_month:02d}-{day_num:02d}"
        if day_str > real_today:
            month_streak_data.append({"day": day_num, "date": day_str, "status": "future"})
        else:
            day_t = get_daily_tasks(user["id"], day_str)
            if not day_t:
                month_streak_data.append({"day": day_num, "date": day_str, "status": "none"})
            elif all(t["is_completed"] for t in day_t):
                month_streak_data.append({"day": day_num, "date": day_str, "status": "completed"})
            else:
                month_streak_data.append({"day": day_num, "date": day_str, "status": "partial"})

    month_name = sel_dt.strftime("%B %Y")

    return render(request, "daily_planner.html", {
        "user": user, "active_page": "daily_planner",
        "today": selected_date, "real_today": real_today,
        "today_tasks": selected_tasks, "week_data": week_data,
        "streak": streak, "is_past": is_past,
        "weekly_stats": {"total_hours": total_hours, "tasks_completed": tasks_completed, "tasks_total": len(week_tasks)},
        "weak_topics": weak_topics, "topic_options": topic_options,
        "month_name": month_name, "month_streak_data": month_streak_data,
        "month_first_weekday": first_weekday,
    })


@app.post("/api/planner/add")
async def planner_add_task(request: Request):
    user = get_current_user(request)
    if not user:
        return JSONResponse({"error": "Not authenticated"}, status_code=401)
    body = await request.json()
    task = add_daily_task(user["id"], body.get("task_date", ""), body.get("task_type", "study"),
                          int(body.get("topic_id", 0)), body.get("description", ""), int(body.get("duration_mins", 30)))
    task["topic_name"] = TOPIC_DISPLAY_NAMES.get(task.get("topic_id"), "")
    return JSONResponse({"task": task})


@app.post("/api/planner/complete")
async def planner_complete_task(request: Request):
    user = get_current_user(request)
    if not user:
        return JSONResponse({"error": "Not authenticated"}, status_code=401)
    body = await request.json()
    complete_daily_task(int(body.get("task_id", 0)))
    return JSONResponse({"ok": True})


@app.post("/api/planner/delete")
async def planner_delete_task(request: Request):
    user = get_current_user(request)
    if not user:
        return JSONResponse({"error": "Not authenticated"}, status_code=401)
    body = await request.json()
    delete_daily_task(int(body.get("task_id", 0)))
    return JSONResponse({"ok": True})


#  INTERVIEW SIMULATOR PAGE 

INTERVIEW_QUESTIONS = {
    "technical": {
        "TCS": [
            {"q": "What is the difference between an array and a linked list?", "ideal": "Arrays store elements in contiguous memory with O(1) random access but O(n) insertion/deletion. Linked lists use nodes with pointers, giving O(1) insertion/deletion at known positions but O(n) access.", "type": "DSA"},
            {"q": "Explain the concept of normalization in DBMS.", "ideal": "Normalization reduces data redundancy by organizing data into related tables. 1NF: atomic values. 2NF: no partial dependencies. 3NF: no transitive dependencies. BCNF: every determinant is a candidate key.", "type": "DBMS"},
            {"q": "What is a deadlock? How can it be prevented?", "ideal": "Deadlock occurs when processes wait indefinitely for resources held by each other. Four conditions: mutual exclusion, hold and wait, no preemption, circular wait. Prevention: break any one condition.", "type": "OS"},
            {"q": "Write a function to reverse a linked list.", "ideal": "Use three pointers: prev=null, current=head, next. While current: next=current.next, current.next=prev, prev=current, current=next. Return prev. Time O(n), Space O(1).", "type": "Coding"},
            {"q": "Explain TCP vs UDP with examples.", "ideal": "TCP: connection-oriented, reliable, ordered (HTTP, FTP). UDP: connectionless, faster, unreliable (streaming, DNS, gaming). TCP uses 3-way handshake.", "type": "CN"},
        ],
        "Amazon": [
            {"q": "Design a system to find the k-th largest element in a stream.", "ideal": "Use a min-heap of size k. For each new element, if larger than top, remove top and insert. Top = k-th largest. Time: O(n log k).", "type": "DSA"},
            {"q": "How would you design a URL shortening service?", "ideal": "Base62 encoding of auto-increment ID or hash. Store in DB + cache (Redis). Handle collisions. Scale with sharding.", "type": "System Design"},
            {"q": "Implement an LRU Cache with O(1) operations.", "ideal": "HashMap + Doubly Linked List. HashMap maps key to node. DLL maintains order. Get: move to front. Put: add to front, evict from tail. Both O(1).", "type": "DSA"},
        ],
        "Microsoft": [
            {"q": "Given a binary tree, serialize and deserialize it.", "ideal": "Serialize: preorder traversal with null markers. Deserialize: reconstruct using queue/recursion. Preorder + null markers uniquely defines a tree.", "type": "DSA"},
            {"q": "Explain the SOLID principles with examples.", "ideal": "S: Single Responsibility. O: Open/Closed. L: Liskov Substitution. I: Interface Segregation. D: Dependency Inversion.", "type": "OOP"},
        ],
        "Generic": [
            {"q": "What is the time complexity of common sorting algorithms?", "ideal": "Bubble/Selection/Insertion: O(n^2). Merge: O(n log n). Quick: O(n log n) avg, O(n^2) worst. Heap: O(n log n).", "type": "DSA"},
            {"q": "Explain process vs thread.", "ideal": "Process: independent with own memory. Thread: lightweight, shares memory within process. Context switching faster for threads.", "type": "OS"},
            {"q": "What is indexing in databases?", "ideal": "Index (B-tree) speeds retrieval from O(n) to O(log n). Trade-off: faster reads, slower writes, extra storage.", "type": "DBMS"},
        ],
    },
    "hr": {
        "Generic": [
            {"q": "Tell me about yourself.", "ideal": "Structure: Present -> Past -> Future. 2 minutes max. Focus on achievements.", "type": "HR"},
            {"q": "Why do you want to join our company?", "ideal": "Research company values/products. Connect your skills to their needs. Show genuine interest.", "type": "HR"},
            {"q": "What is your greatest weakness?", "ideal": "Genuine but non-critical weakness. Show self-awareness and concrete improvement steps.", "type": "HR"},
            {"q": "Where do you see yourself in 5 years?", "ideal": "Show ambition aligned with company growth. Mention skill development and leadership goals.", "type": "HR"},
            {"q": "Describe a challenging situation.", "ideal": "STAR method: Situation, Task, Action, Result. Relevant example with measurable outcomes.", "type": "Behavioral"},
        ],
    },
    "behavioral": {
        "Amazon": [
            {"q": "Tell me about a time you had to make a decision with incomplete data. (Bias for Action)", "ideal": "STAR format. Show calculated risk-taking. Explain decision framework and outcome.", "type": "LP"},
            {"q": "Give an example when you went above and beyond for a customer. (Customer Obsession)", "ideal": "Describe customer need, extra effort, and quantified impact.", "type": "LP"},
            {"q": "Describe a time you simplified a complex process. (Invent and Simplify)", "ideal": "Explain original complexity, analytical approach, simplified solution, measured improvement.", "type": "LP"},
        ],
        "Generic": [
            {"q": "Tell me about a time you worked in a team.", "ideal": "STAR method. Show collaboration, your contribution, and team outcome.", "type": "Behavioral"},
            {"q": "How do you handle pressure and tight deadlines?", "ideal": "Specific example with prioritization and time management techniques.", "type": "Behavioral"},
        ],
    },
}


@app.get("/interview-sim", response_class=HTMLResponse)
async def interview_sim_page(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    interview_hist = get_interview_history(user["id"])
    return render(request, "interview_sim.html", {
        "user": user, "active_page": "interview_sim",
        "mode": "setup",
        "companies": ["TCS", "Infosys", "Wipro", "Accenture", "Amazon", "Microsoft", "Generic"],
        "interview_history": [{"company": s.get("company", ""), "round_type": s.get("round_type", ""),
                               "score": round(s.get("score", 0) * 100), "date": (s.get("completed_at") or "")[:10]}
                              for s in interview_hist[:10]],
    })


@app.post("/interview-sim/start", response_class=HTMLResponse)
async def interview_sim_start(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    form = await request.form()
    company = form.get("company", "Generic")
    round_type = form.get("round_type", "technical")
    duration = int(form.get("duration", 30))

    import random as _rand
    pool = INTERVIEW_QUESTIONS.get(round_type, {}).get(company, [])
    if not pool:
        pool = INTERVIEW_QUESTIONS.get(round_type, {}).get("Generic", [])
    if not pool:
        pool = INTERVIEW_QUESTIONS["technical"]["Generic"]

    question_count = min(len(pool), max(3, duration // 5))
    selected = _rand.sample(pool, min(question_count, len(pool)))
    questions_for_template = [{"idx": i, "question": q["q"], "type": q.get("type", "General"),
                               "ideal_answer": q["ideal"]} for i, q in enumerate(selected)]

    return render(request, "interview_sim.html", {
        "user": user, "active_page": "interview_sim", "mode": "active",
        "company": company, "round_type": round_type,
        "questions": questions_for_template,
        "question_data_json": json.dumps(questions_for_template),
        "duration_mins": duration,
    })


@app.post("/interview-sim/submit", response_class=HTMLResponse)
async def interview_sim_submit(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse("/login", status_code=302)
    form = await request.form()
    company = form.get("company", "Generic")
    round_type = form.get("round_type", "technical")
    question_data = json.loads(form.get("question_data", "[]"))

    results = []
    total_score = 0
    for i, q in enumerate(question_data):
        user_answer = form.get(f"answer_{i}", "").strip()
        ideal = q.get("ideal_answer", "")
        if not user_answer:
            q_score = 0
        else:
            ideal_words = set(ideal.lower().split())
            user_words = set(user_answer.lower().split())
            overlap = len(ideal_words & user_words)
            q_score = min(1.0, overlap / max(len(ideal_words) * 0.3, 1))
        total_score += q_score
        results.append({"question": q["question"], "your_answer": user_answer or "(No answer)",
                        "ideal_answer": ideal, "score": round(q_score * 100), "type": q.get("type", "General")})

    avg_score = total_score / max(len(question_data), 1)
    score_pct = round(avg_score * 100)
    grade = "A" if score_pct >= 80 else "B" if score_pct >= 60 else "C" if score_pct >= 40 else "D"

    if score_pct >= 80:
        feedback = "Excellent! Strong knowledge and communication skills demonstrated."
    elif score_pct >= 60:
        feedback = "Good attempt. Add more specific examples and technical depth."
    elif score_pct >= 40:
        feedback = "Needs improvement. Review core concepts and practice STAR method answers."
    else:
        feedback = "Significant preparation needed. Start with fundamentals and practice answering aloud."

    tips = {"technical": ["Think aloud during the interview", "Ask clarifying questions first",
                          "Discuss time/space complexity", "Start brute force, then optimize"],
            "hr": ["Use STAR method", "Research the company", "Prepare 5-6 stories", "Keep answers to 2-3 minutes"],
            "behavioral": ["Include measurable results", "Be specific, not generic",
                           "Map answers to Leadership Principles for Amazon", "Practice with a timer"]
            }.get(round_type, [])

    record_interview_session(user["id"], company, round_type,
                            json.dumps([q["question"] for q in question_data]),
                            json.dumps([r["your_answer"] for r in results]), avg_score, feedback)

    return render(request, "interview_sim.html", {
        "user": user, "active_page": "interview_sim", "mode": "results",
        "company": company, "round_type": round_type, "score": score_pct,
        "grade": grade, "results": results, "feedback": feedback, "tips": tips,
    })


#  SIMULATION PAGE (OpenENV Live Runner) 

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


# """ SEARCH ENDPOINT """

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
        {"name": "DSA Roadmap", "url": "/dsa-roadmap", "keywords": "dsa data structures algorithms roadmap problems patterns"},
        {"name": "Company Prep", "url": "/company-prep", "keywords": "company tcs infosys wipro accenture amazon microsoft placement"},
        {"name": "Mock Tests", "url": "/mock-tests", "keywords": "mock test full length placement exam practice"},
        {"name": "Daily Planner", "url": "/daily-planner", "keywords": "daily planner schedule study plan tasks"},
        {"name": "Interview Simulator", "url": "/interview-sim", "keywords": "interview simulator mock hr technical behavioral"},
        {"name": "AI Simulation", "url": "/simulation", "keywords": "simulation ai reinforcement learning"},
        {"name": "Profile", "url": "/profile", "keywords": "profile account settings"},
        {"name": "API Explorer", "url": "/api-explorer", "keywords": "api explorer endpoints"},
    ]
    for page in pages:
        if query in page["name"].lower() or query in page["keywords"]:
            results.append({"type": "page", "name": page["name"], "url": page["url"]})

    return JSONResponse({"results": results[:15]})


#  AI SUPPORT CHAT ENDPOINT 

@app.post("/api/ai/chat")
async def ai_support_chat(request: Request, payload: AIChatRequest):
    try:
        user = get_current_user(request)
        message = (payload.message or "").strip()
        if len(message) < 2:
            return JSONResponse({"error": "Message is too short"}, status_code=400)

        user_context = "No authenticated user context."
        if user:
            try:
                progress = get_user_progress(user["id"])
            except Exception:
                progress = []
            try:
                quiz_hist = get_quiz_history(user["id"])
            except Exception:
                quiz_hist = []

            topics_mastered = sum(1 for row in progress if row.get("mastery_level", 0) >= MASTERY_THRESHOLD)
            avg_quiz = round(sum(q.get("score", 0) for q in quiz_hist) / max(len(quiz_hist), 1) * 100)
            user_context = (
                f"Name: {user.get('name', 'Learner')}. "
                f"Topics mastered: {topics_mastered}/{NUM_TOPICS}. "
                f"Total quizzes attempted: {len(quiz_hist)}. "
                f"Average quiz score: {avg_quiz}%."
            )

        try:
            reply = await generate_support_chat_reply(
                message, user_context=user_context, history=payload.history
            )
            reply = (reply or "").strip()
            if not reply:
                raise ValueError("Empty reply from AI model")
            return JSONResponse({
                "reply": reply,
                "model": HF_CHAT_MODEL,
                "source": "huggingface",
            })
        except Exception as e:
            logger.error(f"AI chat failed: {e}")
            fallback = _local_support_chat_reply(message, user_context=user_context)
            return JSONResponse({
                "reply": fallback,
                "model": "fallback",
                "source": "local",
            })
    except Exception as e:
        logger.error(f"AI chat endpoint error: {e}")
        fallback_msg = "Please ask your question again."
        try:
            fallback_msg = _local_support_chat_reply(getattr(payload, "message", "") or "")
        except Exception:
            pass
        return JSONResponse({
            "reply": fallback_msg,
            "model": "fallback",
            "source": "local",
        })


# """ OPENENV CORE API ENDPOINTS """

class PredictRequest(BaseModel):
    input_data: str | dict | None = None
    action: dict | None = None
    command: str | None = None

class ResetRequest(BaseModel):
    archetype: str | None = None
    seed: int | None = None

class ActionRequest(BaseModel):
    action: dict


@app.post("/predict")
@app.post("/api/predict")
async def predict_endpoint(req: PredictRequest = None):
    """
    OpenENV-compatible predict endpoint.

    Accepts:
      - {"command": "reset"}                              -> reset env
      - {"command": "state"}                              -> get state
      - {"command": "spec"}                               -> get spec
      - {"action": {"topic": 0, "difficulty": 2, ...}}    -> explicit step
      - {"input_data": "reset"} or {"input_data": {...}}  -> flexible input
      - Empty body / no action                            -> agent-recommended step

    Returns JSON with status, observation, reward, and human-readable fields.
    """
    async with env_lock:
        try:
            # Parse the incoming request into a command or action
            command = None
            action = None

            if req is not None:
                command = req.command
                action = req.action

                # Handle input_data (string or dict)
                if req.input_data is not None and command is None and action is None:
                    if isinstance(req.input_data, str):
                        text = req.input_data.strip().lower()
                        if text in ("reset", "state", "spec", "step", "auto", "next"):
                            command = text
                        else:
                            # Try parsing as JSON action
                            try:
                                import json as _json
                                action = _json.loads(req.input_data)
                            except (ValueError, TypeError):
                                command = "step"  # default to agent step
                    elif isinstance(req.input_data, dict):
                        action = req.input_data

            # Default: agent-recommended step
            if command is None and action is None:
                command = "step"

            # --- RESET ---
            if command == "reset":
                obs, info = env.reset()
                obs_json = obs_to_json(obs)
                return {
                    "observation": f"Environment reset. Student archetype: {info.get('student_archetype', 'unknown')}. "
                                   f"Topics: {NUM_TOPICS}. Mastered: {info.get('topics_mastered', 0)}. "
                                   f"Completion: {info.get('completion_rate', 0.0):.2f}. Engagement: {float(obs_json.get('engagement', [0.8])[0]):.2f}.",
                    "reward": 0.0,
                    "done": False,
                    "info": info,
                }

            # --- STATE ---
            if command == "state":
                state = env.state()
                return {
                    "observation": f"Current state: step {state.get('step', 0)}, "
                                   f"mastered {state.get('topics_mastered', 0)}/{NUM_TOPICS} topics, "
                                   f"completion {state.get('completion_rate', 0.0):.2f}.",
                    "reward": 0.0,
                    "done": False,
                    "info": state,
                }

            # --- SPEC ---
            if command == "spec":
                spec_path = BASE_DIR / "openenv_spec.json"
                spec_data = json.loads(spec_path.read_text()) if spec_path.exists() else {"name": "CurriculumFlowENV"}
                return {
                    "observation": f"Spec: {spec_data.get('name', 'CurriculumFlowENV')} - {spec_data.get('description', '')}",
                    "reward": 0.0,
                    "done": False,
                    "info": spec_data,
                }

            # --- STEP (explicit action or agent-recommended) ---
            if action is None:
                # Agent-recommended action
                obs_raw = env._get_obs()
                info_raw = env.state()
                obs_dict = {k: v.tolist() if hasattr(v, 'tolist') else v for k, v in obs_raw.items()}
                topic = env.sequencer.select_action(obs_dict, info_raw)
                diff = env.difficulty_agent.select_action(obs_dict, info_raw)
                assess = env.assessment_agent.select_action(obs_dict, info_raw)
                action = {"topic": int(topic), "difficulty": int(diff), "assess": int(assess)}

            obs, reward, terminated, truncated, info = env.step(action)
            obs_json = obs_to_json(obs)
            done = terminated or truncated

            return {
                "observation": f"Step {info.get('step', 0)}: topic={info.get('topic_name', 'unknown')}, "
                               f"difficulty={info.get('difficulty', 0)}, reward={float(reward):.4f}, "
                               f"mastered={info.get('topics_mastered', 0)}/{NUM_TOPICS}, "
                               f"completion={info.get('completion_rate', 0.0):.2f}, "
                               f"engagement={float(obs_json.get('engagement', [0.0])[0]):.2f}.",
                "reward": float(reward),
                "done": done,
                "info": info,
            }

        except Exception as e:
            logger.error(f"/predict error: {e}")
            return JSONResponse(
                status_code=500,
                content={"status": "error", "error": str(e)},
            )


@app.post("/api/reset")
@app.post("/reset")
async def api_reset(req: ResetRequest = None):
    async with env_lock:
        options = {"archetype": req.archetype} if req and req.archetype else None
        seed = req.seed if req else None
        obs, info = env.reset(seed=seed, options=options)
        obs_json = obs_to_json(obs)
        return {
            "observation": f"Environment reset. Student archetype: {info.get('student_archetype', 'unknown')}. "
                           f"Topics: {NUM_TOPICS}. Mastered: {info.get('topics_mastered', 0)}. "
                           f"Completion: {info.get('completion_rate', 0.0):.2f}. "
                           f"Engagement: {float(obs_json.get('engagement', [0.8])[0]):.2f}.",
            "reward": 0.0,
            "done": False,
            "info": info,
        }

@app.post("/api/step")
@app.post("/step")
async def api_step(req: ActionRequest):
    async with env_lock:
        obs, reward, terminated, truncated, info = env.step(req.action)
        obs_json = obs_to_json(obs)
        done = terminated or truncated
        return {
            "observation": f"Step {info.get('step', 0)}: topic={info.get('topic_name', 'unknown')}, "
                           f"difficulty={info.get('difficulty', 0)}, reward={float(reward):.4f}, "
                           f"mastered={info.get('topics_mastered', 0)}/{NUM_TOPICS}, "
                           f"engagement={float(obs_json.get('engagement', [0.0])[0]):.2f}.",
            "reward": float(reward),
            "done": done,
            "info": info,
        }

@app.get("/api/state")
@app.get("/state")
async def api_state():
    async with env_lock:
        state = env.state()
        return {
            "observation": f"State: step {state.get('step', 0)}, "
                           f"mastered {state.get('topics_mastered', 0)}/{NUM_TOPICS}, "
                           f"completion {state.get('completion_rate', 0.0):.2f}.",
            "reward": 0.0,
            "done": False,
            "info": state,
        }

@app.get("/health")
async def health():
    import os
    from curriculum_flow_env.database import DB_PATH, get_connection
    db_info = {"path": str(DB_PATH), "exists": DB_PATH.exists()}
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as cnt FROM users")
        db_info["user_count"] = cursor.fetchone()["cnt"]
        conn.close()
    except Exception as e:
        db_info["error"] = str(e)
    return {
        "status": "healthy", "env": "CurriculumFlowENV", "version": "0.1.0",
        "step": env.step_count, "db": db_info,
        "space_id": os.getenv("SPACE_ID", "local"),
    }

@app.get("/spec")
async def get_spec():
    spec_path = BASE_DIR / "openenv_spec.json"
    if spec_path.exists():
        return json.loads(spec_path.read_text())
    return {"error": "spec not found"}

@app.get("/metadata")
async def get_metadata():
    return {
        "name": "CurriculumFlowENV",
        "description": "Multi-agent RL for adaptive learning path optimization. Three agents jointly personalize education for simulated students with Ebbinghaus forgetting curves.",
        "version": "0.1.0",
        "authors": ["krithickvivek"],
        "license": "Apache-2.0",
    }

@app.get("/schema")
async def get_schema():
    return {
        "topic_selection": {
            "description": "Select the optimal next topic for the student based on mastery levels, forgetting curves, and prerequisite dependencies.",
            "parameters": {
                "topic": {"type": "integer", "min": 0, "max": 65, "description": "Topic index from the 66-topic curriculum graph"},
            },
            "evaluation_criteria": {
                "mastery_gain": "Improvement in student mastery across all topics (0.0-1.0)",
                "prerequisite_respect": "Whether selected topics follow prerequisite ordering",
                "engagement_maintenance": "Student engagement stays above 0.5 threshold",
            },
        },
        "difficulty_adaptation": {
            "description": "Adapt the difficulty level of the current topic to match the student's zone of proximal development.",
            "parameters": {
                "difficulty": {"type": "integer", "min": 0, "max": 4, "description": "Difficulty level: 0=easy, 1=medium, 2=hard, 3=advanced, 4=expert"},
            },
            "evaluation_criteria": {
                "accuracy_rate": "Student accuracy remains in 0.6-0.9 optimal range",
                "difficulty_progression": "Difficulty increases as mastery improves",
                "no_frustration": "Difficulty does not exceed student capability causing engagement drop",
            },
        },
        "assessment_timing": {
            "description": "Decide whether to assess the student on the current topic based on Ebbinghaus forgetting curve timing.",
            "parameters": {
                "assess": {"type": "integer", "min": 0, "max": 1, "description": "0=skip assessment, 1=assess now"},
            },
            "evaluation_criteria": {
                "retention_optimization": "Assessments timed to maximize long-term retention via spaced repetition",
                "completion_rate": "Overall curriculum completion rate (0.0-1.0)",
                "mastery_threshold": "Topics reach mastery threshold of 0.8 before moving on",
            },
        },
    }


# """ OPENENV WEBSOCKET ENDPOINT """

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """OpenEnv WebSocket endpoint — each connection gets an isolated env instance."""
    from curriculum_flow_env.env import CurriculumFlowEnv

    await websocket.accept()
    ws_env = CurriculumFlowEnv(archetype="steady", max_steps=200)
    logger.info("WebSocket session opened")

    try:
        while True:
            data = await websocket.receive_json()
            msg_type = data.get("type", "")

            if msg_type == "reset":
                seed = data.get("seed")
                archetype = data.get("archetype")
                options = {"archetype": archetype} if archetype else None
                obs, info = ws_env.reset(seed=seed, options=options)
                await websocket.send_json({
                    "type": "reset",
                    "observation": obs_to_json(obs),
                    "info": info,
                })

            elif msg_type == "step":
                action = data.get("action", {})
                obs, reward, terminated, truncated, info = ws_env.step(action)
                await websocket.send_json({
                    "type": "step",
                    "observation": obs_to_json(obs),
                    "reward": float(reward),
                    "terminated": terminated,
                    "truncated": truncated,
                    "done": terminated or truncated,
                    "info": info,
                })

            elif msg_type == "state":
                await websocket.send_json({
                    "type": "state",
                    "state": ws_env.state(),
                })

            else:
                await websocket.send_json({
                    "type": "error",
                    "message": f"Unknown message type: {msg_type}",
                })

    except WebSocketDisconnect:
        logger.info("WebSocket session closed")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        try:
            await websocket.close()
        except Exception:
            pass


# """ OPENENV-POWERED RECOMMENDATION ENDPOINTS """

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

    sequencer_reason = f"Selected '{topic_name}' - lowest mastery ({topic_mastery:.0%}) among {len(unlocked)} unlocked topics"
    difficulty_reason = f"Difficulty {diff_rec}/5 - matched to your current mastery level (Zone of Proximal Development)"
    assess_reason = "Assessment recommended - time to validate your knowledge" if assess_rec == 1 else "Continue practicing - build more confidence before testing"

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
    """Single step through the global OpenENV instance " for interactive mode."""
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

