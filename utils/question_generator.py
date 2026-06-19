import streamlit as st
import ollama

from config import LLM_MODEL


def generate_suggested_questions(document_text):

    st.write("Generating questions...")

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": "Generate exactly 5 short questions about this document.\n\n"
                + document_text[:3000]
            }
        ]
    )

    st.success("Question generation succeeded")

    questions = [
        q.strip("-• ").strip()
        for q in response["message"]["content"].split("\n")
        if q.strip()
    ]

    return questions[:5]