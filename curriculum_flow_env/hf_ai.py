"""Hugging Face inference helpers for chat support and AI quiz generation."""

from __future__ import annotations

import json
import os
import random
import re
from typing import Any

import httpx

# User can override these from env without touching code.
HF_CHAT_MODEL = os.getenv("HF_CHAT_MODEL", "Qwen/Qwen2.5-7B-Instruct")
HF_QUIZ_MODEL = os.getenv("HF_QUIZ_MODEL", "Qwen/Qwen2.5-7B-Instruct")

# Prefer env vars, but keep a local fallback for this project setup.
HF_API_KEY = (
    os.getenv("HF_API_KEY")
    or os.getenv("HUGGINGFACE_API_KEY")
    or os.getenv("HF_TOKEN")
    or ""
)

HF_INFERENCE_URL = "https://router.huggingface.co/hf-inference/models/{model}"
HF_CHAT_COMPLETIONS_URL = "https://router.huggingface.co/hf-inference/models/{model}/v1/chat/completions"

CHAT_SYSTEM_PROMPT = (
    "You are Epoch AI, the built-in assistant for the Epoch.ai placement preparation platform. "
    "You help Indian engineering students with:\n"
    "- DSA concepts, problem-solving strategies, and LeetCode patterns\n"
    "- Interview preparation (technical rounds, HR rounds, STAR method)\n"
    "- Company-specific prep (TCS, Infosys, Wipro, Amazon, Google, Microsoft, etc.)\n"
    "- Study planning, time management, and daily roadmaps\n"
    "- Career guidance, layoff recovery, and job search strategies\n"
    "- Quiz and mock test strategies\n\n"
    "Guidelines:\n"
    "- Be concise, practical, and encouraging\n"
    "- Give actionable steps, not vague advice\n"
    "- Reference Epoch.ai features when relevant (Learning modules, DSA Roadmap, Company Prep, Quizzes, Mock Tests, Interview Sim)\n"
    "- If you truly don't know something, say so politely and suggest where the student can find help\n"
    "- Keep responses under 150 words unless a detailed explanation is genuinely needed\n"
    "- Use simple, friendly language suitable for engineering students\n"
    "- Never reveal that you are a language model or discuss your internal workings\n"
)


def _extract_generated_text(payload: Any) -> str:
    """Normalize HF response payload into plain generated text."""
    if isinstance(payload, list) and payload:
        first = payload[0]
        if isinstance(first, dict):
            if "generated_text" in first:
                return str(first["generated_text"]).strip()
            if "summary_text" in first:
                return str(first["summary_text"]).strip()
        return str(first).strip()

    if isinstance(payload, dict):
        if "generated_text" in payload:
            return str(payload["generated_text"]).strip()
        if "error" in payload:
            raise RuntimeError(str(payload["error"]))

    return str(payload).strip()


async def _call_hf_text_model(
    model: str,
    prompt: str,
    *,
    max_new_tokens: int = 400,
    temperature: float = 0.7,
    top_p: float = 0.9,
) -> str:
    if not HF_API_KEY:
        raise RuntimeError("Missing Hugging Face API key")

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    body = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "return_full_text": False,
            "do_sample": True,
        },
        "options": {"wait_for_model": True},
    }

    async with httpx.AsyncClient(timeout=75) as client:
        resp = await client.post(HF_INFERENCE_URL.format(model=model), headers=headers, json=body)
        try:
            data = resp.json()
        except Exception:
            data = {"error": f"Non-JSON response from model {model}"}

    if resp.status_code >= 400:
        err = data.get("error") if isinstance(data, dict) else str(data)
        raise RuntimeError(f"HF model call failed ({resp.status_code}): {err}")

    return _extract_generated_text(data)


async def generate_support_chat_reply(
    user_message: str,
    user_context: str = "",
    history: list | None = None,
) -> str:
    """Generate support/career chat reply using Qwen via HF chat completions."""
    if not HF_API_KEY:
        raise RuntimeError("Missing Hugging Face API key")

    system_content = CHAT_SYSTEM_PROMPT + (
        f"\n\nCurrent user context: {user_context or 'Not available.'}"
    )

    messages: list[dict[str, str]] = [
        {"role": "system", "content": system_content},
    ]

    # Append recent conversation history for context (last 8 turns)
    if history:
        for msg in history[-8:]:
            role = msg.get("role", "user")
            content = (msg.get("content") or "").strip()
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": user_message.strip()})

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": HF_CHAT_MODEL,
        "messages": messages,
        "max_tokens": 400,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": False,
    }

    url = HF_CHAT_COMPLETIONS_URL.format(model=HF_CHAT_MODEL)

    async with httpx.AsyncClient(timeout=75) as client:
        resp = await client.post(url, headers=headers, json=body)
        try:
            data = resp.json()
        except Exception:
            data = {"error": f"Non-JSON response from chat model"}

    if resp.status_code >= 400:
        err = data.get("error") if isinstance(data, dict) else str(data)
        raise RuntimeError(f"HF chat call failed ({resp.status_code}): {err}")

    # Extract from OpenAI-compatible chat completions format
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        # Fallback: try text generation format
        text = _extract_generated_text(data)
        if text:
            return text
        raise RuntimeError(f"Unexpected chat response format: {data}")


def _parse_json_array(text: str) -> list[dict]:
    """Extract first JSON array from a model response."""
    raw = text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

    start = raw.find("[")
    end = raw.rfind("]")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON array found in model output")

    parsed = json.loads(raw[start : end + 1])
    if not isinstance(parsed, list):
        raise ValueError("Model output is not a JSON array")
    return parsed


def _normalize_correct_index(correct_raw: Any, options: list[str]) -> int:
    if isinstance(correct_raw, int):
        return max(0, min(3, correct_raw))

    if isinstance(correct_raw, str):
        val = correct_raw.strip()
        if val.isdigit():
            return max(0, min(3, int(val)))
        letter_map = {"a": 0, "b": 1, "c": 2, "d": 3}
        if val.lower() in letter_map:
            return letter_map[val.lower()]
        for idx, opt in enumerate(options):
            if val.lower() == opt.lower():
                return idx

    return 0


def _normalize_question(item: dict) -> dict | None:
    if not isinstance(item, dict):
        return None

    question = str(item.get("question", "")).strip()
    explanation = str(item.get("explanation", "")).strip()
    options = item.get("options", [])

    if isinstance(options, dict):
        options = [options.get(k, "") for k in ["A", "B", "C", "D"]]

    options = [str(opt).strip() for opt in options if str(opt).strip()]
    if len(options) < 4:
        for key in ("option_a", "option_b", "option_c", "option_d"):
            if key in item:
                val = str(item[key]).strip()
                if val:
                    options.append(val)
    options = options[:4]

    if not question or len(options) < 4:
        return None

    correct = _normalize_correct_index(item.get("correct", item.get("answer", 0)), options)

    # Shuffle options for variation, while keeping the correct index accurate.
    pairs = list(enumerate(options))
    random.shuffle(pairs)
    shuffled_options = [opt for _, opt in pairs]
    for new_idx, (old_idx, _) in enumerate(pairs):
        if old_idx == correct:
            correct = new_idx
            break

    return {
        "question": question,
        "options": shuffled_options,
        "correct": correct,
        "explanation": explanation or "Review this concept and solve a few similar problems.",
    }


async def generate_quiz_with_ai(
    *,
    topic_name: str,
    question_count: int,
    difficulty: str = "mixed",
    focus_prompt: str = "",
) -> list[dict]:
    """Generate quiz questions with HF quiz model."""
    count = max(3, min(25, int(question_count)))
    difficulty = (difficulty or "mixed").strip().lower()
    if difficulty not in {"easy", "medium", "hard", "mixed"}:
        difficulty = "mixed"

    prompt = (
        "Generate high-quality placement-prep multiple choice questions.\n"
        "Return ONLY a valid JSON array, nothing else.\n"
        f"Topic: {topic_name}\n"
        f"Difficulty: {difficulty}\n"
        f"Question count: {count}\n"
        f"Extra focus: {focus_prompt.strip() or 'none'}\n\n"
        "Output format (strict):\n"
        "[\n"
        '  {"question":"...", "options":["...","...","...","..."], "correct":0, "explanation":"..."}\n'
        "]\n"
        "Rules:\n"
        "- exactly 4 options per question\n"
        "- 'correct' must be 0,1,2,or 3\n"
        "- only one correct option per question\n"
        "- use clear, exam-style language\n"
        "- avoid duplicates\n"
        "- no markdown, no code fences\n"
    )

    raw = await _call_hf_text_model(
        HF_QUIZ_MODEL,
        prompt,
        max_new_tokens=min(2200, 240 * count),
        temperature=0.95,
        top_p=0.95,
    )
    parsed = _parse_json_array(raw)

    normalized: list[dict] = []
    for item in parsed:
        q = _normalize_question(item)
        if q:
            normalized.append(q)
        if len(normalized) >= count:
            break

    if not normalized:
        raise ValueError("AI quiz output could not be normalized")

    return normalized[:count]
