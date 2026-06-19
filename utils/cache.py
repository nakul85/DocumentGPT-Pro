import streamlit as st

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH
)


@st.cache_resource
def get_embedding_model():
    """
    Load the embedding model only once.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


@st.cache_resource
def get_vector_store():
    """
    Load ChromaDB only once.
    """

    embedding_model = get_embedding_model()

    return Chroma(
        collection_name="documents",
        embedding_function=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )