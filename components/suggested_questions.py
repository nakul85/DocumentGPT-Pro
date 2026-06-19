import streamlit as st


def render_suggested_questions(questions):
    """
    Render AI-generated suggested questions.

    Returns
    -------
    str | None
        Selected question.
    """

    if not questions:
        return None

    st.subheader("💡 Suggested Questions")

    st.caption(
        "Click any question to instantly ask DocumentGPT."
    )

    st.write("")

    selected_question = None

    for index, question in enumerate(questions):

        with st.container(border=True):

            if st.button(
                f"💬 {question}",
                key=f"suggested_question_{index}",
                use_container_width=True,
            ):
                selected_question = question

    return selected_question