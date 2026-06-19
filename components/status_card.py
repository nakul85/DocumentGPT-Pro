import streamlit as st


def render_status_card(
    title: str,
    value: str,
    status: str = "Ready"
):
    """
    Reusable status card component.
    """

    with st.container(border=True):

        st.markdown(f"### {title}")

        st.write(value)

        st.caption(status)