import streamlit as st


def create_layout():
    """
    Creates the main workspace layout.

    Returns
    -------
    left_panel
    right_panel
    """

    left_panel, right_panel = st.columns(
        [1, 2],
        gap="large"
    )

    return left_panel, right_panel