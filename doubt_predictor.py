import streamlit as st
from llm_helper import ask_llm
from prompts import doubt_prompt


def doubt_predictor():
    from ui_styles import render_page_header
    render_page_header("🔮", "Doubt Predictor", "Discover common student doubts and anticipate potential exam mistakes")

    with st.form("doubt_form"):
        topic = st.text_input(
            "Enter a topic",
            placeholder="e.g., Photosynthesis, Newton's Laws, Binary Trees..."
        )
        submitted = st.form_submit_button("Predict Doubts", type="primary", use_container_width=True)

    if submitted:
        if topic.strip():
            with st.spinner("Predicting common doubts..."):
                prompt = doubt_prompt(topic)
                response, _ = ask_llm(prompt)

            with st.container(border=True):
                st.markdown(
                    "<div style='background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"
                    "padding:12px 16px;border-radius:8px;color:#10B981;font-weight:500;margin-bottom:16px;'>"
                    "✨ Analysis Complete!</div>",
                    unsafe_allow_html=True
                )
                st.subheader(f"Common Doubts in: {topic}")
                st.write(response)
        else:
            st.warning("Please enter a topic to analyze.")
