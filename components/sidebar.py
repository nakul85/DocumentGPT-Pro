import streamlit as st

from config import (
    APP_NAME,
    LLM_MODEL,
    EMBEDDING_MODEL
)

from utils.vector_store import (
    clear_database,
    get_document_count
)

from utils.export_chat import (
    export_txt,
    export_markdown,
    export_pdf
)




def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        # ==================================================
        # Header
        # ==================================================

        st.title(APP_NAME)

        st.caption(
            "Your Private AI Knowledge Assistant"
        )

        st.divider()

        # ==================================================
        # AI Engine
        # ==================================================

        st.subheader("🤖 AI Engine")

        st.metric(
            "LLM",
            LLM_MODEL
        )

        st.metric(
            "Embeddings",
            EMBEDDING_MODEL.split("/")[-1]
        )

        st.divider()

        # ==================================================
        # Knowledge Base
        # ==================================================

        st.subheader("📚 Knowledge Base")

        chunk_count = get_document_count()

        st.metric(
            "Indexed Chunks",
            chunk_count
        )

        document_name = st.session_state.get(
            "document_name",
            ""
        )

        if document_name:

            st.caption(
                f"📄 {document_name}"
            )

        document_status = (
            "🟢 Ready"
            if st.session_state.get(
                "document_processed",
                False
            )
            else "🔴 No Document"
        )

        st.caption(
            f"Status: {document_status}"
        )

        st.divider()


        # ==================================================
        # Conversation
        # ==================================================

        st.subheader("💬 Conversation")

        messages = st.session_state.get(
            "messages",
            []
        )

        st.metric(
            "Messages",
            len(messages)
        )

        retrieval_time = st.session_state.get(
            "retrieval_time",
            0.0
        )

        llm_time = st.session_state.get(
            "llm_time",
            0.0
        )

        total_time = st.session_state.get(
            "response_time",
            0.0
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "⚡ Retrieval",
                f"{retrieval_time:.2f}s"
            )

        with col2:

            st.metric(
                "🧠 LLM",
                f"{llm_time:.2f}s"
            )

        st.metric(
            "⏱ Total Response",
            f"{total_time:.2f}s"
        )

        st.divider()

        # ==================================================
        # Export
        # ==================================================

        st.subheader("📤 Export Chat")

        st.download_button(
            "📄 TXT",
            data=export_txt(messages),
            file_name="conversation.txt",
            mime="text/plain",
            use_container_width=True,
            disabled=len(messages) == 0
        )

        st.download_button(
            "📝 Markdown",
            data=export_markdown(messages),
            file_name="conversation.md",
            mime="text/markdown",
            use_container_width=True,
            disabled=len(messages) == 0
        )

        st.download_button(
            "📕 PDF",
            data=export_pdf(messages),
            file_name="conversation.pdf",
            mime="application/pdf",
            use_container_width=True,
            disabled=len(messages) == 0
        )

        st.divider()

        # ==================================================
        # Actions
        # ==================================================

        st.subheader("⚙️ Actions")

        if st.button(
            "💬 Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []
            st.session_state.response_time = 0.0
            st.session_state.retrieval_time = 0.0
            st.session_state.llm_time = 0.0
            st.session_state.confidence = 0
            st.session_state.confidence_label = "No Match"

            st.success(
                "Conversation cleared."
            )

            st.rerun()

        if st.button(
            "🗑 Clear Knowledge Base",
            use_container_width=True
        ):

            clear_database()

            st.session_state.document_processed = False
            st.session_state.chunk_count = 0
            st.session_state.document_summary = ""
            st.session_state.document_text = ""
            st.session_state.document_name = ""
            st.session_state.document_questions = []
            st.session_state.document_insights = {}

            st.session_state.messages = []

            st.session_state.response_time = 0.0
            st.session_state.retrieval_time = 0.0
            st.session_state.llm_time = 0.0

            st.session_state.confidence = 0
            st.session_state.confidence_label = "No Match"

            st.success(
                "Knowledge base cleared."
            )

            st.rerun()

        st.divider()

        # ==================================================
        # System
        # ==================================================

        st.subheader("🖥️ System")

        st.success(
            "🟢 Ollama Connected"
        )

        st.caption(
            "Running Locally • Offline Mode"
        )

        st.divider()

        # ==================================================
        # About
        # ==================================================

        st.subheader("ℹ️ About")

        st.markdown(
            """
**DocumentGPT Pro**

Production-ready Retrieval-Augmented Generation (RAG) assistant.

### Tech Stack

- 🦙 Ollama
- 🔗 LangChain
- 🧠 Sentence Transformers
- 📚 ChromaDB
- ⚡ Streamlit

### Features

- AI Summary
- Semantic Search
- Suggested Questions
- Source References
- Context Relevance Scoring
- Streaming Responses
- Chat Export
- Offline Inference
"""
        )