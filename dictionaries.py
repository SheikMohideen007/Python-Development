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
print(user)

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