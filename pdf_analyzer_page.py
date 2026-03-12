import streamlit as st
from pdf_helper import extract_text_from_pdf
from llm_helper import ask_llm
from prompts import pdf_analysis_prompt
from database import save_pdf_analysis

def pdf_analyzer_page(user):
    from ui_styles import render_page_header
    render_page_header("📄", "PDF Analyzer", "Analyze question papers to instantly identify key recurring exam topics")

    with st.form("pdf_analyzer_form"):
        uploaded_file = st.file_uploader("Upload question paper PDF", type="pdf")
        submitted = st.form_submit_button("Analyze PDF", type="primary", use_container_width=True)
    
    if submitted:
        if uploaded_file:
            with st.spinner("Extracting text from PDF..."):
                text = extract_text_from_pdf(uploaded_file)

            if text and not text.startswith("Error"):
                with st.spinner("Analyzing content..."):
                    prompt = pdf_analysis_prompt(text)
                    analysis = ask_llm(prompt)

                with st.container(border=True):
                    st.markdown("<div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px 16px; border-radius: 8px; color: #10B981; font-weight: 500; font-size: 0.95rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;'>✨ Analysis Complete!</div>", unsafe_allow_html=True)
                    st.subheader("Analysis Results")
                    st.write(analysis)

                try:
                    save_pdf_analysis(user["id"], uploaded_file.name, analysis)
                except Exception as e:
                    pass
            else:
                st.error("Failed to extract text from PDF. Please check the file.")
        else:
            st.warning("Please upload a PDF file.")
