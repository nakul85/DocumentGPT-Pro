from typing import List

from langchain_core.documents import Document

from config import TOP_K_RESULTS
from utils.cache import get_vector_store

vector_store = get_vector_store()


def clear_database():
    """
    Remove every stored document.
    """

    data = vector_store.get()

    ids = data.get("ids", [])

    if ids:
        vector_store.delete(ids=ids)


def add_documents(chunks: List[str]):
    """
    Store document chunks together with metadata.
    """

    clear_database()

    documents = []

    for index, chunk in enumerate(chunks):

        documents.append(

            Document(

                page_content=chunk,

                metadata={

                    "chunk_id": index + 1,

                    "source": "Uploaded Document"

                }

            )

        )

    vector_store.add_documents(documents)


def search_documents(
    query: str,
    k: int = TOP_K_RESULTS
):
    """
    Retrieve the most relevant chunks.
    """

    return vector_store.similarity_search(
        query=query,
        k=k
    )


def search_documents_with_scores(
    query: str,
    k: int = TOP_K_RESULTS
):
    """
    Retrieve chunks together with similarity scores.
    """

    return vector_store.similarity_search_with_score(
        query=query,
        k=k
    )


def get_document_count() -> int:
    """
    Number of indexed chunks.
    """

    data = vector_store.get()

    ids = data.get("ids", [])

    return len(ids)