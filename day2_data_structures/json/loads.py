import json
json_string = '{"name":"Sharook","age":21}'
parsed_data = json.loads(json_string)
print(parsed_data)