from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    """
    Extract text content from an uploaded PDF file.

    Args:
        pdf_file: Streamlit uploaded file object

    Returns:
        str: Extracted text from the PDF
    """
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"