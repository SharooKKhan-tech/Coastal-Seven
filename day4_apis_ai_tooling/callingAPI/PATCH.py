import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "title": "Partially Updated"
}

response = requests.patch(url, json=data)

print(response.json())