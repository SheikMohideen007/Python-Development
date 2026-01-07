import requests

# GET request to fetch user data
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, headers={"Accept": "application/json"})

print(response.status_code)
print(response.text)
response_json = response.json()
for user in response_json:
    print("User ID:", user['id'], "Name:", user['name'], "Email:", user['email'])


# POST request to create a new post
url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello API",
    "body": "Learning POST request",
    "userId": 2
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())

# Check if POST was successful
if response.status_code in (200, 201):
    print("POST success")
else:
    print("POST failed")
