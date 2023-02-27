'''
dictionary -> {}
mutable -> it can change
Dictionary is represented as {key : value , .....}
keys can only be mutable datattypes -> number, tuple, strings
values can be of any datatypes -> another dictionary, list, string, int, float, boolean



'''

# stu = {}
# print(stu)
# print(type(stu))

stu = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 20,
    "courses" : ["Python", "Javascript"]
}


# stu_keys = stu.keys()
# print(stu_keys)

# stu_values = stu.values()
# print(stu_values)

# stu_items = stu.items()
# print(stu_items)

# print(stu)
# TODO: How to acccess the value using key
# print(stu["fname"])
# TODO: How to modify value in a key
# stu["age"] = 25
# print(stu["age"])
# print(stu)

# print(stu["gender"])

# Iterating(loop) the dictionary

stu = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 20,
    "courses" : ["Python", "Javascript"]
}

# for item in stu.items():
#     print(item)

# for k,v in stu.items():
#     print("Key is: ",k)
#     print("value is: ", v)

# for key in stu.keys():
#     print("key is : ",key)

# for val in stu.values():
#     print("value is :",val)

# TODO: clear
# print(stu)
# stu.clear()
# print(stu)

stu = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 20,
    "courses" : ["Python", "Javascript"]
}
# print(stu)
# stu_copy = stu.copy()
# print(stu_copy)

# print("fname" in stu)
# print("gender" in stu)

# TODO: get function
# print(stu.get("fname"))
# print(stu["gender"])
# print(stu.get("gender","NA"))

# print(stu)
# NOTE: In case of pop() we have to tell the key name
# print(stu.pop('age'))
# print(stu)

# NOTE: It removes last key: value pair from the dictionary
# print(stu)
# print(stu.popitem())
# print(stu)

# Initializing the values in a dictionary
# new_stu = {}.fromkeys(["name", "age", "country"], "NA")
# print(new_stu)

stu = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 20,
    "courses" : ["Python", "Javascript"]
}
# TODO: update
# stu["age"] = 21
# print(stu)  
# stu.update(age = 21)
# print(stu)

# stu.update({'age':24})
# print(stu)

# stu1 = dict(name = "Jane", age= 12)
# print(stu1) 
# print(type(stu1))

# new_stu = {}
# new_stu.update(stu)
# print("New student:",new_stu)

# myDict = {}
# myDict = myDict.update(dict.fromkeys(["one", "two"],10))
# print(myDict)

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", 
"power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", 
"notications", "achievements"]
initial_game_state = {}.fromkeys(game_properties,0)
print(initial_game_state)



#  Question 9
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list = inventory.copy()
# stock_list["cookie"] = 18
stock_list.update({"cookie" : 18})
stock_list.pop("cake")
# print(stock_list)

