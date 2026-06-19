import streamlit as st

from components.status_card import render_status_card


def format_file_size(size: int) -> str:
    """
    Convert bytes into a readable format.
    """

    units = ["B", "KB", "MB", "GB"]

    index = 0

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    return f"{size:.2f} {units[index]}"


def render_uploader():
    """
    Render the document upload section.
    """

    st.subheader("📚 Knowledge Base")

    st.caption(
        "Upload a document to build your private AI knowledge base."
    )

    st.info(
        "📄 **Supported formats:** PDF • DOCX • TXT"
    )

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed"
    )

    if uploaded_file is None:

        st.warning(
            "Upload a document to begin indexing and chatting."
        )

        return None

    st.success(
        f"✅ **{uploaded_file.name}** uploaded successfully."
    )

    # ----------------------------------------
    # Dynamic Status
    # ----------------------------------------

    if st.session_state.get("document_processed", False):

        render_status_card(
            title="Document Status",
            value="Processed",
            status="Ready for Questions"
        )

    else:

        render_status_card(
            title="Document Status",
            value="Ready to Process",
            status="Click 'Process Document'"
        )

    # ----------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📦 Size",
            format_file_size(uploaded_file.size)
        )

    with col2:

        st.metric(
            "📄 Type",
            uploaded_file.name.split(".")[-1].upper()
        )

    return uploaded_file