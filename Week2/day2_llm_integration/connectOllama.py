import requests

url = "http://localhost:11434/api/generate"

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Chat ended")
        exit()

    data = {
        "model": "phi3:mini",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    if "response" in result:
        print("AI:", result["response"])
    else:
        print("Error:", result)
print(response.json()["response"])