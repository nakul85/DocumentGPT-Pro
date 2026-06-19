import streamlit as st

from utils.helpers import (
    ensure_directories,
    load_css
)

from components.chat import initialize_chat


def initialize_application():
    """
    Initialize the entire application.
    """

    st.set_page_config(
        page_title="DocumentGPT Pro",
        page_icon="📄",
        layout="wide"
    )

    ensure_directories()

    load_css(
        "assets/style.css"
    )

    initialize_chat()