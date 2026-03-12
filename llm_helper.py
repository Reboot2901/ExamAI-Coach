import os

try:
    import google.generativeai as genai
except ImportError as e:
    genai = None
    _import_error = str(e)
else:
    _import_error = None


def ask_llm(prompt: str) -> str:
    if genai is None:
        return f"Import error in llm_helper: {_import_error}"

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Missing GEMINI_API_KEY."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "No response generated."
    except Exception as e:
        return f"LLM error: {e}"