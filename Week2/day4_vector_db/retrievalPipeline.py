import requests
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from docx import Document


def extract_text_from_file(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        reader = PdfReader(file_path)

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    elif file_path.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    return text.strip()


def chunk_text(text, chunk_size=80):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(chunk)

    return chunks

if __name__ == "__main__":


    file_path = input("Enter file path: ")
    text = extract_text_from_file(file_path)
    print("\nText Extracted Successfully")


    chunks = chunk_text(text)
    print("\nChunks Created:", len(chunks))
    for i, chunk in enumerate(chunks):

        print(f"\nChunk {i+1}:\n{chunk}")

        print("\n---------------------")


   
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("\nEmbedding Model Loaded")
    embeddings = model.encode(chunks)

    print("\nEmbeddings Created")

    print("Embedding Shape:", embeddings.shape)



    client = chromadb.Client()

    collection = client.get_or_create_collection("documents")

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[str(i) for i in range(len(chunks))]
    )

    print("\nData Stored in ChromaDB")

    stored_data = collection.get()

    print("\nStored Data:\n")

    for i in range(len(stored_data['ids'])):

        print(f"ID: {stored_data['ids'][i]}")

        print(f"Document:\n{stored_data['documents'][i]}")

        print("\n---------------------")


    while True:

        query = input("\nAsk a question (or type exit): ")

        if query.lower() == "exit":

            print("\nChat Ended")

            break

        query_embedding = model.encode([query]).tolist()

        results = collection.query(
            query_embeddings=query_embedding,
            n_results=2
        )

        retrieved_chunks = results['documents'][0]


        context = "\n".join(retrieved_chunks)


        prompt = f"""
You are an AI assistant.

Answer the question ONLY using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

        url = "http://localhost:11434/api/generate"

        data = {
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)

        result = response.json()


        print("\nAI Answer:\n")

        print(result["response"])

        print("\n============================")