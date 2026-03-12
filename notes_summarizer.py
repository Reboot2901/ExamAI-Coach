import streamlit as st
from llm_helper import ask_llm
from prompts import notes_summarizer_prompt


def parse_summary(text: str) -> dict:
    parsed = {"summary": "", "key_concepts": "", "important_definitions": "", "quick_revision": ""}
    try:
        if "---SUMMARY---" in text:
            parts = text.split("---SUMMARY---")
            rest = parts[1]
            if "---KEY CONCEPTS---" in rest:
                summary_part, rest = rest.split("---KEY CONCEPTS---", 1)
                parsed["summary"] = summary_part.strip()
                if "---IMPORTANT DEFINITIONS---" in rest:
                    concepts_part, rest = rest.split("---IMPORTANT DEFINITIONS---", 1)
                    parsed["key_concepts"] = concepts_part.strip()
                    if "---QUICK REVISION POINTS---" in rest:
                        defs_part, rev_part = rest.split("---QUICK REVISION POINTS---", 1)
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
    render_page_header("✍️", "Notes Summarizer", "Paste your study notes and get an AI-generated structured summary")

    with st.form("notes_summary_form"):
        notes_input = st.text_area(
            "Notes Content",
            height=250,
            placeholder="Paste your notes here...",
            label_visibility="collapsed",
            key="notes_input_text_area"
        )
        submitted = st.form_submit_button("Summarize Notes", type="primary", use_container_width=True)

    if submitted:
        if notes_input.strip():
            with st.spinner("Analyzing and summarizing your notes..."):
                prompt = notes_summarizer_prompt(notes_input)
                response, _ = ask_llm(prompt)
            st.session_state.notes_parsed_data = parse_summary(response)
        else:
            st.warning("Please paste some notes.")

    if "notes_parsed_data" in st.session_state:
        parsed = st.session_state.notes_parsed_data
        st.markdown(
            "<div style='background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"
            "padding:12px 16px;border-radius:8px;color:#10B981;font-weight:500;margin-bottom:16px;'>"
            "✨ Summary Generated!</div>",
            unsafe_allow_html=True
        )

        if parsed.get("summary"):
            with st.container(border=True):
                st.subheader("📝 Summary")
                st.write(parsed["summary"])
        if parsed.get("key_concepts"):
            with st.container(border=True):
                st.subheader("💡 Key Concepts")
                st.write(parsed["key_concepts"])
        if parsed.get("important_definitions"):
            with st.container(border=True):
                st.subheader("📚 Important Definitions")
                st.write(parsed["important_definitions"])
        if parsed.get("quick_revision"):
            with st.container(border=True):
                st.subheader("⚡ Quick Revision Points")
                st.write(parsed["quick_revision"])

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📥 Download Summary",
                data="\n\n".join([f"SUMMARY:\n{parsed.get('summary', '')}",
                                  f"KEY CONCEPTS:\n{parsed.get('key_concepts', '')}",
                                  f"DEFINITIONS:\n{parsed.get('important_definitions', '')}",
                                  f"REVISION:\n{parsed.get('quick_revision', '')}"]),
                file_name="summary.txt",
                mime="text/plain",
                type="secondary",
                use_container_width=True
            )
        with col2:
            if st.button("🗑️ Clear", key="clear_notes_btn", type="secondary", use_container_width=True):
                del st.session_state.notes_parsed_data
                st.session_state.notes_input_text_area = ""
                st.rerun()
