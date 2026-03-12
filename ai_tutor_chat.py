import streamlit as st
import json
import requests
from llm_helper import MODEL_NAME, OLLAMA_API_URL, ask_llm
from prompts import chat_prompt
from database import save_chat_message
from search_helper import should_use_live_search

def ai_tutor_chat(user):
    from ui_styles import render_page_header
    render_page_header("🤖", "AI Tutor Chat", "Chat with your personal AI study tutor for personalized 24/7 learning support")
    
    # Configure mode section
    cols = st.columns([1, 4])
    with cols[0]:
        st.session_state.use_live_search = st.toggle("Live Web Grounded AI 🌐", value=st.session_state.get("use_live_search", True), help="Toggle to use Gemini with Google Search Grounding for real-time web results.")

    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display empty state if no messages exist
    if len(st.session_state.messages) == 0:
        st.markdown(
            '''
            <div style="text-align: center; margin-top: 100px; margin-bottom: 60px;">
                <div style="font-size: 3rem; margin-bottom: 16px; opacity: 0.8;">🤖</div>
                <h3 style="color: #F8FAFC; font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 1.5rem; margin-bottom: 8px;">
                    How can I help you today?
                </h3>
                <p style="color: #94A3B8; font-size: 0.95rem;">Ask your first question to start learning.</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        # Display chat messages stacked vertically
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

    # Fixed bottom chat input
    if prompt := st.chat_input("Ask your doubt..."):
        # Add and display user message immediately
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Rerun to show user message and trigger assistant response
        st.rerun()

    # If the last message is from the user, generate AI response
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        # Get last user prompt for DB saving and history matching
        prompt = st.session_state.messages[-1]["content"]

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            sources_placeholder = st.empty()
            response_placeholder.markdown("AI Tutor is typing... ⏳")
            
            # Check for toggle or automatic live search triggers
            is_live_search = st.session_state.get("use_live_search", False)
            
            # Auto-detect if it's not strictly disabled
            if not is_live_search and should_use_live_search(prompt):
                is_live_search = True

            grounded_prompt = prompt

            paired_history = []
            temp_user = ""
            # Skip the very last one which is the current prompt
            for m in st.session_state.messages[:-1]:
                if m["role"] == "user":
                    temp_user = m["content"]
                elif m["role"] == "assistant":
                    paired_history.append({"user": temp_user, "assistant": m["content"]})
                    temp_user = ""
                    
            # Send the grounded or default prompt
            ai_prompt = chat_prompt(grounded_prompt, paired_history)
            
            full_response = ""
            
            if is_live_search:
                response_placeholder.markdown("Searching via Google Grounding... 🌐")
                from search_helper import ask_gemini_grounded
                
                # We do not stream grounded Gemini responses in this implementation because metadata might arrive at the end.
                # However we can simulate typing or just show a loading state, then dump response.
                answer, sources = ask_gemini_grounded(prompt)
                full_response = answer
                response_placeholder.markdown(full_response)
                
                # If there are sources from Gemini Grounding, display them below the response
                if len(sources) > 0:
                    sources_html = "<div style='margin-top: 15px; margin-bottom: 5px;'><span style='font-size: 0.8rem; font-weight: 600; text-transform: uppercase; color: #94A3B8; letter-spacing: 0.5px;'>Google Search Grounding Sources</span></div>"
                    for s in sources:
                        sources_html += f"""
                        <a href="{s['url']}" target="_blank" style="text-decoration: none; display: block; margin-bottom: 8px;">
                            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px; transition: all 0.2s ease;">
                                <div style="color: #60A5FA; font-weight: 500; font-size: 0.9rem; margin-bottom: 4px;">{s['title']}</div>
                            </div>
                        </a>
                        """
                    sources_placeholder.markdown(sources_html, unsafe_allow_html=True)
            else:
                # Streaming LLM logic for Ollama
                try:
                    payload = {
                        "model": MODEL_NAME,
                        "prompt": ai_prompt,
                        "stream": True # Enable streaming
                    }
                    
                    with requests.post(OLLAMA_API_URL, json=payload, stream=True, timeout=60) as r:
                        r.raise_for_status()
                        for line in r.iter_lines():
                            if line:
                                chunk = json.loads(line)
                                word = chunk.get("response", "")
                                if word:
                                    full_response = "{}{}".format(full_response, word)
                                response_placeholder.markdown("{}▌".format(full_response))
                                
                                if chunk.get("done"):
                                    break
                                    
                    response_placeholder.markdown(full_response)
                except Exception as e:
                    full_response = f"❌ Error connecting to AI: {str(e)}"
                    response_placeholder.markdown(full_response)
            
        # Append AI message
        st.session_state.messages.append({"role": "assistant", "content": full_response})

        try:
            save_chat_message(user["id"], "user", prompt)
            save_chat_message(user["id"], "assistant", full_response)
        except Exception as e:
            pass
