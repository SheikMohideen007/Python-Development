# Control Flow in Python

# If, Else, and Elif
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")

# Nested If
z = 15
if x < y:
    if z > x:
        print("z is greater than x and x is less than y")

# Match-Case (Python 3.10+)
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))
print(http_status(404))
print(http_status(123))

# Logical Operators
# Using 'and', 'or', and 'not'

a = True
b = False

# 'and' operator
if a and b:
    print("Both a and b are True")
else:
    print("At least one of a or b is False")

# 'or' operator
if a or b:
    print("At least one of a or b is True")
else:
    print("Both a and b are False")

# 'not' operator
if not a:
    print("a is False")
else:
    print("a is True")

# Arithmetic Operators
# Examples of addition, subtraction, multiplication, division, and more

x = 15
y = 4

# Addition
print("x + y =", x + y)

# Subtraction
print("x - y =", x - y)

# Multiplication
print("x * y =", x * y)

# Division
print("x / y =", x / y)

# Floor Division
print("x // y =", x // y)

# Modulus
print("x % y =", x % y)

# Exponentiation
print("x ** y =", x ** y)