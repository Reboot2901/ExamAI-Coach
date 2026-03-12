import streamlit as st
from quiz_generator import generate_quiz, display_quiz
from database import save_quiz_score

def quiz_generator_page(user):
    from ui_styles import render_page_header
    render_page_header("📊", "Quiz Generator", "Create MCQ quizzes to test your knowledge instantly")

    with st.form("quiz_gen_form"):
        topic = st.text_input("Enter topic for quiz", placeholder="e.g., Python, Data Science, etc.")
        submitted = st.form_submit_button("Generate Quiz", type="primary", use_container_width=True)
    
    if submitted:
        if topic:
            with st.spinner("Generating quiz..."):
                quiz_data = generate_quiz(topic)
            st.session_state.quiz_data = quiz_data
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
        else:
            st.warning("Please enter a topic.")

    if "quiz_data" in st.session_state:
        with st.container(border=True):
            display_quiz(st.session_state.quiz_data)
            
        # Save score if completed
        if st.session_state.get("quiz_submitted", False):
            correct = sum(1 for q in st.session_state.quiz_data["questions"]
                         if st.session_state.quiz_answers.get(list(st.session_state.quiz_answers.keys()).index(q["question"])+1 if st.session_state.quiz_answers else 0, "") == q["correct_answer"])
            save_quiz_score(user["id"], topic, correct, len(st.session_state.quiz_data["questions"]))
