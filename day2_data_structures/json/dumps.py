import json
data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "JavaScript", "C++"]
}

json_string = json.dumps(data)
print(json_string)  
