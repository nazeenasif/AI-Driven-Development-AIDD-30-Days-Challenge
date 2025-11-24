# utils/text_cleaner.py
import re

def clean_text(text):
    """
    Cleans text by removing common PDF artifacts like page numbers,
    headers/footers, excessive whitespace, and hyphenation.
    """
    if not text:
        return ""

    # Remove common headers/footers (can be improved with more specific patterns)
    # This is a very basic example, more robust cleaning might be needed
    text = re.sub(r'(\n\s*\d+\s*\n)|(\n\s*[A-Za-z]+\s*\n)', '\n', text) # Remove standalone numbers or words on a line
    
    # Remove hyphenation at the end of lines
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)

    # Replace multiple newlines with a single one (or two for paragraph separation)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Remove excessive whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Strip leading/trailing whitespace from each line
    text = "\n".join([line.strip() for line in text.split('\n')])
    
    return text.strip()

