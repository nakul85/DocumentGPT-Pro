from typing import Dict, List

from utils.chunking import chunk_text
from utils.document_loader import load_document
from utils.document_ai import analyze_document
from utils.vector_store import add_documents


def process_document(file_path: str) -> Dict:
    """
    Process an uploaded document.

    Steps
    -----
    1. Load document
    2. Split into chunks
    3. Store chunks in ChromaDB
    4. Run AI analysis

    Returns
    -------
    dict
    """

    # Load document
    text = load_document(file_path)

    # Create chunks
    chunks: List[str] = chunk_text(text)

    # Store vectors
    add_documents(chunks)

    # AI Analysis
    ai = analyze_document(text)

    return {
        "text": text,
        "chunks": chunks,
        "summary": ai["summary"],
        "questions": ai["questions"]
    }