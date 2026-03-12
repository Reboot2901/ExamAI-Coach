"""
search_helper.py — Gemini live search with graceful fallbacks.

All public functions return (answer: str, sources: list).
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"


def _configure() -> bool:
    """Configure Gemini. Returns False if API key is missing."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return False
    genai.configure(api_key=api_key)
    return True


def should_use_live_search(query: str) -> bool:
    """
    Return True if the query likely requires recent/live information.
    Uses keyword matching — never crashes.
    """
    if not query or not query.strip():
        return False
    live_keywords = [
        "latest", "current", "today", "recent", "news",
        "now", "2024", "2025", "this year", "right now", "update"
    ]
    return any(kw in query.lower() for kw in live_keywords)


def ask_gemini_grounded(question: str) -> tuple[str, list]:
    """
    Gemini answer with grounding context.
    Always returns (answer: str, sources: list) — never raises.
    """
    if not question or not question.strip():
        return "Please provide a valid question.", []

    if not _configure():
        return "⚠️ GEMINI_API_KEY is missing. Please set it in your .env file.", []

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = (
            "You are an AI study assistant. Answer the following student question "
            "clearly, accurately and in a student-friendly way.\n\n"
            f"Question: {question}"
        )
        response = model.generate_content(prompt)
        answer = response.text.strip() if response and response.text else "No answer generated."
        return answer, []

    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
            return "⚠️ Invalid API Key. Please check your GEMINI_API_KEY in .env.", []
        if "quota" in error_msg.lower() or "rate" in error_msg.lower():
            return "⚠️ Rate limit reached. Please try again shortly.", []
        # Fallback to standard call
        fallback, _ = ask_gemini_standard(question)
        return fallback, []


def ask_gemini_standard(question: str, history_context: str = "") -> tuple[str, list]:
    """
    Standard Gemini call — no live grounding.
    Always returns (answer: str, sources: list).
    """
    if not question or not question.strip():
        return "Please provide a valid question.", []

    if not _configure():
        return "⚠️ GEMINI_API_KEY is missing. Please set it in your .env file.", []

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = (
            "You are an AI study assistant. Answer the student accurately and clearly.\n"
            + (f"{history_context}\n" if history_context else "")
            + f"Question: {question}"
        )
        response = model.generate_content(prompt)
        answer = response.text.strip() if response and response.text else "No response generated."
        return answer, []

    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
            return "⚠️ Invalid API Key. Please check your GEMINI_API_KEY in .env.", []
        return f"❌ Gemini Error: {error_msg}", []
