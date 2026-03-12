import streamlit as st
import re
from llm_helper import ask_llm
from prompts import mistake_prompt
from database import save_mistake_analysis


def mistake_explainer(user):
    from ui_styles import render_page_header
    render_page_header("📝", "Mistake Explainer", "Get detailed AI feedback on your answers with scores and improvement tips")

    with st.form("mistake_form"):
        col1, col2 = st.columns(2)
        with col1:
            question = st.text_area("Question", height=150, placeholder="Paste the exam question here...")
        with col2:
            student_answer = st.text_area("Your Answer", height=150, placeholder="Type your answer here...")
        submitted = st.form_submit_button("Analyze Answer", type="primary", use_container_width=True)

    if submitted:
        if question.strip() and student_answer.strip():
            with st.spinner("Analyzing your answer..."):
                prompt = mistake_prompt(question, student_answer)
                response, _ = ask_llm(prompt)

            score = 0
            mistakes, missing, correct_exp, tip = "", "", "", ""

            for line in response.split("\n"):
                if "SCORE:" in line or "Score:" in line:
                    m = re.search(r"(\d+)/10", line)
                    if m:
                        score = int(m.group(1))
                elif "MISTAKES:" in line:
                    mistakes = line.replace("MISTAKES:", "").strip()
                elif "MISSING CONCEPTS:" in line:
                    missing = line.replace("MISSING CONCEPTS:", "").strip()
                elif "CORRECT EXPLANATION:" in line:
                    correct_exp = line.replace("CORRECT EXPLANATION:", "").strip()
                elif "STUDY TIP:" in line:
                    tip = line.replace("STUDY TIP:", "").strip()

            with st.container(border=True):
                st.markdown(
                    "<div style='background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"
                    "padding:12px 16px;border-radius:8px;color:#10B981;font-weight:500;margin-bottom:16px;'>"
                    "✨ Analysis Complete!</div>",
                    unsafe_allow_html=True
                )
                st.subheader(f"📊 Score: {score}/10")
                safe_progress = min(max(float(score) / 10.0, 0.0), 1.0)
                st.progress(safe_progress)

                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("**❌ Mistakes Made**")
                    st.write(mistakes or "No major mistakes identified")
                    st.markdown("**🤔 Missing Concepts**")
                    st.write(missing or "All key concepts covered")
                with col_b:
                    st.markdown("**✅ Correct Answer**")
                    st.write(correct_exp or "See full response above")
                    st.markdown("**💡 Study Tip**")
                    st.write(tip or "Keep practicing similar questions")

                st.divider()
                with st.expander("📄 View Full AI Response"):
                    st.write(response)

            try:
                save_mistake_analysis(user["id"], question, student_answer, response, score)
            except Exception:
                pass
        else:
            st.warning("Please enter both the question and your answer.")
