from io import BytesIO
from typing import List

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def _conversation_text(messages: List[dict]) -> str:
    """
    Convert conversation into plain text.
    """

    lines = []

    for message in messages:

        role = message["role"].capitalize()

        lines.append(
            f"{role}:\n{message['content']}\n"
        )

    return "\n".join(lines)


def export_txt(messages: List[dict]) -> bytes:
    """
    Export chat as TXT.
    """

    return _conversation_text(messages).encode("utf-8")


def export_markdown(messages: List[dict]) -> bytes:
    """
    Export chat as Markdown.
    """

    md = []

    md.append("# DocumentGPT Conversation\n")

    for message in messages:

        role = message["role"].capitalize()

        md.append(
            f"## {role}\n\n{message['content']}\n"
        )

    return "\n".join(md).encode("utf-8")


def export_pdf(messages: List[dict]) -> bytes:
    """
    Export chat as PDF.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>DocumentGPT Conversation</b>",
            styles["Heading1"]
        )
    )

    for message in messages:

        role = message["role"].capitalize()

        story.append(
            Paragraph(
                f"<b>{role}</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                message["content"],
                styles["BodyText"]
            )
        )

    document.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf