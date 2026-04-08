"""
Seed demo data for Epoch.ai hackathon demo.
Creates a demo user with rich quiz history across multiple topics
so the dashboard, growth analytics, and AI recommendations look impressive.

Usage: python seed_demo_data.py
"""

import json
import random
from datetime import datetime, timedelta
from curriculum_flow_env.database import (
    init_db, get_connection, create_user, get_user_by_email,
    record_quiz_attempt, update_topic_mastery,
)
from curriculum_flow_env.simulation.curriculum import (
    TOPIC_DISPLAY_NAMES, TOPIC_GROUPS, GROUP_DISPLAY_NAMES, NUM_TOPICS,
)

init_db()

DEMO_EMAIL = "demo@epoch.ai"
DEMO_PASSWORD = "demo123"
DEMO_NAME = "Alex Kumar"


def seed():
    # Check if demo user exists
    existing = get_user_by_email(DEMO_EMAIL)
    if existing:
        print(f"Demo user already exists (id={existing['id']}). Deleting and recreating...")
        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM quiz_attempts WHERE user_id = ?", (existing["id"],))
        c.execute("DELETE FROM user_progress WHERE user_id = ?", (existing["id"],))
        c.execute("DELETE FROM users WHERE id = ?", (existing["id"],))
        conn.commit()
        conn.close()

    # Create demo user
    user = create_user(
        email=DEMO_EMAIL,
        password=DEMO_PASSWORD,
        name=DEMO_NAME,
        role="student",
        experience_level="intermediate",
        organization="Epoch Labs",
        bio="Curious Learner, Problem Solver, Fast Learner",
    )
    uid = user["id"]
    print(f"Created demo user: {DEMO_NAME} (id={uid}, email={DEMO_EMAIL})")

    # Define mastery levels per topic to simulate a realistic learning journey
    # Some topics strong, some weak, some untouched
    mastery_map = {
        0: 0.05,   # Numbers - low
        1: 0.0,    # HCF & LCM - untouched
        2: 0.12,   # Percentages - started
        3: 0.0,    # Profit & Loss
        4: 0.0,    # Ratio & Proportion
        5: 0.0,    # Time & Work
        6: 0.0,    # Time & Distance
        7: 0.0,    # Simple Interest
        8: 0.0,    # Compound Interest
        9: 0.0,    # Averages
        10: 0.0,   # Problems on Ages
        11: 0.0,   # Permutations
        12: 0.15,  # Coding-Decoding - some progress
        13: 0.0,   # Blood Relations
        14: 0.0,   # Direction Sense
        15: 0.0,   # Seating Arrangement
        16: 0.0,   # Syllogism
        17: 0.08,  # Number Series - started
        18: 0.0,   # Analogies
        19: 0.0,   # Logical Deduction
        20: 0.65,  # Synonyms - STRONG
        21: 0.45,  # Antonyms - good
        22: 0.30,  # Sentence Completion - decent
        23: 0.20,  # Reading Comprehension
        24: 0.0,   # Para Jumbles
        25: 0.0,   # Spotting Errors
        26: 0.0,   # Idioms & Phrases
        27: 0.10,  # Tables (data interp)
        28: 0.0,   # Bar Graphs
        29: 0.0,   # Pie Charts
        30: 0.0,   # Line Graphs
        31: 0.35,  # C Basics - decent
        32: 0.20,  # Data Types & Operators
        33: 0.10,  # Control Flow
        34: 0.0,   # Arrays & Strings
        35: 0.0,   # Pointers & References
        36: 0.0,   # OOP Concepts
        37: 0.0,   # Data Structures
        38: 0.0,   # Algorithms Basics
        39: 0.0,   # SQL Basics
    }

    # Set mastery levels
    for tid, mastery in mastery_map.items():
        if mastery > 0:
            update_topic_mastery(uid, tid, mastery)

    # Generate quiz history spread across 7 days
    base_date = datetime.now() - timedelta(days=7)
    quiz_data = [
        # (topic_id, score_pct, correct, total, day_offset)
        (20, 100, 5, 5, 0),   # Synonyms - perfect
        (20, 80, 4, 5, 1),    # Synonyms - good
        (21, 60, 3, 5, 1),    # Antonyms - ok
        (31, 80, 4, 5, 1),    # C Basics - good
        (0,  40, 2, 5, 2),    # Numbers - struggled
        (0,  20, 1, 5, 2),    # Numbers - struggled again
        (22, 60, 3, 5, 2),    # Sentence Completion
        (31, 60, 3, 5, 3),    # C Basics - second attempt
        (12, 40, 2, 5, 3),    # Coding-Decoding
        (32, 40, 2, 5, 3),    # Data Types
        (2,  60, 3, 5, 4),    # Percentages
        (21, 80, 4, 5, 4),    # Antonyms - improved!
        (17, 40, 2, 5, 5),    # Number Series
        (23, 60, 3, 5, 5),    # Reading Comprehension
        (33, 40, 2, 5, 5),    # Control Flow
        (27, 40, 2, 5, 6),    # Tables
        (20, 80, 4, 5, 6),    # Synonyms - still strong
        (22, 80, 4, 5, 7),    # Sentence Completion - improved!
    ]

    sample_questions = [
        {"question": "Sample question", "your_answer": "Option A",
         "correct_answer": "Option A", "is_correct": True,
         "explanation": "This demonstrates the key concept."},
        {"question": "Sample question 2", "your_answer": "Option B",
         "correct_answer": "Option C", "is_correct": False,
         "explanation": "Review the fundamental approach to this type of problem."},
    ]

    for tid, score_pct, correct, total, day_off in quiz_data:
        score = score_pct / 100.0

        # Generate realistic results_json
        results = []
        for i in range(total):
            is_correct = i < correct
            results.append({
                "question": f"Q{i+1} for {TOPIC_DISPLAY_NAMES.get(tid, 'Topic')}",
                "your_answer": "Correct Option" if is_correct else "Wrong Option",
                "correct_answer": "Correct Option",
                "is_correct": is_correct,
                "explanation": f"Explanation for question {i+1}.",
            })
        random.shuffle(results)

        record_quiz_attempt(uid, tid, score, total, correct, json.dumps(results))

        # Manually set the attempted_at date for a spread-out history
        attempt_date = (base_date + timedelta(days=day_off, hours=random.randint(9, 21))).strftime("%Y-%m-%d %H:%M:%S")
        conn = get_connection()
        c = conn.cursor()
        c.execute(
            "UPDATE quiz_attempts SET attempted_at = ? WHERE id = (SELECT MAX(id) FROM quiz_attempts WHERE user_id = ? AND topic_id = ?)",
            (attempt_date, uid, tid)
        )
        conn.commit()
        conn.close()

    print(f"Seeded {len(quiz_data)} quiz attempts across {len(set(q[0] for q in quiz_data))} topics")
    print(f"Set mastery levels for {sum(1 for v in mastery_map.values() if v > 0)} topics")
    print(f"\nDemo login: {DEMO_EMAIL} / {DEMO_PASSWORD}")
    print("Ready for hackathon demo!")


if __name__ == "__main__":
    seed()
