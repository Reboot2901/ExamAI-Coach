import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard(user):
    # Premium Hero Section
    st.markdown("""
        <div style="padding: 32px 0 0 0;">
            <h1 class="hero-title">Welcome to <span class="gradient-text">ExamAI Coach</span></h1>
            <p class="hero-subtitle">Your AI-powered study companion safely guiding your exam preparation.</p>
        </div>
    """, unsafe_allow_html=True)

    # Tool cards
    tools = [
        {
            "name": "Mistake Explainer",
            "icon": "📝",
            "description": "Get detailed AI feedback on your answers with scores and clear improvement tips.",
            "page": "Mistake Explainer",
            "color_class": "theme-indigo-violet"
        },
        {
            "name": "Viva Practice",
            "icon": "🎤",
            "description": "Practice viva voce examinations with real-time expert evaluation and scoring.",
            "page": "Viva Practice",
            "color_class": "theme-violet-magenta"
        },
        {
            "name": "Doubt Predictor",
            "icon": "🔮",
            "description": "Discover common student doubts and anticipate potential exam mistakes easily.",
            "page": "Doubt Predictor",
            "color_class": "theme-cyan-blue"
        },
        {
            "name": "AI Tutor",
            "icon": "🤖",
            "description": "Chat with an advanced AI tutor for personalized 24/7 learning support.",
            "page": "AI Tutor",
            "color_class": "theme-emerald-teal-tut"
        },
        {
            "name": "Flashcards",
            "icon": "🃏",
            "description": "Generate intelligent flashcards for rapid review and active recall memorization.",
            "page": "Flashcards",
            "color_class": "theme-amber-coral"
        },
        {
            "name": "Quiz Generator",
            "icon": "📊",
            "description": "Create automated MCQ quizzes to test your knowledge gaps instantly.",
            "page": "Quiz Generator",
            "color_class": "theme-magenta-purple"
        },
        {
            "name": "Study Planner",
            "icon": "📅",
            "description": "Get highly personalized study plans optimized for your exact exam dates.",
            "page": "Study Planner",
            "color_class": "theme-indigo-purple"
        },
        {
            "name": "Notes Summarizer",
            "icon": "✍️",
            "description": "Instantly summarize long notes into key bullet points.",
            "page": "Notes Summarizer",
            "color_class": "theme-teal-cyan"
        },
        {
            "name": "PDF Analyzer",
            "icon": "📄",
            "description": "Analyze question papers to instantly identify key recurring exam topics.",
            "page": "PDF Analyzer",
            "color_class": "theme-violet-blue"
        },
        {
            "name": "Analytics",
            "icon": "📈",
            "description": "View performance analytics and track your learning progress.",
            "page": "Analytics",
            "color_class": "theme-emerald-teal"
        }
    ]

    # Display tool cards in a premium grid layout (3 Columns)
    cols = st.columns(3)
    for i, tool in enumerate(tools):
        with cols[i % 3]:
            # The entire card is designed as a single interactive element via CSS (.premium-card)
            # We use an invisible streamlit button layered over it to handle clicks.
            st.markdown(f"""
            <div class="premium-card {tool['color_class']}">
                <div class="card-icon-container">{tool['icon']}</div>
                <h3>{tool['name']}</h3>
                <p>{tool['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Invisible absolute-positioned button wrapper
            st.markdown('<div class="card-button-wrapper">', unsafe_allow_html=True)
            if st.button(f"Go {tool['name']}", key=f"btn_{tool['name']}", use_container_width=True):
                st.session_state.page = tool['page']
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # Progress section
    st.markdown("<h2 style='font-family: Poppins, sans-serif; font-weight: 600; margin-top: 32px; margin-bottom: 24px;'>📈 Performance Analytics</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Questions Analyzed", "12")
    with col2:
        st.metric("Viva Sessions", "8")
    with col3:
        st.metric("Quizzes Mastered", "5")

    # Sample progress chart

    progress_data = pd.DataFrame({
        "Quiz Phase": ["Diagnostic", "Week 1", "Week 2", "Midterm Prep", "Final Review"],
        "Score": [65, 72, 85, 88, 96]
    })
    
    fig = px.area(progress_data, x="Quiz Phase", y="Score", title="Overall Learning Trajectory")
    
    # Premium Plotly Styling
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#9CA3AF",
        title_font_color="#FFFFFF",
        title_font_family="Poppins",
        title_font_size=20,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    fig.update_traces(
        line_color="#00d2ff",
        fillcolor="rgba(0, 210, 255, 0.1)"
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.05)", zeroline=False)
    
    st.plotly_chart(fig, use_container_width=True)
