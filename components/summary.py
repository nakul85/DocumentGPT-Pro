import streamlit as st


def render_summary(summary: str):
    """
    Display the AI-generated document summary.
    """

    if not summary:
        return

    st.subheader("🧠 AI Document Summary")

    st.caption(
        "Automatically generated after document processing."
    )

    st.markdown(summary)

    st.divider()