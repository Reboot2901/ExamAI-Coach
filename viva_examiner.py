import streamlit as st
from llm_helper import ask_llm
from prompts import viva_question_prompt, viva_eval_prompt
from database import save_viva_attempt

def viva_examiner(user):
    from ui_styles import render_page_header
    render_page_header("🎤", "Viva Examiner", "Practice viva voce examinations with AI evaluation")

    # Form and Action Buttons
    with st.form("viva_gen_form"):
        subject = st.selectbox("Select Subject", ["DBMS", "Operating Systems", "Computer Networks", "Artificial Intelligence"])
        generate_clicked = st.form_submit_button("Generate Viva Question", type="primary", use_container_width=True)
        
    if generate_clicked:
        with st.spinner("Generating question..."):
            prompt = viva_question_prompt(subject)
            question = ask_llm(prompt)
            st.session_state.viva_question = question
            st.session_state.viva_subject = subject

    # Evaluation Section
    if "viva_question" in st.session_state:
        st.markdown("<h3 style='margin-top: 24px; font-family: Outfit, sans-serif;'>Current Question</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(14, 165, 233, 0.2); padding: 16px; border-radius: 12px; color: #E0F2FE; font-weight: 500; font-size: 1rem; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);'>{st.session_state.viva_question}</div>", unsafe_allow_html=True)
        
        with st.form("viva_eval_form"):
            answer = st.text_area("Your Answer", height=150, placeholder="Provide your detailed answer...")
            evaluate_clicked = st.form_submit_button("Evaluate Answer", type="primary", use_container_width=True)
        
        if evaluate_clicked:
            if answer:
                with st.spinner("Evaluating your answer..."):
                    prompt = viva_eval_prompt(st.session_state.viva_question, answer)
                    evaluation = ask_llm(prompt)
                
                # Render results in a targeted panel
                with st.container(border=True):
                    st.markdown("<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px 16px; border-radius: 8px; color: #10B981; font-weight: 500; font-size: 0.95rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;'>✨ Evaluation Complete!</div>", unsafe_allow_html=True)
                    st.subheader("Evaluation Results")
                    st.write(evaluation)
                
                try:
                    save_viva_attempt(user["id"], st.session_state.viva_subject, st.session_state.viva_question, answer, evaluation)
                except Exception as e:
                    pass # Ignore if DB not setup
            else:
                st.warning("Please provide an answer.")
