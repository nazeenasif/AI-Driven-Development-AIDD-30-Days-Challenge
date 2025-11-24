import sys
import os
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from agent.agent_core import agent  # LLM Agent import

# -------------------
# OpenRouter API Config
# -------------------
OPENROUTER_API_KEY = "[Your_API_key]"  # <-- Replace with your OpenRouter API key
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-2.5-flash-lite"  # ✅ Valid model

# -------------------
# Quiz Generator
# -------------------
def generate_quiz(file_path):
    """
    Generates a quiz using OpenRouter LLM based on the full PDF content.
    """
    raw_text = extract_text_from_pdf(file_path)
    if not raw_text:
        return "❌ Could not extract text from PDF to generate quiz."

    cleaned_text = clean_text(raw_text)

    prompt = f"""
You are an educational quiz generator.

Read the following PDF text and create a quiz strictly based on the content.

TEXT:
{cleaned_text}

Generate:
- 5 MCQs (each with A/B/C/D options + correct answer)
- 2 True/False questions
- 2 Short questions

Keep questions clear and accurate.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "pdf-quiz-generator"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 600
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=data)
        response.raise_for_status()
        res_json = response.json()
        quiz_text = res_json["choices"][0]["message"]["content"]
        return quiz_text

    except Exception as e:
        # Print full response for debugging
        return f"❌ Quiz generation failed: {e}\n\nResponse:\n{response.text if 'response' in locals() else ''}"
