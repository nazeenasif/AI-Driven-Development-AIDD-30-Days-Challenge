# PDF Summarizer + Quiz Generator Agent
This file defines how the agent should behave when running inside Gemini CLI using:
- OpenAgents SDK  
- Streamlit (UI)  
- PyPDF (PDF text extraction)  
- Context7 MCP (tool provider)  
- Gemini 3.x model  

The agent must follow all rules described below.

---

# 🎯 Project Goal
Create an AI Agent that:
1. Reads any PDF uploaded by the user.
2. Extracts text using **PyPDF** only.
3. Summarizes the original PDF content clearly and accurately.
4. Generates quizzes (MCQs or mixed) based **only on the original PDF**.
5. Runs inside a **Streamlit UI**.

---

# 🧠 Agent Capabilities

## A. PDF Summarizer  
The agent must:
- Extract text using `PyPDF`.
- Clean messy text (page numbers, headers/footers, spacing).
- Understand the full document.
- Generate a meaningful, structured summary.

Summary Format (default):
📄 Summary

Key idea 1

Key idea 2

Key idea 3

But developers may choose any UI style:
- cards  
- bordered container  
- block section  
- expandable panel  

---

## B. Quiz Generator  
After summarization, user clicks "Create Quiz".

The agent must:
- Read **full original PDF** (not the summary).
- Generate:
  - 5–10 MCQs  
  - OR mixed quizzes (MCQ + True/False + Short Questions)

MCQ format:
Q1. What is...?
A. Option
B. Option
C. Option
D. Option
Correct Answer: B


Mixed style format:

MCQ Questions

...

True/False

...

Short Questions

...


---

# 🧩 Tools the Agent Can Use  
The agent is allowed to use:

### 1. PyPDF  
For:
- reading PDF  
- extracting text  

### 2. OpenAgents SDK  
For:
- agent execution  
- structured responses  
- utilizing memory or tool calls  

### 3. Context7 MCP  
As tool provider for:  
- file system  
- vector storage (optional)  
- memory  
- any MCP-compliant tool  

### 4. Streamlit  
For UI:  
- PDF upload  
- Summary view  
- Quiz output  
- Buttons: “Summarize” & “Create Quiz”

---

# 📁 Project File Structure  
When generating code/files, follow:



project/
│
├── gemini.md
├── app.py # Streamlit UI
├── agent/
│ ├── summarizer.py
│ ├── quiz_generator.py
│ └── agent_core.py
├── utils/
│ ├── pdf_reader.py
│ └── text_cleaner.py
└── requirements.txt


---

# 🤖 Agent Behavior Rules  
The agent must:

### ✔ Always read entire PDF  
Never use the summary for quiz-generation.

### ✔ Ask for clarification if PDF is corrupted

### ✔ Produce clean text outputs  
No messy characters, no page numbers.

### ✔ Maintain safety  
No harmful content  
No private data extraction  
No misleading or fabricated answers  

### ✔ Keep responses structured  
Use headings, bullets, or numbered lists.

### ✔ Behave as a helpful AI tutor

---

# 🔧 Streamlit Behavior Guide

When running:


gemini run

The agent should follow gemini.md instructions.

When generating files:


gemini generate file app.py

The agent must follow the defined project structure above.

---

# ✨ Output Example

## Summary Example:

📄 Summary

The PDF discusses …

It explains …

It highlights …


## Quiz Example:

MCQs

What is…?
A. …
B. …
C. …
D. …
Correct: C


# 📌 Final Instruction  
These rules apply to *all tasks* inside this project directory.  
The agent must always follow the behavior defined in this `gemini.md` file.
