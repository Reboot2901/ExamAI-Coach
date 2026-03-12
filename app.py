"""
app.py — ExamAI Coach entry point.
"""
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# MUST be first Streamlit command
st.set_page_config(
    page_title="ExamAI Coach — Premium AI Study Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

from ui_styles import apply_global_styles
apply_global_styles()

# Lazy imports to avoid circular issues
from dashboard import show_dashboard
from mistake_explainer import mistake_explainer
from viva_examiner import viva_examiner
from doubt_predictor import doubt_predictor
from ai_tutor_chat import ai_tutor_chat
from flashcards import display_flashcards
from quiz_generator_page import quiz_generator_page
from study_planner_page import study_planner_page
from notes_summarizer import notes_summarizer
from pdf_analyzer_page import pdf_analyzer_page
from analytics import display_dashboard as analytics_page


def main():
    # Stub user (no auth required — single-user mode)
    user = {"id": "local_user", "name": "Student", "username": "student"}

    # Initialize page state
    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    # ── Sidebar ────────────────────────────────────────────────
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

        pages = [
            ("🏠", "Dashboard"),
            ("📝", "Mistake Explainer"),
            ("🎤", "Viva Practice"),
            ("🔮", "Doubt Predictor"),
            ("🤖", "AI Tutor"),
            ("🃏", "Flashcards"),
            ("📊", "Quiz Generator"),
            ("📅", "Study Planner"),
            ("✍️", "Notes Summarizer"),
            ("📄", "PDF Analyzer"),
            ("📈", "Analytics"),
        ]

        current_page = st.session_state.page
        for icon, name in pages:
            btn_type = "primary" if current_page == name else "secondary"
            if st.button(f"{icon}  {name}", key=f"nav_{name}", use_container_width=True, type=btn_type):
                st.session_state.page = name
                st.rerun()

    # ── Main content ───────────────────────────────────────────
    page = st.session_state.page

    if page == "Dashboard":
        show_dashboard(user)
    elif page == "Mistake Explainer":
        mistake_explainer(user)
    elif page == "Viva Practice":
        viva_examiner(user)
    elif page == "Doubt Predictor":
        doubt_predictor()
    elif page == "AI Tutor":
        ai_tutor_chat(user)
    elif page == "Flashcards":
        display_flashcards()
    elif page == "Quiz Generator":
        quiz_generator_page(user)
    elif page == "Study Planner":
        study_planner_page()
    elif page == "Notes Summarizer":
        notes_summarizer()
    elif page == "PDF Analyzer":
        pdf_analyzer_page(user)
    elif page == "Analytics":
        analytics_page(user)


if __name__ == "__main__":
    main()
