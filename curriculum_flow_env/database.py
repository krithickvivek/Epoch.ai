"""
CurriculumFlowENV Database Module
SQLite database for user management, progress tracking, quiz attempts, and learning sessions.
"""

import sqlite3
import hashlib
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List, Any

# Database path — use HF Spaces persistent storage if available, else project-local
PROJECT_ROOT = Path(__file__).resolve().parent.parent
_HF_PERSISTENT = Path("/data")
if os.getenv("SPACE_ID") and _HF_PERSISTENT.exists():
    DB_DIR = _HF_PERSISTENT
else:
    DB_DIR = PROJECT_ROOT / "data"
DB_PATH = DB_DIR / "mindmatrix.db"

SALT = "mindmatrix_salt_"


def _hash_password(password: str) -> str:
    """Hash a password using SHA-256 with salt."""
    return hashlib.sha256(f"{SALT}{password}".encode()).hexdigest()


def get_connection() -> sqlite3.Connection:
    """Get a database connection with row_factory set."""
    conn = sqlite3.connect(str(DB_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def init_db() -> None:
    """Create all tables if they do not exist."""
    DB_DIR.mkdir(parents=True, exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT NOT NULL,
            role TEXT DEFAULT 'student',
            experience_level TEXT DEFAULT 'beginner',
            organization TEXT DEFAULT '',
            bio TEXT DEFAULT '',
            profile_pic TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id TEXT NOT NULL,
            mastery_level REAL DEFAULT 0.0 CHECK(mastery_level >= 0.0 AND mastery_level <= 1.0),
            time_spent INTEGER DEFAULT 0,
            last_practiced TEXT DEFAULT (datetime('now')),
            attempts INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id)
        );

        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id TEXT NOT NULL,
            score REAL DEFAULT 0.0 CHECK(score >= 0.0 AND score <= 1.0),
            total_questions INTEGER DEFAULT 0,
            correct_answers INTEGER DEFAULT 0,
            attempted_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS chapter_passes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            chapter_num INTEGER NOT NULL,
            score REAL DEFAULT 0.0,
            passed_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id, chapter_num)
        );

        CREATE TABLE IF NOT EXISTS learning_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            started_at TEXT DEFAULT (datetime('now')),
            ended_at TEXT,
            topics_studied TEXT DEFAULT '[]',
            engagement_avg REAL DEFAULT 0.0,
            reward_total REAL DEFAULT 0.0,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS mock_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            test_type TEXT NOT NULL DEFAULT 'full',
            company TEXT DEFAULT '',
            total_questions INTEGER DEFAULT 0,
            correct_answers INTEGER DEFAULT 0,
            score REAL DEFAULT 0.0,
            time_taken INTEGER DEFAULT 0,
            section_scores TEXT DEFAULT '{}',
            started_at TEXT DEFAULT (datetime('now')),
            completed_at TEXT,
            results_json TEXT DEFAULT '[]',
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS daily_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_date TEXT NOT NULL,
            task_type TEXT NOT NULL DEFAULT 'study',
            topic_id INTEGER,
            description TEXT DEFAULT '',
            duration_mins INTEGER DEFAULT 30,
            is_completed INTEGER DEFAULT 0,
            completed_at TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            chapter_num INTEGER DEFAULT 0,
            note TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id, chapter_num)
        );

        CREATE TABLE IF NOT EXISTS interview_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            company TEXT DEFAULT '',
            round_type TEXT DEFAULT 'technical',
            questions_json TEXT DEFAULT '[]',
            responses_json TEXT DEFAULT '[]',
            score REAL DEFAULT 0.0,
            feedback TEXT DEFAULT '',
            completed_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()


def seed_test_user() -> None:
    """Create a default test user if it does not already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", ("testuser1@gmail.com",))
    if cursor.fetchone() is None:
        cursor.execute(
            """INSERT INTO users (email, password_hash, name, role, experience_level)
               VALUES (?, ?, ?, ?, ?)""",
            (
                "testuser1@gmail.com",
                _hash_password("testuser1"),
                "Test User",
                "student",
                "beginner",
            ),
        )
        conn.commit()

    conn.close()


# ---------------------------------------------------------------------------
# CRUD Functions
# ---------------------------------------------------------------------------

def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Retrieve a user by email address. Returns dict or None."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None


def create_user(
    email: str,
    password: str,
    name: str,
    role: str = "student",
    experience_level: str = "beginner",
    organization: str = "",
    bio: str = "",
    profile_pic: str = "",
) -> Dict[str, Any]:
    """Create a new user and return the user dict."""
    conn = get_connection()
    cursor = conn.cursor()
    password_hash = _hash_password(password)

    cursor.execute(
        """INSERT INTO users (email, password_hash, name, role, experience_level,
                              organization, bio, profile_pic)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (email, password_hash, name, role, experience_level, organization, bio, profile_pic),
    )
    conn.commit()
    user_id = cursor.lastrowid

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def verify_password(email: str, password: str) -> Optional[Dict[str, Any]]:
    """Verify credentials. Returns user dict on success, None on failure."""
    user = get_user_by_email(email)
    if user is None:
        return None
    if user["password_hash"] == _hash_password(password):
        return user
    return None


def update_user(user_id: int, **kwargs) -> Dict[str, Any]:
    """Update user fields. Accepts name, role, experience_level, organization, bio, profile_pic."""
    allowed = {"name", "role", "experience_level", "organization", "bio", "profile_pic"}
    fields = {k: v for k, v in kwargs.items() if k in allowed}
    if not fields:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row)
    conn = get_connection()
    cursor = conn.cursor()
    set_clause = ", ".join(f"{k} = ?" for k in fields)
    values = list(fields.values()) + [user_id]
    cursor.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def get_user_progress(user_id: int) -> List[Dict[str, Any]]:
    """Get all progress records for a user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_progress WHERE user_id = ? ORDER BY last_practiced DESC", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_topic_mastery(
    user_id: int,
    topic_id: str,
    mastery_level: float,
    time_spent: int = 0,
) -> Dict[str, Any]:
    """Insert or update mastery for a specific topic. Returns the progress record."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, attempts, time_spent FROM user_progress WHERE user_id = ? AND topic_id = ?",
        (user_id, topic_id),
    )
    existing = cursor.fetchone()

    now = datetime.utcnow().isoformat()

    if existing:
        new_time = existing["time_spent"] + time_spent
        new_attempts = existing["attempts"] + 1
        cursor.execute(
            """UPDATE user_progress
               SET mastery_level = ?, time_spent = ?, last_practiced = ?, attempts = ?
               WHERE id = ?""",
            (mastery_level, new_time, now, new_attempts, existing["id"]),
        )
    else:
        cursor.execute(
            """INSERT INTO user_progress (user_id, topic_id, mastery_level, time_spent, last_practiced, attempts)
               VALUES (?, ?, ?, ?, ?, 1)""",
            (user_id, topic_id, mastery_level, time_spent, now),
        )

    conn.commit()

    cursor.execute(
        "SELECT * FROM user_progress WHERE user_id = ? AND topic_id = ?",
        (user_id, topic_id),
    )
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def record_quiz_attempt(
    user_id: int,
    topic_id: str,
    score: float,
    total_questions: int,
    correct_answers: int,
    results_json: str = "[]",
) -> Dict[str, Any]:
    """Record a quiz attempt and return the record."""
    conn = get_connection()
    cursor = conn.cursor()

    # Ensure results_json column exists (migration-safe)
    try:
        cursor.execute("ALTER TABLE quiz_attempts ADD COLUMN results_json TEXT DEFAULT '[]'")
        conn.commit()
    except Exception:
        pass  # column already exists

    cursor.execute(
        """INSERT INTO quiz_attempts (user_id, topic_id, score, total_questions, correct_answers, results_json)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (user_id, topic_id, score, total_questions, correct_answers, results_json),
    )
    conn.commit()
    attempt_id = cursor.lastrowid

    cursor.execute("SELECT * FROM quiz_attempts WHERE id = ?", (attempt_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def record_learning_session(
    user_id: int,
    started_at: str,
    ended_at: str,
    topics_studied: List[str],
    engagement_avg: float = 0.0,
    reward_total: float = 0.0,
) -> Dict[str, Any]:
    """Record a learning session and return the record."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO learning_sessions (user_id, started_at, ended_at, topics_studied,
                                          engagement_avg, reward_total)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (user_id, started_at, ended_at, json.dumps(topics_studied), engagement_avg, reward_total),
    )
    conn.commit()
    session_id = cursor.lastrowid

    cursor.execute("SELECT * FROM learning_sessions WHERE id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def get_quiz_history(user_id: int, topic_id: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
    """Get quiz attempt history for a user, optionally filtered by topic."""
    conn = get_connection()
    cursor = conn.cursor()

    if topic_id:
        cursor.execute(
            "SELECT * FROM quiz_attempts WHERE user_id = ? AND topic_id = ? ORDER BY attempted_at DESC LIMIT ?",
            (user_id, topic_id, limit),
        )
    else:
        cursor.execute(
            "SELECT * FROM quiz_attempts WHERE user_id = ? ORDER BY attempted_at DESC LIMIT ?",
            (user_id, limit),
        )

    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def record_chapter_pass(user_id: int, topic_id: int, chapter_num: int, score: float) -> None:
    """Record that a user passed a chapter quiz (score >= 0.8)."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO chapter_passes (user_id, topic_id, chapter_num, score, passed_at)
            VALUES (?, ?, ?, ?, datetime('now'))
        """, (user_id, topic_id, chapter_num, score))
        conn.commit()
    except Exception:
        try:
            cursor.execute("""ALTER TABLE quiz_attempts ADD COLUMN chapter_num INTEGER DEFAULT 0""")
            conn.commit()
        except Exception:
            pass
        # Retry with migration-safe approach
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chapter_passes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    topic_id INTEGER NOT NULL,
                    chapter_num INTEGER NOT NULL,
                    score REAL DEFAULT 0.0,
                    passed_at TEXT DEFAULT (datetime('now')),
                    UNIQUE(user_id, topic_id, chapter_num)
                )
            """)
            conn.commit()
            cursor.execute("""
                INSERT OR REPLACE INTO chapter_passes (user_id, topic_id, chapter_num, score, passed_at)
                VALUES (?, ?, ?, ?, datetime('now'))
            """, (user_id, topic_id, chapter_num, score))
            conn.commit()
        except Exception:
            pass
    conn.close()


def get_chapter_passes(user_id: int, topic_id: int = None) -> List[Dict[str, Any]]:
    """Get chapter passes for a user. If topic_id given, filter to that topic."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if topic_id is not None:
            cursor.execute(
                "SELECT * FROM chapter_passes WHERE user_id = ? AND topic_id = ? ORDER BY chapter_num",
                (user_id, topic_id)
            )
        else:
            cursor.execute(
                "SELECT * FROM chapter_passes WHERE user_id = ? ORDER BY topic_id, chapter_num",
                (user_id,)
            )
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
    except Exception:
        conn.close()
        return []


def is_main_quiz_unlocked(user_id: int, topic_id: int) -> bool:
    """Check if all 5 chapter quizzes are passed for a topic."""
    passes = get_chapter_passes(user_id, topic_id)
    passed_chapters = {p["chapter_num"] for p in passes if p["score"] >= 0.8}
    return len(passed_chapters) >= 5


def get_all_unlocked_main_quizzes(user_id: int) -> set:
    """Get set of topic IDs where main quiz is unlocked."""
    all_passes = get_chapter_passes(user_id)
    topic_chapters = {}
    for p in all_passes:
        if p["score"] >= 0.8:
            tid = p["topic_id"]
            if tid not in topic_chapters:
                topic_chapters[tid] = set()
            topic_chapters[tid].add(p["chapter_num"])
    return {tid for tid, chs in topic_chapters.items() if len(chs) >= 5}


def get_growth_data(user_id: int, days: int = 30) -> Dict[str, Any]:
    """
    Aggregate growth data for a user over the specified number of days.
    Returns mastery progression, quiz score trends, and session summaries.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()

    # Current mastery per topic
    cursor.execute(
        "SELECT topic_id, mastery_level, time_spent, attempts FROM user_progress WHERE user_id = ?",
        (user_id,),
    )
    mastery = [dict(r) for r in cursor.fetchall()]

    # Quiz scores in period
    cursor.execute(
        """SELECT topic_id, score, attempted_at
           FROM quiz_attempts
           WHERE user_id = ? AND attempted_at >= ?
           ORDER BY attempted_at ASC""",
        (user_id, cutoff),
    )
    quiz_scores = [dict(r) for r in cursor.fetchall()]

    # Learning sessions in period
    cursor.execute(
        """SELECT started_at, ended_at, topics_studied, engagement_avg, reward_total
           FROM learning_sessions
           WHERE user_id = ? AND started_at >= ?
           ORDER BY started_at ASC""",
        (user_id, cutoff),
    )
    sessions = [dict(r) for r in cursor.fetchall()]

    # Compute summary stats
    total_time = sum(m["time_spent"] for m in mastery)
    avg_mastery = (sum(m["mastery_level"] for m in mastery) / len(mastery)) if mastery else 0.0
    avg_quiz_score = (sum(q["score"] for q in quiz_scores) / len(quiz_scores)) if quiz_scores else 0.0
    total_sessions = len(sessions)

    conn.close()

    return {
        "period_days": days,
        "mastery_by_topic": mastery,
        "quiz_score_trend": quiz_scores,
        "sessions": sessions,
        "summary": {
            "total_time_spent": total_time,
            "average_mastery": round(avg_mastery, 4),
            "average_quiz_score": round(avg_quiz_score, 4),
            "total_sessions": total_sessions,
        },
    }


# ---------------------------------------------------------------------------
# Mock Tests CRUD
# ---------------------------------------------------------------------------

def record_mock_test(user_id: int, test_type: str, company: str, total_questions: int,
                     correct_answers: int, score: float, time_taken: int,
                     section_scores: str = "{}", results_json: str = "[]") -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO mock_tests (user_id, test_type, company, total_questions,
            correct_answers, score, time_taken, section_scores, completed_at, results_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), ?)
    """, (user_id, test_type, company, total_questions, correct_answers,
          score, time_taken, section_scores, results_json))
    conn.commit()
    mid = cursor.lastrowid
    cursor.execute("SELECT * FROM mock_tests WHERE id = ?", (mid,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def get_mock_test_history(user_id: int, limit: int = 20) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM mock_tests WHERE user_id = ? ORDER BY completed_at DESC LIMIT ?",
        (user_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Daily Planner CRUD
# ---------------------------------------------------------------------------

def get_daily_tasks(user_id: int, task_date: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM daily_tasks WHERE user_id = ? AND task_date = ? ORDER BY id",
        (user_id, task_date))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_daily_task(user_id: int, task_date: str, task_type: str, topic_id: int,
                   description: str, duration_mins: int = 30) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO daily_tasks (user_id, task_date, task_type, topic_id, description, duration_mins)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, task_date, task_type, topic_id, description, duration_mins))
    conn.commit()
    tid = cursor.lastrowid
    cursor.execute("SELECT * FROM daily_tasks WHERE id = ?", (tid,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def complete_daily_task(task_id: int) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE daily_tasks SET is_completed = 1, completed_at = datetime('now') WHERE id = ?",
        (task_id,))
    conn.commit()
    conn.close()


def delete_daily_task(task_id: int) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM daily_tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def get_weekly_tasks(user_id: int, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM daily_tasks WHERE user_id = ? AND task_date >= ? AND task_date <= ? ORDER BY task_date, id",
        (user_id, start_date, end_date))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Bookmarks CRUD
# ---------------------------------------------------------------------------

def add_bookmark(user_id: int, topic_id: int, chapter_num: int = 0, note: str = "") -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO bookmarks (user_id, topic_id, chapter_num, note, created_at)
        VALUES (?, ?, ?, ?, datetime('now'))
    """, (user_id, topic_id, chapter_num, note))
    conn.commit()
    conn.close()


def get_bookmarks(user_id: int) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM bookmarks WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def remove_bookmark(user_id: int, topic_id: int, chapter_num: int = 0) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM bookmarks WHERE user_id = ? AND topic_id = ? AND chapter_num = ?",
        (user_id, topic_id, chapter_num))
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
# Interview Sessions CRUD
# ---------------------------------------------------------------------------

def record_interview_session(user_id: int, company: str, round_type: str,
                             questions_json: str, responses_json: str,
                             score: float, feedback: str) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO interview_sessions (user_id, company, round_type, questions_json,
            responses_json, score, feedback, completed_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (user_id, company, round_type, questions_json, responses_json, score, feedback))
    conn.commit()
    sid = cursor.lastrowid
    cursor.execute("SELECT * FROM interview_sessions WHERE id = ?", (sid,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)


def get_interview_history(user_id: int, limit: int = 20) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM interview_sessions WHERE user_id = ? ORDER BY completed_at DESC LIMIT ?",
        (user_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Auto-initialize on import
# ---------------------------------------------------------------------------
init_db()
seed_test_user()
