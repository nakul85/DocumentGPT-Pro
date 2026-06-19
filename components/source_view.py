import streamlit as st


def render_sources(documents):
    """
    Display retrieved source chunks in a professional format.
    """

    if not documents:
        return

    st.subheader("📚 Retrieved Sources")

    st.caption(
        "These document sections were retrieved from the knowledge base and used to generate the answer."
    )

    for index, doc in enumerate(documents, start=1):

        metadata = getattr(doc, "metadata", {})

        source = metadata.get(
            "source",
            "Uploaded Document"
        )

        chunk_id = metadata.get(
            "chunk_id",
            index
        )

        score = metadata.get(
            "score"
        )

        with st.container(border=True):

            st.markdown(
                f"### 📄 Source {index}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.caption(
                    f"**Document:** {source}"
                )

            with col2:

                st.caption(
                    f"**Chunk:** {chunk_id}"
                )

            if score is not None:

                confidence = max(
                    0,
                    min(
                        100,
                        round((1 - score) * 100)
                    )
                )

                st.progress(
                    confidence / 100
                )

                st.caption(
                    f"Match Confidence: **{confidence}%**"
                )

            st.markdown("---")

            st.markdown(
                doc.page_content
            )