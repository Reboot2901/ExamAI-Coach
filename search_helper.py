import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_gemini_api_key():
    """Retrieve the Gemini API key from environment variables."""
    return os.environ.get("GEMINI_API_KEY", "")

def should_use_live_search(query):
    """
    Determine if a query likely requires real-time web search.
    Looks for keywords indicating recency or live information.
    """
    query_lower = query.lower()
    search_keywords = [
        "latest", "current", "recent", "today", "new", 
        "update", "news", "now", "trends", "this year", "this month",
        "right now"
    ]
    
    for word in search_keywords:
        if word in query_lower:
            return True
            
    return False

def get_gemini_client():
    """Initialize the Gemini client if the key is available."""
    api_key = get_gemini_api_key()
    if not api_key or api_key == "your_gemini_api_key_here" or api_key.startswith("tvly-"):
        return None
        
    return genai.Client(api_key=api_key)

def ask_gemini_grounded(question):
    """
    Call Gemini with Google Search Grounding enabled via the new SDK.
    Returns (answer_text, sources_list) or handles errors.
    """
    client = get_gemini_client()
    if not client:
        return "⚠️ GEMINI_API_KEY is missing or invalid. Please check your .env file.", []
        
    try:
        # Configure the tool for Google Search
        tool = types.Tool(google_search=types.GoogleSearch())
        
        prompt = f"""You are an AI study assistant. Answer the student's question clearly and simply.
Because they asked about current information, use the Google Search tool to find the latest facts.
Question: {question}"""

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(tools=[tool])
        )
        
        sources = format_grounded_sources(response)
        
        return response.text, sources
        
    except Exception as e:
        return f"❌ Error connecting to Gemini Search: {str(e)}", []
        
def ask_gemini_standard(question, history_context=""):
    """
    Standard Gemini call without grounding for timeless questions.
    """
    client = get_gemini_client()
    if not client:
        return "⚠️ GEMINI_API_KEY is missing or invalid. Please check your .env file."
        
    try:
        prompt = f"""You are an AI study assistant. Answer the student accurately.
{history_context}
Question: {question}"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Error connecting to Gemini: {str(e)}"

def format_grounded_sources(response):
    """
    Extracts and formats source links and titles from the Gemini response grounding metadata.
    Returns a list of dictionaries with 'title', 'url', and 'content' snippet.
    """
    sources = []
    
    if not response.candidates:
        return sources
        
    candidate = response.candidates[0]
    
    if hasattr(candidate, 'grounding_metadata') and candidate.grounding_metadata:
        metadata = candidate.grounding_metadata
        
        # In the Google GenAI Python SDK, grounding_chunks hold the web sources
        chunks = getattr(metadata, 'grounding_chunks', [])
        if chunks:
            for chunk in chunks:
                web_source = getattr(chunk, 'web', None)
                if web_source:
                    sources.append({
                        "title": getattr(web_source, 'title', 'Web Source'),
                        "url": getattr(web_source, 'uri', '#'),
                        "content": "" # Snippets aren't always explicitly isolated in the same way, but the title and URI are present.
                    })
                    
    return sources
