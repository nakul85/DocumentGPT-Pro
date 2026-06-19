import streamlit as st


def begin_card(title: str):
    """
    Start a dashboard card.
    """

    st.markdown(
        f"""
        <div class="dashboard-card">
            <h4>{title}</h4>
        """,
        unsafe_allow_html=True
    )


def end_card():
    """
    Close dashboard card.
    """

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )