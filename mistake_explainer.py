import streamlit as st
import re
from database import save_mistake_analysis

def mistake_explainer(user):
    from ui_styles import render_page_header
    render_page_header("📝", "Mistake Explainer", "Get detailed AI feedback on your answers with scores and clear improvement tips")

    with st.form("mistake_form"):
        col1, col2 = st.columns(2)
        with col1:
            question = st.text_area("Question", height=150, placeholder="Paste the exam question here...")
        with col2:
            student_answer = st.text_area("Your Answer", height=150, placeholder="Type your answer here...")
        
        submitted = st.form_submit_button("Analyze Answer", type="primary", use_container_width=True)
    
    if submitted:
        if question and student_answer:
            with st.spinner("Analyzing your answer..."):
                try:
                    from llm_helper import ask_llm
                except Exception as e:
                    st.error(f"LLM helper import failed: {e}")
                    st.stop()
                    
                prompt = f"""
You are an exam coach.

Analyze the student's mistake below.

Question:
{question}

Student response:
{student_answer}

Return:
1. What the mistake is
2. Why it is incorrect
3. The correct concept or answer
4. A simple way to remember it
"""
                response = ask_llm(prompt)

            # Parse response
            lines = response.split('\n')
            score = 0
            mistakes = ""
            missing = ""
            correct_exp = ""
            tip = ""

            for line in lines:
                if "SCORE:" in line or "Score:" in line:
                    match = re.search(r'(\d+)/10', line)
                    if match:
                        score = int(match.group(1))
                elif "MISTAKES:" in line:
                    mistakes = line.replace("MISTAKES:", "").strip()
                elif "MISSING CONCEPTS:" in line:
                    missing = line.replace("MISSING CONCEPTS:", "").strip()
                elif "CORRECT EXPLANATION:" in line:
                    correct_exp = line.replace("CORRECT EXPLANATION:", "").strip()
                elif "STUDY TIP:" in line:
                    tip = line.replace("STUDY TIP:", "").strip()

            # Display results in a unified glass container
            with st.container(border=True):
                st.markdown("<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px 16px; border-radius: 8px; color: #10B981; font-weight: 500; font-size: 0.95rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;'>✨ Analysis Complete!</div>", unsafe_allow_html=True)

                st.subheader(f"📊 Score: {score}/10")
                
                # Ensure safe bounds between 0.0 and 1.0 to prevent Streamlit crashes
                safe_progress = min(max(float(score) / 10.0, 0.0), 1.0)
                st.progress(safe_progress)
                
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.markdown("<h3 style='color: #F87171; font-size: 1.1rem; margin-bottom: 8px;'>❌ Mistakes Made</h3>", unsafe_allow_html=True)
                    st.write(mistakes or "No major mistakes identified")
                    
                    st.markdown("<h3 style='color: #FBBF24; font-size: 1.1rem; margin-top: 16px; margin-bottom: 8px;'>🤔 Missing Concepts</h3>", unsafe_allow_html=True)
                    st.write(missing or "All key concepts covered")

                with res_col2:
                    st.markdown("<h3 style='color: #34D399; font-size: 1.1rem; margin-bottom: 8px;'>✅ Correct Answer</h3>", unsafe_allow_html=True)
                    st.write(correct_exp or "Answer analysis provided above")
                    
                    st.markdown("<h3 style='color: #60A5FA; font-size: 1.1rem; margin-top: 16px; margin-bottom: 8px;'>💡 Study Tip</h3>", unsafe_allow_html=True)
                    st.write(tip or "Keep practicing similar questions")

            try:
                save_mistake_analysis(user["id"], question, student_answer, response, score)
            except Exception as e:
                pass
        else:
            st.warning("Please enter both question and answer.")
