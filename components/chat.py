import time
import streamlit as st


def initialize_chat():
    """
    Initialize chat-related session state.
    """

    defaults = {
        "messages": [],
        "response_time": 0.0,
        "retrieval_time": 0.0,
        "llm_time": 0.0,
        "retrieval_start": 0.0,
        "llm_start": 0.0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def add_message(role: str, content: str):
    """
    Add a message to conversation history.
    """

    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )


def clear_chat():
    """
    Clear chat history.
    """

    st.session_state.messages = []

    st.session_state.response_time = 0.0
    st.session_state.retrieval_time = 0.0
    st.session_state.llm_time = 0.0


def display_chat():
    """
    Display conversation.
    """

    st.subheader("💬 Conversation")

    container = st.container(
        border=True,
        height=540
    )

    with container:

        if not st.session_state.messages:

            st.markdown(
                """
## 🤖 Welcome to DocumentGPT Pro

Upload a document and ask questions in natural language.

### You can ask things like:

- Summarize this document.
- What are the key findings?
- Explain the second section.
- List important concepts.
- Generate interview questions.
- Compare two topics.

---
"""
            )

            return

        avatars = {
            "user": "🧑",
            "assistant": "🤖"
        }

        for message in st.session_state.messages:

            with st.chat_message(
                message["role"],
                avatar=avatars.get(message["role"])
            ):

                st.markdown(message["content"])


# --------------------------------------------------
# Retrieval Timer
# --------------------------------------------------

def start_retrieval_timer():

    st.session_state.retrieval_start = time.time()


def stop_retrieval_timer():

    st.session_state.retrieval_time = round(

        time.time()
        - st.session_state.retrieval_start,

        2
    )


# --------------------------------------------------
# LLM Timer
# --------------------------------------------------

def start_llm_timer():

    st.session_state.llm_start = time.time()


def stop_llm_timer():

    st.session_state.llm_time = round(

        time.time()
        - st.session_state.llm_start,

        2
    )

    st.session_state.response_time = round(

        st.session_state.retrieval_time
        + st.session_state.llm_time,

        2
    )