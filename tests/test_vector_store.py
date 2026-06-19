from utils.document_loader import load_document
from utils.chunking import chunk_text
from utils.vector_store import add_documents, search_documents

# Load document
text = load_document("data/sample.txt")

# Split into chunks
chunks = chunk_text(text)

# Store in ChromaDB
add_documents(chunks)

print("Document stored successfully!\n")

# Ask a question
query = "What is Machine Learning?"

results = search_documents(query)

print("Search Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 50)