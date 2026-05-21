import requests

url = "http://localhost:11434/api/generate"

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    print("Sending request...")

    data = {
        "model": "gemma2:2b",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    print("Response received")

    result = response.json()

    print(result)

    if "response" in result:
        print("AI:", result["response"])
    else:
        print("Error:", result)