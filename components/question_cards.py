import streamlit as st


def render_questions(questions):
    """
    Display AI generated suggested questions.
    """

    st.subheader("💡 Suggested Questions")

    if not questions:
        st.info("Questions will appear after processing a document.")
        return

    for question in questions:
        st.button(
            question,
            use_container_width=True,
            disabled=True
        )