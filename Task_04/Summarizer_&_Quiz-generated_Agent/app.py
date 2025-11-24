import streamlit as st
import os
import sys

# Add the project root to the sys.path to allow absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__)))) # Point to the current directory initially, then it will handle 'agent' and 'utils'

from agent.summarizer import summarize_pdf
from agent.quiz_generator import generate_quiz


st.set_page_config(page_title="PDF Summarizer & Quiz Generator", layout="wide")

st.title("📚 PDF Summarizer & Quiz Generator")
st.markdown("Upload a PDF to get a summary and a generated quiz based on its content.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Display buttons for actions
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Summarize PDF"):
            with st.spinner("Summarizing..."):
                summary = summarize_pdf(temp_file_path)
                st.subheader("Summary")
                st.markdown(summary)

    with col2:
        if st.button("Create Quiz"):
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(temp_file_path)
                st.subheader("Generated Quiz")
                st.markdown(quiz)

    # Clean up the temporary file after processing or if user uploads new file
    # (This simple cleanup might not be ideal for all scenarios, but works for basic demo)
    # os.remove(temp_file_path)
    # Consider adding a more robust cleanup or caching strategy for production
