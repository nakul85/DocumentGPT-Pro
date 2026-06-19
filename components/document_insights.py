import streamlit as st


def render_document_insights(insights: dict):
    """
    Display document insights in a clean dashboard.
    """

    if not insights:
        return

    st.subheader("📊 Document Insights")

    st.caption(
        "Quick statistics about the uploaded document."
    )

    # -----------------------------
    # First Row
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📄 Pages",
            insights["pages"]
        )

    with col2:

        st.metric(
            "🧩 Chunks",
            insights["chunks"]
        )

    # -----------------------------
    # Second Row
    # -----------------------------

    col3, col4 = st.columns(2)

    with col3:

        st.metric(
            "🔤 Words",
            f"{insights['words']:,}"
        )

    with col4:

        st.metric(
            "🔠 Characters",
            f"{insights['characters']:,}"
        )

    # -----------------------------
    # Reading Time
    # -----------------------------

    st.metric(
        "📖 Estimated Reading Time",
        f"{insights['reading_time']} min"
    )