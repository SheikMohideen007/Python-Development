# Dictionaries and their methods

sampledict = {"name": "Sheik", "age": 30, "city": "New York"}
sampledict["age"] = 25
print(sampledict)
sampledict["country"] = "USA"
print(sampledict)
sampledict.pop("city")
print(sampledict)
sampledict.update({"age": 28, "city": "Los Angeles"})
print(sampledict)
print(sampledict.keys())
print(sampledict.values())
print(sampledict.items())
print(sampledict.get("name"))
print(sampledict.get("nonexistent_key", "Default Value"))
print(sampledict.popitem())
print(sampledict)
sampledict2 = dict.fromkeys(["name", "age", "city"], "Unknown")
print(sampledict2)
for key, value in sampledict.items():
    print(f"{key}: {value}")
for key in sampledict.keys():
    print(f"Key: {key}")
print(sampledict2.__contains__("name"))

# Dunder methods for dictionaries
my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))
print(my_dict.__len__())
print("a" in my_dict)
print(my_dict.__contains__("a"))
print(my_dict["a"])
print(my_dict.__getitem__("a"))
my_dict["d"] = 4
my_dict.__setitem__("e", 5)
print(my_dict)
del my_dict["e"]
my_dict.__delitem__("d")
print(my_dict)


user = {
    "name": "Sheik",
    "age": 24,
    "is_dev": True
}
user["age"] = 25
user["city"] = "Chennai"

print("Name:", user["name"])
print("Age:", user.get("age"))
print("Is Developer:", user.get("is_dev"))
# Iterate through keys
for key in user:
    print(f"{key}: {user[key]}")

# Iterate through values
for value in user.values():
    print(value)    

# Iterate through key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Nested Dictionary
response = {
    "status": 200,
    "data": {
        "user": {
            "id": 1,
            "name": "Sheik"
        }
    }
}
print("User ID:", response["data"]["user"]["id"])
print("User Name:", response["data"]["user"]["name"])