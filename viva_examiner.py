import streamlit as st
from llm_helper import ask_llm
from prompts import viva_question_prompt, viva_eval_prompt
from database import save_viva_attempt


def viva_examiner(user):
    from ui_styles import render_page_header
    render_page_header("🎤", "Viva Examiner", "Practice viva voce examinations with real-time AI evaluation")

    with st.form("viva_gen_form"):
        subject = st.selectbox(
            "Select Subject",
            ["DBMS", "Operating Systems", "Computer Networks", "Artificial Intelligence",
             "Data Structures", "Algorithms", "Software Engineering", "Machine Learning"]
        )
        generate_clicked = st.form_submit_button("Generate Viva Question", type="primary", use_container_width=True)

    if generate_clicked:
        with st.spinner("Generating question..."):
            prompt = viva_question_prompt(subject)
            question, _ = ask_llm(prompt)
            st.session_state.viva_question = question
            st.session_state.viva_subject = subject

    if "viva_question" in st.session_state:
        st.markdown(
            f"<div style='background:rgba(14,165,233,0.08);border:1px solid rgba(14,165,233,0.2);"
            f"padding:16px;border-radius:12px;color:#E0F2FE;font-size:1rem;margin:16px 0;'>"
            f"<strong>Question:</strong><br>{st.session_state.viva_question}</div>",
            unsafe_allow_html=True
        )

        with st.form("viva_eval_form"):
            answer = st.text_area("Your Answer", height=150, placeholder="Provide your detailed answer...")
            evaluate_clicked = st.form_submit_button("Evaluate Answer", type="primary", use_container_width=True)

        if evaluate_clicked:
            if answer.strip():
                with st.spinner("Evaluating your answer..."):
                    prompt = viva_eval_prompt(st.session_state.viva_question, answer)
                    evaluation, _ = ask_llm(prompt)

                with st.container(border=True):
                    st.markdown(
                        "<div style='background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"
                        "padding:12px 16px;border-radius:8px;color:#10B981;font-weight:500;margin-bottom:16px;'>"
                        "✨ Evaluation Complete!</div>",
                        unsafe_allow_html=True
                    )
                    st.subheader("Evaluation Results")
                    st.write(evaluation)

                try:
                    save_viva_attempt(
                        user["id"],
                        st.session_state.viva_subject,
                        st.session_state.viva_question,
                        answer,
                        evaluation
                    )
                except Exception:
                    pass
            else:
                st.warning("Please provide an answer.")
