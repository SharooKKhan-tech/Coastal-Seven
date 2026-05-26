import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "phi3:mini",
    "prompt": "Explain recursion in programming",
    "stream": True
}

response = requests.post(url, json=data)

for line in response.iter_lines():

    if line:

        decoded_line = line.decode("utf-8")

        print(decoded_line)

        json_data = json.loads(decoded_line)

        if "response" in json_data:
            print(json_data["response"], end="", flush=True)