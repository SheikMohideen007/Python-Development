class SampleClass:

    def __init__(self,name:str,age:int):
        if not isinstance(name, str): 
            raise ValueError("Name must be a string")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

obj=SampleClass("Sheik",25)
obj.greet()