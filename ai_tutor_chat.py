import streamlit as st
from llm_helper import ask_llm
from prompts import chat_prompt
from database import save_chat_message
from search_helper import should_use_live_search, ask_gemini_grounded


def ai_tutor_chat(user):
    from ui_styles import render_page_header
    render_page_header("🤖", "AI Tutor Chat", "Chat with your personal AI study tutor — available 24/7")

    # Controls row
    col_toggle, _ = st.columns([1, 4])
    with col_toggle:
        use_live_search = st.toggle(
            "Live Search 🌐",
            value=st.session_state.get("use_live_search", False),
            help="Enable to use live web grounding for real-time questions."
        )
        st.session_state.use_live_search = use_live_search

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show empty state
    if not st.session_state.messages:
        st.markdown("""
        <div style="text-align:center; margin-top:80px; margin-bottom:60px;">
            <div style="font-size:3rem; margin-bottom:12px;">🤖</div>
            <h3 style="color:#F8FAFC; font-family:'Outfit',sans-serif; font-weight:600; margin-bottom:8px;">
                How can I help you study today?
            </h3>
            <p style="color:#94A3B8; font-size:0.95rem;">Ask your first question to get started.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask your doubt..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    # Generate AI response for last user message
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        prompt = st.session_state.messages[-1]["content"]

        with st.chat_message("assistant"):
            placeholder = st.empty()
            sources_placeholder = st.empty()
            placeholder.markdown("_Thinking..._ ⏳")

            full_response = ""
            sources = []

            # Decide live search or standard
            is_live = st.session_state.get("use_live_search", False) or should_use_live_search(prompt)

            if is_live:
                placeholder.markdown("_Searching via live Gemini..._ 🌐")
                full_response, sources = ask_gemini_grounded(prompt)
            else:
                # Build history context
                paired_history = []
                temp_user = ""
                for m in st.session_state.messages[:-1]:
                    if m["role"] == "user":
                        temp_user = m["content"]
                    elif m["role"] == "assistant":
                        paired_history.append({"user": temp_user, "assistant": m["content"]})
                        temp_user = ""
                ai_prompt = chat_prompt(prompt, paired_history)
                full_response, _ = ask_llm(ai_prompt)

            placeholder.markdown(full_response)

            # Show sources
            if sources:
                sources_html = "<div style='margin-top:12px;'><span style='font-size:0.8rem;font-weight:600;color:#94A3B8;text-transform:uppercase;letter-spacing:0.5px;'>Sources</span></div>"
                for s in sources:
                    sources_html += f"""<a href="{s['url']}" target="_blank" style="text-decoration:none;display:block;margin-bottom:6px;">
                        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:8px 12px;">
                            <span style="color:#60A5FA;font-size:0.88rem;">{s['title']}</span>
                        </div></a>"""
                sources_placeholder.markdown(sources_html, unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

        try:
            save_chat_message(user["id"], "user", prompt)
            save_chat_message(user["id"], "assistant", full_response)
        except Exception:
            pass
