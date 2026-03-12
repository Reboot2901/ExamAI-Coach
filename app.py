import streamlit as st
from dashboard import show_dashboard
from mistake_explainer import mistake_explainer
from viva_examiner import viva_examiner
from doubt_predictor import doubt_predictor
from ai_tutor_chat import ai_tutor_chat
from flashcards import display_flashcards as flashcards
from quiz_generator_page import quiz_generator_page as quiz_generator
from study_planner_page import study_planner_page as study_planner
from notes_summarizer import notes_summarizer
from pdf_analyzer_page import pdf_analyzer_page as pdf_analyzer
from analytics import display_dashboard as analytics
from dotenv import load_dotenv

# Load environment variables (Tavily API key, etc.)
load_dotenv()

# Page configuration (MUST BE FIRST STREAMLIT COMMAND)
st.set_page_config(
    page_title="ExamAI Coach - Premium AI Study Companion",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_styles import apply_global_styles

# Apply Premium AI SaaS Dashboard Dark Theme CSS
apply_global_styles()

# Main app logic
def main():
    # Hardcoded user stub for downstream pages that expect a user object for saving to the DB
    user = {"id": "local_user", "name": "Local Student", "username": "student"}
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-brand">
            <div class="brand-icon">🎓</div>
            <div class="brand-text">
                <h2>ExamAI Coach</h2>
                <p>AI Study Assistant</p>
            </div>
        </div>
        <div class="sidebar-divider"></div>
        """, unsafe_allow_html=True)

        menu_options = [
            {"icon": "🏠", "name": "Dashboard"},
            {"icon": "📝", "name": "Mistake Explainer"},
            {"icon": "🎤", "name": "Viva Practice"},
            {"icon": "🔮", "name": "Doubt Predictor"},
            {"icon": "🤖", "name": "AI Tutor"},
            {"icon": "🃏", "name": "Flashcards"},
            {"icon": "📊", "name": "Quiz Generator"},
            {"icon": "📅", "name": "Study Planner"},
            {"icon": "✍️", "name": "Notes Summarizer"},
            {"icon": "📄", "name": "PDF Analyzer"},
            {"icon": "📈", "name": "Analytics"}
        ]

        if "page" not in st.session_state:
            st.session_state.page = "Dashboard"
            
        current_page = st.session_state.page
        
        for option in menu_options:
            is_active = current_page == option["name"]
            btn_type = "primary" if is_active else "secondary"
            
            # Use unicode whitespace characters to simulate exact 14px gap (EM space)
            if st.button(f"{option['icon']} \u2003 {option['name']}", key=f"nav_{option['name']}", use_container_width=True, type=btn_type):
                st.session_state.page = option["name"]
                st.rerun()

    # Main content
    current_page = st.session_state.page

    if current_page == "Dashboard":
        show_dashboard(user)
    elif current_page == "Mistake Explainer":
        mistake_explainer(user)
    elif current_page == "Viva Practice":
        viva_examiner(user)
    elif current_page == "Doubt Predictor":
        doubt_predictor()
    elif current_page == "AI Tutor":
        ai_tutor_chat(user)
    elif current_page == "Flashcards":
        flashcards()
    elif current_page == "Quiz Generator":
        quiz_generator(user)
    elif current_page == "Study Planner":
        study_planner()
    elif current_page == "Notes Summarizer":
        notes_summarizer()
    elif current_page == "PDF Analyzer":
        pdf_analyzer(user)
    elif current_page == "Analytics":
        analytics(user)


if __name__ == "__main__":
    main()
