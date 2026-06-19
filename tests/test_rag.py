from utils.document_loader import load_document
from utils.chunking import chunk_text
from utils.vector_store import add_documents, search_documents
from utils.llm import generate_answer

# Load document
text = load_document("data/sample.txt")

# Split document
chunks = chunk_text(text)

# Store chunks
add_documents(chunks)

# Ask question
question = "What is Retrieval-Augmented Generation?"

# Search
results = search_documents(question)

# Build context
context = "\n\n".join([doc.page_content for doc in results])

# Generate answer
answer = generate_answer(context, question)

print("\n===== QUESTION =====")
print(question)

print("\n===== CONTEXT =====")
print(context)

print("\n===== ANSWER =====")
print(answer)