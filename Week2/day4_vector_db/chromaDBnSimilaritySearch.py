import os
import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from docx import Document

def extract_text_from_file(file_path):

    text = ""
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file_path.endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    return text.strip()
def chunk_text(text, chunk_size=10):

    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

if __name__ == "__main__":

    file_path = input("Enter the file path: ")
    text = extract_text_from_file(file_path)
    chunks = chunk_text(text)
    print(chunks)
    print("Chunks Created")

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    print(embeddings.shape)
    print("Embeddings created")

    client = chromadb.Client()
    collection = client.create_collection("documents")
    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[str(i) for i in range(len(chunks))]
    )

    stored_data = collection.get()

    print("\nStored Data in ChromaDB:\n")

    print(stored_data)

    query = input("\nAsk a question: ")
    results = collection.query(
        query_texts=[query],
        n_results=2
    )
    print("\nMost Relevant Chunks:\n")

    for doc in results['documents'][0]:
        print(doc)
        print("\n-------------------\n")