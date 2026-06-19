from utils.document_loader import load_document
from utils.chunking import chunk_text
text = load_document("data/sample.txt")

print("\n===== DOCUMENT =====\n")
print(text)

chunks = chunk_text(text)

print("\n===== CHUNKS =====")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)