import os
import sys
import requests
from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# IMPORTANT → Use your OpenRouter API key here
OPENROUTER_API_KEY = "[Your_API_key]"  # <- Replace this

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-2.5-flash-lite"  # Gemini model via OpenRouter


def summarize_pdf(file_path):
    """
    Reads a PDF, extracts text, cleans it,
    and generates a summary using Gemini LLM via OpenRouter API.
    """

    # Step 1 → Extract text
    raw_text = extract_text_from_pdf(file_path)
    if not raw_text:
        return "❌ Could not extract text from PDF."

    # Step 2 → Clean text
    cleaned_text = clean_text(raw_text)

    # Step 3 → Generate summary using Gemini LLM
    prompt = f"""
    Summarize the following text clearly, concisely, and in simple language.
    Avoid unnecessary details. Keep the structure clean.

    Text:
    {cleaned_text}
    """

    # **** Required OpenRouter headers ****
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",   # Required by OpenRouter
        "X-Title": "pdf-summarizer-app"       # Required by OpenRouter
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 500,
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=data)
        response.raise_for_status()  # raise errors

        res_json = response.json()
        summary = res_json["choices"][0]["message"]["content"]

        return f"📄 **Summary Generated Successfully**\n\n{summary}"

    except Exception as e:
        return f"❌ Summarization failed: {e}\n\nResponse Text:\n{response.text}"



if __name__ == "__main__":
    # Test run
    file_path = "sample.pdf"  # replace with your PDF path
    print(summarize_pdf(file_path))
