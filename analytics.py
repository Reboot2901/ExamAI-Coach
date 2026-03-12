import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database import get_user_stats, get_user_data

def display_dashboard(user):
    """Display user dashboard with analytics"""
    from ui_styles import render_page_header
    render_page_header("📈", "Analytics Dashboard", f"Welcome back, {user['name']}! View your performance analytics and track deep learning progress.")

    stats = get_user_stats(user["id"])

    # Key metrics
    if stats["total_mistakes"] > 0 or stats["total_quizzes"] > 0 or stats["total_vivas"] > 0 or stats["total_chats"] > 0:
        with st.container(border=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Mistake Analyses", stats["total_mistakes"])
            with col2:
                st.metric("Viva Sessions", stats["total_vivas"])
            with col3:
                st.metric("AI Chat Messages", stats["total_chats"])
            with col4:
                st.metric("Quizzes Taken", stats["total_quizzes"])

        # Charts
        with st.container(border=True):
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Quiz Performance")
                if stats["total_quizzes"] > 0:
                    user_data = get_user_data(user["id"])
                    
                    # Extract real scores from user history
                    scores = []
                    for q in user_data.get("quiz_scores", []):
                        percent = (q["score"] / q["total"]) * 100 if q["total"] > 0 else 0
                        scores.append(percent)
                        
                    quiz_data = pd.DataFrame({
                        "Quiz": [f"Quiz {i+1}" for i in range(len(scores))],
                        "Score": scores
                    })
                    fig = px.line(quiz_data, x="Quiz", y="Score", title="Quiz Scores Over Time")
                    st.plotly_chart(fig)
                else:
                    st.markdown("<div style='background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(14, 165, 233, 0.2); padding: 12px 16px; border-radius: 8px; color: #38bdf8; font-weight: 500; font-size: 0.95rem; display: flex; align-items: center; gap: 8px;'>ℹ️ No quizzes taken yet</div>", unsafe_allow_html=True)

            with col2:
                st.subheader("Activity Overview")
                activity_data = pd.DataFrame({
                    "Activity": ["Mistakes", "Vivas", "Chats", "Quizzes", "PDFs"],
                    "Count": [stats["total_mistakes"], stats["total_vivas"], stats["total_chats"], stats["total_quizzes"], stats["total_pdfs"]]
                })
                fig = px.pie(activity_data, values="Count", names="Activity", title="Activity Distribution")
                st.plotly_chart(fig)

        with st.container(border=True):
            st.subheader("Recent Activity")
            st.write("• Completed mistake analysis")
            st.write("• Participated in viva session")
            st.write("• Generated flashcards")
            st.write("• Took quiz on Python")
    else:
        st.markdown("<div style='background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(14, 165, 233, 0.2); padding: 12px 16px; border-radius: 8px; color: #38bdf8; font-weight: 500; font-size: 0.95rem; margin-bottom: 24px; display: flex; align-items: center; gap: 8px;'>ℹ️ No analytics data available yet. Start using the study tools to see your progress here!</div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("Study Tools")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📝 Mistake Explainer", use_container_width=True):
                st.session_state.page = "Mistake Explainer"
                st.rerun()
        with col2:
            if st.button("🎤 Viva Examiner", use_container_width=True):
                st.session_state.page = "Viva Practice"
                st.rerun()
        with col3:
            if st.button("🤖 AI Tutor Chat", use_container_width=True):
                st.session_state.page = "AI Tutor"
                st.rerun()