def greet(name: list):
    return f"Hello {name}"

print(greet(['Sheik','Shemo','Mohideen']))

def greet(name, age):
    return f"{name} is {age}"

print(greet('Sheik',23))
print(greet(age=23,name='Sheik'))

def name(name='Shemo'):
    return f"Hello {name}"

print(name())
print(name("Mohideen"))