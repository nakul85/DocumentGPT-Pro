import math
from pathlib import Path

from pypdf import PdfReader
from docx import Document


def get_document_insights(file_path: str, text: str, chunk_count: int):
    """
    Generate document statistics.
    """

    extension = Path(file_path).suffix.lower()

    pages = "-"

    try:

        if extension == ".pdf":
            pages = len(PdfReader(file_path).pages)

        elif extension == ".docx":
            pages = len(Document(file_path).paragraphs)

    except Exception:
        pages = "-"

    words = len(text.split())

    characters = len(text)

    reading_time = max(
        1,
        math.ceil(words / 200)
    )

    return {
        "pages": pages,
        "words": words,
        "characters": characters,
        "chunks": chunk_count,
        "reading_time": reading_time
    }