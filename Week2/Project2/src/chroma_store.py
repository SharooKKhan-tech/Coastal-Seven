import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(persist_directory="./vector_store")
)

collection = client.get_or_create_collection(
    name="document_memory"
)

def chunk_text(text, chunk_size=500):
    words = text.split()

    return [
        " ".join(words[i:i+chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

def store_chunks(chunks, embed_function):
    for i, chunk in enumerate(chunks):

        embedding = embed_function(chunk)

        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk]
        )

def search(query_embedding):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )