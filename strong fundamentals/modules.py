def addition(a, b):
    print(f"Adding {a} and {b} gives {a + b}")


def subtraction(a, b):
    print(f"Subtracting {b} from {a} gives {a - b}")


def multiplication(a, b):
    print(f"Multiplying {a} and {b} gives {a * b}")

def division(a, b):
    if b != 0:
        print(f"Dividing {a} by {b} gives {a / b}")
    else:
        print("Cannot divide by zero")
