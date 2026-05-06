import json

# Converting JSON string to Python dictionary (loads)
json_data = '{"name": "Sheik", "age": 24,"is_dev": true}'
python_data = json.loads(json_data)

print(python_data)
print(type(python_data))

# Reading JSON data from a file (load)
with open('response.json', 'r') as file:
    data = json.load(file)

print(data)

# Converting Python dictionary to JSON string and writing to a file
python_dict={'username':'Sheik','age':24,'is_dev':True,'Hobbies':['Coding','Reading','Traveling']}
json_string=json.dumps(python_dict,indent=4)
with open("output.json","w") as file:
    file.write(json_string)
    file.close()