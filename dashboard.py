import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_user_stats


def show_dashboard(user):
    # Hero
    st.markdown("""
    <div style="padding: 2rem 0 1rem;">
        <h1 class="hero-title">Welcome to <span class="gradient-text">ExamAI Coach</span></h1>
        <p class="hero-subtitle">Your AI-powered study companion — smarter exam prep, better results.</p>
    </div>
    """, unsafe_allow_html=True)

    tools = [
        {"name": "Mistake Explainer",  "icon": "📝", "desc": "Get detailed AI feedback with scores and improvement tips.", "page": "Mistake Explainer",  "theme": "theme-indigo-violet"},
        {"name": "Viva Practice",      "icon": "🎤", "desc": "Practice viva examinations with real-time AI evaluation.", "page": "Viva Practice",      "theme": "theme-violet-magenta"},
        {"name": "Doubt Predictor",    "icon": "🔮", "desc": "Discover common doubts and anticipate exam mistakes.",    "page": "Doubt Predictor",    "theme": "theme-cyan-blue"},
        {"name": "AI Tutor",           "icon": "🤖", "desc": "Chat with your 24/7 personalized AI study tutor.",       "page": "AI Tutor",           "theme": "theme-emerald-teal-tut"},
        {"name": "Flashcards",         "icon": "🃏", "desc": "Generate smart flashcards for rapid active recall.",    "page": "Flashcards",         "theme": "theme-amber-coral"},
        {"name": "Quiz Generator",     "icon": "📊", "desc": "Create MCQ quizzes to test your knowledge gaps.",       "page": "Quiz Generator",     "theme": "theme-magenta-purple"},
        {"name": "Study Planner",      "icon": "📅", "desc": "Personalized study plans for your exact exam dates.",    "page": "Study Planner",      "theme": "theme-indigo-purple"},
        {"name": "Notes Summarizer",   "icon": "✍️", "desc": "AI-generated structured summaries from your notes.",    "page": "Notes Summarizer",   "theme": "theme-teal-cyan"},
        {"name": "PDF Analyzer",       "icon": "📄", "desc": "Identify key topics from your question paper PDFs.",    "page": "PDF Analyzer",       "theme": "theme-violet-blue"},
        {"name": "Analytics",          "icon": "📈", "desc": "Track your performance and learning progress over time.","page": "Analytics",          "theme": "theme-emerald-teal"},
    ]

    st.markdown("<h2 style='font-size:1.4rem;font-weight:700;margin:2rem 0 1rem;color:#F8FAFC;'>🚀 Your Learning Tools</h2>", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, tool in enumerate(tools):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="premium-card {tool['theme']}">
                <div class="card-icon-container">{tool['icon']}</div>
                <h3>{tool['name']}</h3>
                <p>{tool['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="card-button-wrapper">', unsafe_allow_html=True)
            if st.button(f"Open {tool['name']}", key=f"card_{tool['name']}", use_container_width=True):
                st.session_state.page = tool["page"]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # Stats section
    st.markdown("<h2 style='font-size:1.4rem;font-weight:700;margin:2.5rem 0 1rem;color:#F8FAFC;'>📈 Performance Overview</h2>", unsafe_allow_html=True)

    try:
        stats = get_user_stats(user["id"])
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Mistakes Analyzed", stats["total_mistakes"])
        c2.metric("Viva Sessions", stats["total_vivas"])
        c3.metric("Quizzes Taken", stats["total_quizzes"])
        c4.metric("PDFs Analyzed", stats["total_pdfs"])
    except Exception:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Mistakes Analyzed", 0)
        c2.metric("Viva Sessions", 0)
        c3.metric("Quizzes Taken", 0)
        c4.metric("PDFs Analyzed", 0)

    # Sample progress chart
    progress_data = pd.DataFrame({
        "Session": ["Start", "Week 1", "Week 2", "Midterm", "Final"],
        "Score": [60, 70, 82, 88, 95]
    })
    fig = px.area(progress_data, x="Session", y="Score", title="Learning Progress Trajectory")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font_color="#9CA3AF", title_font_color="#FFFFFF",
        title_font_family="Outfit", title_font_size=18,
        margin=dict(l=20, r=20, t=48, b=20)
    )
    fig.update_traces(line_color="#818cf8", fillcolor="rgba(129,140,248,0.1)")
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False)
    st.plotly_chart(fig, use_container_width=True)
