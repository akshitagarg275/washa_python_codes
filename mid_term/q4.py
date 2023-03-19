import json
from difflib import get_close_matches

data = []
json_file = open('products.json', encoding="utf8")
json_str = json_file.read()
json_data = json.loads(json_str)
for item in range (len(json_data)):
    # print (json_data[item]["name"])
    data.append(json_data[item]["name"])

prod_dict = {}
suggestions = []

for product in data:
    # print(product)
    if product:
        product_split= product.split("-",1)
        product_key = product_split[0].strip()
        if (len(product_split) > 1):
            product_detail = product_split[1].strip()
    # print(product_key)
    

    # print(product_detail)
    # print(product_key)

    if product_key in prod_dict:
        val = prod_dict[product_key]
        val.append(product_detail)
        prod_dict[product_key] = val
        # print(prod_dict[product_key])
    else:
        prod_dict[product_key] = [product_detail,]
        # prod_dict[product_key].append(product_detail)

word = input("Enter a word: ")

for k in prod_dict.keys():
    if word.lower() in k.lower() and k.lower().find(word.lower()) == 0:
        suggestions.append(k) 
    else:
        print("There is no such key")

print("Does this match what you are looking for?")

for s in range(len(suggestions)):
    print(f"{s+1} {suggestions[s]}")

ch = int(input(("Plese enter the number beside the product lookup: ")))

choice = suggestions[ch-1]
print(f"did you mean {choice}?")

confirmation = input("Press y if yes, n if no: ")

if confirmation == 'y':
    items = prod_dict[choice]
    for item in items:
        print(item)
else:
    print("Ok Bye!")