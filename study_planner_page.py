import streamlit as st
from study_planner import generate_study_plan, display_study_plan

def study_planner_page():
    from ui_styles import render_page_header
    render_page_header("📅", "Study Planner", "Get personalized study plans optimized for your exact exam dates")

    with st.form("study_planner_form"):
        col1, col2 = st.columns(2)
        with col1:
            subject = st.text_input("Subject", placeholder="e.g., Mathematics, Physics, etc.")
        with col2:
            days = st.number_input("Days until exam", min_value=1, max_value=365, value=7)
        submitted = st.form_submit_button("Generate Study Plan", type="primary", use_container_width=True)
        
    if submitted:
        if subject:
            with st.spinner("Creating personalized study plan..."):
                plan = generate_study_plan(subject, days)
                
            with st.container(border=True):
                display_study_plan(plan, subject, days)
        else:
            st.warning("Please enter a subject.")
