# class SampleClass:

#     def __init__(self,name:str,age:int):
#         if not isinstance(name, str): 
#             raise ValueError("Name must be a string")
#         if not isinstance(age, int):
#             raise ValueError("Age must be an integer")
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# obj=SampleClass("Sheik",25)
# obj.greet()

# Demonstrating the use of class variables and instance variables in Python
class Person:
    isHuman=True  # class variable shared by all instances of the class
    def __init__(self,name):
        self.name=name  # instance variable unique to each instance of the class

    def getPersonName(self):
        return self.name    

a=Person('Sheik')
b=Person('Mohideen')
print(a.getPersonName(),a.isHuman)
print(b.getPersonName(),b.isHuman)


# Demonstrating the use of class variables and instance variables in Python
class Laptops:
    listOfLaps=[] # class variable to store the list of laptops
    def __init__(self,laptop):
        self.listOfLaps.append(laptop) # instance variable to store the laptop name and also appending it to the class variable listOfLaps

    def getLaptops(self):
        print('here is a list of laptops',self.listOfLaps)

Laptops('Dell')
Laptops('HP')
Lap=Laptops('Lenovo')
Lap.getLaptops()