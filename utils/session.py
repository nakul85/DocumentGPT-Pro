import streamlit as st


def initialize_session():
    """
    Initialize all Streamlit session state variables.
    """

    defaults = {
    "document_processed": False,
    "chunk_count": 0,
    "document_insights": {},
    "document_summary": "",
    "document_questions": [],
    "document_text": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_document_state():
    """
    Reset document-related state while keeping the chat.
    """

    st.session_state.document_processed = False
    st.session_state.chunk_count = 0
    st.session_state.document_summary = ""
    st.session_state.document_text = ""
    st.session_state.active_document = None


def clear_chat():
    """
    Clear only the conversation history.
    """

    st.session_state.messages = []