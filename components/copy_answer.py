import streamlit as st


def render_copy_answer(answer: str):
    """
    Display a copy-friendly answer box.
    """

    if not answer:
        return

    with st.expander(
        "📋 Copy Answer",
        expanded=False
    ):

        st.caption(
            "Click inside the box and press Ctrl+C."
        )

        st.text_area(
            label="",
            value=answer,
            height=180,
            key="copy_answer_box"
        )