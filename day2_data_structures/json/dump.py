import json
data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "JavaScript", "C++"]
}
with open('data.json', 'w') as file:
    json.dump(data, file)