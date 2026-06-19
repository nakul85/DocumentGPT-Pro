import streamlit as st

from components.summary import render_summary
from components.suggested_questions import render_suggested_questions
from components.document_insights import render_document_insights
from components.statistics import render_statistics


def render_workspace():
    """
    Render the AI Workspace.
    """

    st.subheader("📄 AI Workspace")

    st.caption(
        "Everything generated from your uploaded document."
    )

    st.divider()

    # ==========================================
    # AI Summary
    # ==========================================

    render_summary(
        st.session_state.get(
            "document_summary",
            ""
        )
    )

    st.divider()

    # ==========================================
    # Insights + Questions
    # ==========================================

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    with left:

        render_document_insights(
            st.session_state.document_insights
        )

    with right:

        selected_question = render_suggested_questions(
            st.session_state.get(
                "document_questions",
                []
            )
        )

        if selected_question:

            st.session_state.selected_question = (
                selected_question
            )

            st.rerun()

    st.divider()

    # ==========================================
    # Statistics
    # ==========================================

    render_statistics(
        st.session_state.chunk_count
    )