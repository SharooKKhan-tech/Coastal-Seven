import requests

url = "http://localhost:11434/api/generate"

data = {
        "model": "phi3:mini",
        "prompt":"expalin the concept of recursion in programming",
        "stream": False
    }

response = requests.post(url, json=data)

result = response.json()

print(result)

print(result["response"])


