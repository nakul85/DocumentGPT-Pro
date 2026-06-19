import streamlit as st


def render_statistics(chunk_count):

    st.subheader("System")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Chunks",
            chunk_count
        )

    with c2:

        st.metric(
            "Status",
            "Ready"
        )

    st.metric(
        "Last Response",
        f"{st.session_state.response_time} sec"
    )