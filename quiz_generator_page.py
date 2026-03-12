import streamlit as st
from quiz_generator import generate_quiz, display_quiz


def quiz_generator_page(user):
    from ui_styles import render_page_header
    render_page_header("📊", "Quiz Generator", "Create automated MCQ quizzes to test your knowledge gaps instantly")

    with st.form("quiz_gen_form"):
        topic = st.text_input("Enter a topic for the quiz:", placeholder="e.g., Newton's Laws, Binary Trees...")
        submitted = st.form_submit_button("Generate Quiz", type="primary", use_container_width=True)

    if submitted:
        if topic.strip():
            with st.spinner("Generating quiz questions..."):
                quiz_data = generate_quiz(topic)
            st.session_state.current_quiz = quiz_data
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()
        else:
            st.warning("Please enter a topic.")

    if "current_quiz" in st.session_state:
        display_quiz(st.session_state.current_quiz)
