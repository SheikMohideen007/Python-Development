# Functions in Python

# Function to greet a user with their name
def funcWithParam(name: str) -> str:
    return f"\nHello {name}"

print(funcWithParam("Sheik"))

# Function to ask for user confirmation with retries and reminders
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# Function to demonstrate exception handling
def checkTheNumber(number: int):
    try:
        if number % 0 == 0:
            print("came on try")
    except Exception as e:
        print(f"cannot divide by zero {e}")
    finally:
        print("finally block executed")

checkTheNumber(10)

# Function to greet a list of names
def greet(name: list):
    return f"Hello {name}"

print(greet(['Sheik','Shemo','Mohideen']))

# Function to greet a user with their name and age
def greet(name, age):
    return f"{name} is {age}"

print(greet('Sheik',23))
print(greet(age=23,name='Sheik'))

# Function with a default parameter for name
def name(name='Shemo'):
    return f"Hello {name}"

print(name())
print(name("Mohideen"))

# Function to check and return a greeting for a name
def check(name: str):
    return f"Hello {name}"

print(check(1))
print(check("Sheik"))