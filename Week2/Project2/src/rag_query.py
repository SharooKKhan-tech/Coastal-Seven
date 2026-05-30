from embedder import create_embedding
from chroma_store import search
from ollama_client import ask_llm

def ask_question(question):

    query_embedding = create_embedding(question)

    results = search(query_embedding)

    documents = results["documents"][0]

    if not documents:
        return "No relevant information found."

    context = " ".join(documents)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

    answer = ask_llm(prompt)

    return answer