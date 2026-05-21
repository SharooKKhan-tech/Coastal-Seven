import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Python API",
    "body": "Learning requests library",
    "userId": 1
}

response = requests.post(url, json=new_post)

print(response.status_code)
print(response.json())