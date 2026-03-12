import streamlit as st
from llm_helper import ask_llm
from prompts import notes_summarizer_prompt

def parse_summary(text):
    parsed = {
        "summary": "",
        "key_concepts": "",
        "important_definitions": "",
        "quick_revision": ""
    }
    
    try:
        if "---SUMMARY---" in text:
            parts = text.split("---SUMMARY---")
            rest = parts[1]
            if "---KEY CONCEPTS---" in rest:
                summary_part, rest = rest.split("---KEY CONCEPTS---")
                parsed["summary"] = summary_part.strip()
                
                if "---IMPORTANT DEFINITIONS---" in rest:
                    concepts_part, rest = rest.split("---IMPORTANT DEFINITIONS---")
                    parsed["key_concepts"] = concepts_part.strip()
                    
                    if "---QUICK REVISION POINTS---" in rest:
                        defs_part, rev_part = rest.split("---QUICK REVISION POINTS---")
                        parsed["important_definitions"] = defs_part.strip()
                        parsed["quick_revision"] = rev_part.strip()
                    else:
                        parsed["important_definitions"] = rest.strip()
                else:
                    parsed["key_concepts"] = rest.strip()
            else:
                parsed["summary"] = rest.strip()
        else:
            parsed["summary"] = text.strip()
    except Exception:
        parsed["summary"] = text.strip()
        
    return parsed

def notes_summarizer():
    from ui_styles import render_page_header
    render_page_header("✍️", "Notes Summarizer", "Paste your study notes and get a clean AI-generated summary with key concepts.")

    with st.form("notes_summary_form"):
        notes_input = st.text_area(
            "Notes Content", 
            height=250, 
            placeholder="Paste your notes here to generate a summary, key concepts, and important points.",
            label_visibility="collapsed",
            key="notes_input_text_area"
        )
        submitted = st.form_submit_button("Summarize Notes", type="primary", use_container_width=True)

    if submitted:
        if notes_input.strip():
            with st.spinner("Analyzing and summarizing your notes..."):
                prompt = notes_summarizer_prompt(notes_input)
                response = ask_llm(prompt)
                
            st.session_state.notes_parsed_data = parse_summary(response)
        else:
            st.warning("Please paste some notes to summarize.")
            
    if "notes_parsed_data" in st.session_state:
        parsed_data = st.session_state.notes_parsed_data
        
        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
        st.markdown("<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px 16px; border-radius: 8px; color: #10B981; font-weight: 500; font-size: 0.95rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;'>✨ Summary Generated Successfully!</div>", unsafe_allow_html=True)
        
        # Output sections in glass panels
        if parsed_data.get("summary"):
            with st.container(border=True):
                st.subheader("📝 Summary")
                st.write(parsed_data["summary"])

        if parsed_data.get("key_concepts"):
            with st.container(border=True):
                st.subheader("💡 Key Concepts")
                st.write(parsed_data["key_concepts"])

        if parsed_data.get("important_definitions"):
            with st.container(border=True):
                st.subheader("📚 Important Definitions")
                st.write(parsed_data["important_definitions"])

        if parsed_data.get("quick_revision"):
            with st.container(border=True):
                st.subheader("⚡ Quick Revision Points")
                st.write(parsed_data["quick_revision"])
            
        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 Copy Summary", key="copy_btn", type="secondary", use_container_width=True):
                st.toast("Highlight the text to copy it to your clipboard!")
        with col2:
            if st.button("🗑️ Clear Notes", key="clear_btn", type="secondary", use_container_width=True):
                if "notes_parsed_data" in st.session_state:
                    del st.session_state.notes_parsed_data
                if "notes_input_text_area" in st.session_state:
                    st.session_state.notes_input_text_area = ""
                st.rerun()
