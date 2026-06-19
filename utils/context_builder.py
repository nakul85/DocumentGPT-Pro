def build_context(documents, max_chars: int = 1800) -> str:
    """
    Build an optimized context from retrieved documents.

    Limits the total context length before sending it
    to the LLM to improve response time.
    """

    context = []

    total_chars = 0

    for document in documents:

        text = document.page_content.strip()

        if not text:
            continue

        remaining = max_chars - total_chars

        if remaining <= 0:
            break

        if len(text) > remaining:
            text = text[:remaining]

        context.append(text)

        total_chars += len(text)

    return "\n\n".join(context)