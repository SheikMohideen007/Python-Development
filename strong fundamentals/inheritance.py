class A:
    def test(self):
        print("A")

class B:
    def test(self):
        print("B")

class C(A, B):
    pass

c = C()
print(C.__mro__)  # This will show the method resolution order for class C
c.test()  # This will print "A" because class A is listed before class B

class Dog:
    def speak(self):
        print("Woof!")
    
class Cat:
    def speak(self):
        print("Meow!")

class Animal(Dog, Cat):
    def speak(self):
        print("Some sound")
        super().speak()  # This will call the speak method of the next class in the MRO 

print(Animal.__mro__)  # This will show the method resolution order for class Animal   
animal = Animal()
animal.speak()  # This will print "Some sound" followed by "Woof!"



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

print(D.__mro__)  # This will show the method resolution order for class D
d = D()
d.show()
print(issubclass(D,A)) # This will return True because D is a subclass of A