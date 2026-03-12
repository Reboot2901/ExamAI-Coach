import streamlit as st
import re
from llm_helper import ask_llm
from prompts import flashcard_generator_prompt

def generate_flashcards(topic):
    """Generate flashcards for a topic"""
    prompt = flashcard_generator_prompt(topic)
    response = ask_llm(prompt)

    # Parse the response to extract Q&A pairs
    flashcards = []
    lines = response.split('\n')
    current_q = None
    current_a = None

    for line in lines:
        line = line.strip()
        if line.startswith('Q:') or line.startswith('Question:'):
            if current_q and current_a:
                flashcards.append({"question": current_q, "answer": current_a})
            current_q = line.replace('Q:', '').replace('Question:', '').strip()
            current_a = None
        elif line.startswith('A:') or line.startswith('Answer:'):
            current_a = line.replace('A:', '').replace('Answer:', '').strip()

    if current_q and current_a:
        flashcards.append({"question": current_q, "answer": current_a})

    return flashcards[:10]  # Return up to 10 flashcards

def display_flashcards():
    """Display flashcard generator interface"""
    from ui_styles import render_page_header
    render_page_header("🃏", "Flashcards", "Generate intelligent flashcards for rapid review and active recall memorization")

    with st.form("flashcard_gen_form"):
        topic = st.text_input("Enter a topic to generate flashcards:")
        submitted = st.form_submit_button("Generate Flashcards", type="primary", use_container_width=True)

    if submitted:
        if topic:
            with st.spinner("Generating flashcards..."):
                flashcards = generate_flashcards(topic)

            if flashcards:
                with st.container(border=True):
                    st.markdown(f"<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px 16px; border-radius: 8px; color: #10B981; font-weight: 500; font-size: 0.95rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;'>✨ Generated {{len(flashcards)}} flashcards!</div>", unsafe_allow_html=True)

                    for i, card in enumerate(flashcards):
                        with st.expander(f"Flashcard {i+1}: {card['question'][:50]}..."):
                            st.write(f"**Question:** {card['question']}")
                            st.write(f"**Answer:** {card['answer']}")
            else:
                st.error("Failed to generate flashcards. Please try again.")
        else:
            st.warning("Please enter a topic.")