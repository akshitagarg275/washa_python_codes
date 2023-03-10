import json
from difflib import get_close_matches

data = []
json_file = open('products.json', encoding="utf8")
json_str = json_file.read()
json_data = json.loads(json_str)
for item in range (len(json_data)):
    # print (json_data[item]["name"])
    data.append(json_data[item]["name"])

print(data)
print(len(data))
    