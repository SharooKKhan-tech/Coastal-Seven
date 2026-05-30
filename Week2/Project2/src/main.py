from extractor import extract_text
from chroma_store import chunk_text, store_chunks
from embedder import create_embedding
from rag_query import ask_question
import os

# Ask user for file path
file_path = input("Enter file path: ").strip()

# Check file exists
if not os.path.exists(file_path):
    print("❌ File not found.")
    exit()

print(f"\n📄 Processing file: {file_path}")

# Extract text
text = extract_text(file_path)

if not text.strip():
    print("⚠️ No text found in file.")
    exit()

# Chunk text
chunks = chunk_text(text)

# Store in ChromaDB
store_chunks(chunks, create_embedding)

print(f"✅ Stored {len(chunks)} chunks successfully.")

# Question-answer loop
while True:

    question = input("\nAsk a Question (or type exit): ")

    if question.lower() == "exit":
        print("👋 Exiting...")
        break

    answer = ask_question(question)

    print("\n🤖 AI Answer:\n")
    print(answer)