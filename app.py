import os
import streamlit as st
from components.copy_answer import render_copy_answer
from utils.confidence import calculate_confidence
from utils.context_builder import build_context
from components.layout import create_layout
from components.sidebar import render_sidebar
from components.uploader import render_uploader
from components.chat import (
    initialize_chat,
    display_chat,
    add_message,
    start_retrieval_timer,
    stop_retrieval_timer,
    start_llm_timer,
    stop_llm_timer
)
from components.source_view import render_sources
from components.workspace import render_workspace
from utils.document_processor import process_document
from utils.document_insights import get_document_insights
from utils.vector_store import (
    search_documents,
    search_documents_with_scores
)
from utils.llm import (
    stream_answer,
    build_history
)
from utils.helpers import (
    ensure_directories,
    load_css
)

# --------------------------------------------------
# App Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="DocumentGPT Pro",
    page_icon="📄",
    layout="wide"
)

ensure_directories()
load_css("assets/style.css")

initialize_chat()

# --------------------------------------------------
# Session State
# --------------------------------------------------

defaults = {
    "document_processed": False,
    "chunk_count": 0,
    "document_insights": {},
    "document_summary": "",
    "document_questions": [],
    "document_text": "",
    "document_name": "",
    "selected_question": None,
    "confidence": 0,
    "confidence_label": "No Match"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📄 DocumentGPT Pro")

st.caption(
    "Private AI-powered document assistant running locally using Ollama."
)

st.divider()

left_panel, right_panel = create_layout()

# ==================================================
# LEFT PANEL
# ==================================================

with left_panel:

    uploaded_file = render_uploader()

    if uploaded_file:

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        if not st.session_state.document_processed:

            if st.button(
                "🚀 Process Document",
                use_container_width=True
            ):

                with st.spinner("Processing document..."):

                    result = process_document(file_path)

                text = result["text"]
                chunks = result["chunks"]
                summary = result["summary"]
                questions = result["questions"]
                st.session_state.document_text = text
                st.session_state.document_summary = summary
                st.session_state.document_questions = questions
                st.session_state.chunk_count = len(chunks)

                st.session_state.document_insights = (
                    get_document_insights(
                        file_path=file_path,
                        text=text,
                        chunk_count=len(chunks)
                    )
                )

                st.session_state.document_processed = True

                st.success(
                    "✅ Document processed successfully!"
                )

                #st.rerun()

    if st.session_state.document_processed:

        render_workspace()

# ==================================================
# RIGHT PANEL
# ==================================================

with right_panel:

    display_chat()

    if st.session_state.document_processed:

        typed_question = st.chat_input(
            "Ask anything about your document..."
        )

        selected_question = st.session_state.get(
            "selected_question"
        )

        question = selected_question or typed_question

        if selected_question:
            st.session_state.selected_question = None

        if question:

            add_message(
                "user",
                question
            )

            with st.spinner("Searching knowledge base..."):

                start_retrieval_timer()

                results = search_documents_with_scores(
                    question
                )

                documents = []

                for doc, score in results:

                    doc.metadata["score"] = score

                    documents.append(doc)

                confidence, confidence_label = calculate_confidence(
                    results
                )

                st.session_state.confidence = confidence

                st.session_state.confidence_label = confidence_label

                context = build_context(
                    documents
                )

                stop_retrieval_timer()

            history = build_history(
                st.session_state.messages
            )

            with st.chat_message("assistant"):

                placeholder = st.empty()

                answer = ""

                start_llm_timer()

                for chunk in stream_answer(
                    context=context,
                    question=question,
                    history=history
                ):

                    answer += chunk

                    placeholder.markdown(
                        answer + "▌"
                    )

                placeholder.markdown(answer)

            stop_llm_timer()

            add_message(
                "assistant",
                answer
            )
            render_copy_answer(answer)
            render_sources(
                documents
            )

    else:

        st.info(
            "👈 Upload and process a document to start chatting."
        )

# --------------------------------------------------
# Sidebar (Render Last)
# --------------------------------------------------

render_sidebar()