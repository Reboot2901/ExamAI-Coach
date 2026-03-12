import os
import requests
from dotenv import load_dotenv

load_dotenv()

# =========================
# Configuration
# =========================

# Choose provider: "ollama" or "gemini"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")

# Ollama settings
MODEL_NAME = "llama3"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Gemini settings
GEMINI_MODEL = "gemini-1.5-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# =========================
# Ollama function
# =========================

def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from Ollama.")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"


# =========================
# Gemini function
# =========================

def ask_gemini(prompt: str) -> str:
    try:
        import google.generativeai as genai

        if not GEMINI_API_KEY:
            return "Error: GEMINI_API_KEY not found in environment variables."

        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text
        return "No response from Gemini."

    except Exception as e:
        return f"Error connecting to Gemini: {e}"


# =========================
# Main helper
# =========================

def ask_llm(prompt: str) -> str:
    if LLM_PROVIDER.lower() == "ollama":
        return ask_ollama(prompt)
    elif LLM_PROVIDER.lower() == "gemini":
        return ask_gemini(prompt)
    else:
        return "Error: Invalid LLM_PROVIDER. Use 'ollama' or 'gemini'."