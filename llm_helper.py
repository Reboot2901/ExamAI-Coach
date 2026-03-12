"""
llm_helper.py — Single source of truth for all Gemini API calls.

Usage:
    from llm_helper import ask_llm
    answer, sources = ask_llm("Explain Newton's second law")
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"


def _get_model() -> genai.GenerativeModel:
    """Configure Gemini and return the model instance."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY is not set. Add it to your .env file.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def ask_llm(prompt: str) -> tuple[str, list]:
    """
    Send a prompt to Gemini and return (answer: str, sources: list).

    Always returns a 2-tuple so callers can safely unpack:
        answer, sources = ask_llm(prompt)

    Sources list is always empty for non-grounded calls.
    """
    if not prompt or not prompt.strip():
        return "Please provide a valid input.", []

    try:
        model = _get_model()
        response = model.generate_content(prompt)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip(), []

        return "No response was generated. Please try again.", []

    except EnvironmentError as e:
        return f"⚠️ Configuration Error: {e}", []
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "invalid api key" in error_msg.lower():
            return "⚠️ Invalid API Key. Please check your GEMINI_API_KEY in .env.", []
        if "quota" in error_msg.lower() or "rate" in error_msg.lower():
            return "⚠️ Rate limit reached. Please wait a moment and try again.", []
        if "not found" in error_msg.lower() or "model" in error_msg.lower():
            return f"⚠️ Model error: {error_msg}. Check your Gemini model name.", []
        return f"❌ Gemini Error: {error_msg}", []