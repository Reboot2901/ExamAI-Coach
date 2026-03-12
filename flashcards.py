import streamlit as st
import re
from llm_helper import ask_llm
from prompts import flashcard_generator_prompt


def generate_flashcards(topic: str):
    prompt = flashcard_generator_prompt(topic)
    response, _ = ask_llm(prompt)

    flashcards = []
    lines = response.split("\n")
    current_q, current_a = None, None

    for line in lines:
        line = line.strip()
        if line.startswith("Q:") or line.lower().startswith("question:"):
            if current_q and current_a:
                flashcards.append({"question": current_q, "answer": current_a})
            current_q = re.sub(r"^(Q:|question:)", "", line, flags=re.IGNORECASE).strip()
            current_a = None
        elif line.startswith("A:") or line.lower().startswith("answer:"):
            current_a = re.sub(r"^(A:|answer:)", "", line, flags=re.IGNORECASE).strip()

    if current_q and current_a:
        flashcards.append({"question": current_q, "answer": current_a})

    return flashcards[:10]


def display_flashcards():
    from ui_styles import render_page_header
    render_page_header("🃏", "Flashcards", "Generate intelligent flashcards for rapid review and active recall")

    with st.form("flashcard_gen_form"):
        topic = st.text_input("Enter a topic to generate flashcards:", placeholder="e.g., Photosynthesis, Binary Search...")
        submitted = st.form_submit_button("Generate Flashcards", type="primary", use_container_width=True)

    if submitted:
        if topic.strip():
            with st.spinner("Generating flashcards..."):
                flashcards = generate_flashcards(topic)

            if flashcards:
                st.markdown(
                    f"<div style='background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"
                    f"padding:12px 16px;border-radius:8px;color:#10B981;font-weight:500;margin-bottom:16px;'>"
                    f"✨ Generated {len(flashcards)} flashcards!</div>",
                    unsafe_allow_html=True
                )
                for i, card in enumerate(flashcards):
                    with st.expander(f"📇 Card {i+1}: {card['question'][:50]}{'...' if len(card['question']) > 50 else ''}"):
                        st.markdown(f"**Question:** {card['question']}")
                        st.markdown(f"**Answer:** {card['answer']}")
            else:
                st.warning("Could not parse flashcards. Please try a different topic or try again.")
        else:
            st.warning("Please enter a topic.")