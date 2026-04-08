"""
CurriculumFlowENV Authentication Module
Simple session-based authentication using in-memory session storage.
"""

import uuid
from typing import Optional, Dict, Any

from fastapi import Request, Response

from .database import get_user_by_email, verify_password

# In-memory session store: {session_token: user_id}
sessions: Dict[str, int] = {}

SESSION_COOKIE_NAME = "mindmatrix_session"


def create_session(user_id: int) -> str:
    """Create a new session for a user and return the session token."""
    token = str(uuid.uuid4())
    sessions[token] = user_id
    return token


def get_current_user(request: Request) -> Optional[Dict[str, Any]]:
    """
    Read the session cookie from the request and return the user dict.
    Returns None if no valid session exists.
    """
    token = request.cookies.get(SESSION_COOKIE_NAME)
    if token is None or token not in sessions:
        return None

    user_id = sessions[token]

    # Look up the user by id via email scan (use a direct query instead)
    from .database import get_connection

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        # Session references a deleted user; clean up
        del sessions[token]
        return None

    return dict(row)


def login_user(response: Response, user_id: int) -> str:
    """
    Create a session for the user and set the session cookie on the response.
    Returns the session token.
    """
    token = create_session(user_id)
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=token,
        httponly=True,
        samesite="lax",
        max_age=60 * 60 * 24 * 7,  # 7 days
    )
    return token


def logout_user(response: Response, request: Request) -> None:
    """
    Clear the session from memory and delete the session cookie.
    """
    token = request.cookies.get(SESSION_COOKIE_NAME)
    if token and token in sessions:
        del sessions[token]

    response.delete_cookie(key=SESSION_COOKIE_NAME)
