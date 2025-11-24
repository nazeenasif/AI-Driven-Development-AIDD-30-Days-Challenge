# utils/pdf_reader.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using PyPDF2.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
