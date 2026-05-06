try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter valid number")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution completed")

response = {"status": 200, "data": {"name": "Sheik"}}

try:
    print(response["data"]["age"])
except Exception as e:
    print("Key not found in response",e.__class__.__name__)

    