import ollama
import streamlit as st

from config import LLM_MODEL


MAX_SUMMARY_CHARS = 6000


def generate_document_summary(document_text: str):

    document_text = document_text[:MAX_SUMMARY_CHARS]

    st.write("DEBUG MODEL:", LLM_MODEL)

    try:
        response = ollama.chat(
            model=LLM_MODEL,
            options={
                "temperature": 0.2,
                "num_predict": 220,
                "num_ctx": 2048
            },
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize:\n\n{document_text}"
                }
            ]
        )

        st.success("✅ Ollama summary succeeded")

        return response["message"]["content"]

    except Exception as e:

        st.error(f"❌ Ollama Error: {type(e).__name__}")

        st.exception(e)

        raise