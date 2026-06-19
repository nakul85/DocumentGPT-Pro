import streamlit as st


def render_confidence_card():
    """
    Display answer confidence.
    """

    confidence = st.session_state.get(
        "confidence",
        0
    )

    label = st.session_state.get(
        "confidence_label",
        "No Match"
    )

    if confidence == 0:
        return

    st.subheader("🧠 Answer Confidence")

    st.progress(
        confidence / 100
    )

    if label == "High":
        icon = "🟢"

    elif label == "Medium":
        icon = "🟡"

    else:
        icon = "🔴"

    col1, col2 = st.columns(
        [1, 1]
    )

    with col1:

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

    with col2:

        st.metric(
            "Quality",
            f"{icon} {label}"
        )