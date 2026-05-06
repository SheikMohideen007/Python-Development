# from asyncio import run

# async def func1():
#     print('from async')
#     def insidefunc():
#         print('from inside func')
#     print('before calling inside func')
#     insidefunc()

# async def func2():
#     print('from async2')
#     def insidefunc():
#         print('from inside func')
#     print('before calling inside func')
#     insidefunc()

# async def func3():
#     await func1()
#     await func2()

# # run(func3())

# str='hello'
# print(str[::-1])
# # s=''
# # for i in range(len(str)):
# #     s+=str[i]
# #     print(s)
# ss="aabbbccccccd"

# def count_characters(s):
#     c={}
#     for i in ss:
#         c[i]=c.get(i,0)+1
#     return c

# print(count_characters(ss))

# lis=[1,2,3,4,4,4,5,5]

# def remove_duplicates_set(lis:list):
#     s=set()
#     for i in lis:
#         s.add(i)
#     return s

# def remove_duplicates(list:list):
#     new_list=[]
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# print(remove_duplicates(lis))

# lis2=remove_duplicates(lis)
# lis2.sort()

# print(lis2[-2])


# def missing_number(lst):
#     n = len(lst) + 1
#     total = n * (n + 1) // 2
#     print('total', total)
#     return total - sum(lst)

# print(missing_number([3,2,4,5]))

# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# print(is_anagram("listen", "silent"))


# zeros=[1,0,0,0,1,1]
# inc=0
# for i in zeros:
#     if(zeros[i]!=0):
#         c=zeros[inc]
#         zeros[inc]=zeros[i]
#         zeros[i]=c
#         inc+=1

    
# print(zeros)    


# def sayHello() -> None:
#     print("Hello")

# sayHello()

# a:int=10
# b:str="string"
# v:str='c'
# d:float=10.0
# e:bool=True
# print(type(a))
# print(type(b))
# print(type(v))
# print(type(d))
# print(type(e))

# for i in range(0,5,2):
#     print(i)

# for i in range(len(b)):
#     print(b[i],' ',i,end='')
# num=10
# while(num>0):
#     print(num)
#     num-=1

# Python doesn't have do-while, but we can emulate it:
# while True:
#     print(num)
#     num-=1
#     if not (num>0):
#         break

# def funcWithParam(name:str) -> str:
#     return f"\nHello {name}" 

# print(funcWithParam("Sheik"))

# default argument example:def ask_ok(prompt, retries=4, reminder='Please try again!'):
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# print(ask_ok("Do you want to continue? (yes/no): "))


# def checkTheNumber(number:int):
#     try:
#         if (number%0==0):
#            print("came on try")
#     except Exception as e:
#        print(f"cannot divide by zero {e}")
#     finally:
#         print("finally block executed")

# checkTheNumber(10)

# List & its methods

# sampleList:list=[1,2,3,4,5]
# sampleList.append(6)
# print(max(sampleList))
# sampleList.insert(0,0)
# print(sampleList)
# sampleList.remove(3)
# print(sampleList)
# sampleList.pop()
# print(sampleList)
# sampleList.reverse()
# print(sampleList)
# sampleList.sort()
# print(sampleList)
# sampleList.clear()
# print(sampleList)
# sampleList.extend([7,8,9])
# print(sampleList)
# sampleList2=sampleList.copy()
# print(sampleList2)
# print(sampleList2.count(8))
# print(sampleList2.index(7))
# sampleList2[0]=10
# sampleList2[1:3]=[20,30]
# print(sampleList2)
# print(sampleList2.__contains__(20))



# Dictionary & its methods
# sampledict:dict={"name":"Sheik","age":30,"city":"New York"}

# sampledict["age"]=25
# print(sampledict)
# sampledict["country"]="USA"
# print(sampledict)
# sampledict.pop("city")
# print(sampledict)
# sampledict.update({"age":28,"city":"Los Angeles"})
# print(sampledict)
# print(sampledict.keys())
# print(sampledict.values())
# print(sampledict.items())
# print(sampledict.get("name"))
# print(sampledict.get("nonexistent_key","Default Value"))
# print(sampledict.popitem())
# print(sampledict)
# sampledict2=dict.fromkeys(["name","age","city"],"Unknown")
# print(sampledict2)
# for key, value in sampledict.items():
#     print(f"{key}: {value}")
# for key in sampledict.keys():
#     print(f"Key: {key}")
# print(sampledict2.__contains__("nameoo"))
# print(sampledict2)


# Set & its methods

# sampleSet:set={1,2,3,4,5}
# sampleSet.add(6)
# print(max(sampleSet))
# sampleSet.remove(3)
# print(sampleSet)
# sampleSet.discard(5)
# print(sampleSet)
# sampleSet.pop()
# print(sampleSet)
# sampleSet.update((7,8,9))
# print(sampleSet)
# sampleSet2=sampleSet.copy()
# sampleSet2.add(10)
# print(sampleSet2)
# print(sampleSet2.__contains__(8))
# print('union of sampleSet and sampleSet2:', sampleSet.union(sampleSet2))
# print('intersection of sampleSet and sampleSet2:', sampleSet.intersection(sampleSet2))
# print('difference of sampleSet and sampleSet2:', sampleSet2.difference(sampleSet))
# print('is sampleSet2 a subset of sampleSet:', sampleSet2.issubset(sampleSet))
# print('is sampleSet2 a superset of sampleSet:', sampleSet2.issuperset(sampleSet))
# print('is sampleSet2 disjoint with sampleSet:', sampleSet.isdisjoint(sampleSet2))
# sampleSet.update(sampleSet2)
# print(sampleSet)
# sampleSet2.clear()
# sampleSet.clear()
# print(sampleSet)


# tuples and its methods

# sampleTuple:tuple=(1,2,3,4,5)
# print(sampleTuple+(6,7,8)) # here creating a new tuple by concatenating the existing tuple with another tuple. The original sampleTuple remains unchanged because tuples are immutable in Python.
# sampleTuple.__add__((6,7,8)) # this is another way to concatenate tuples using the __add__ method, which is the underlying method that gets called when you use the + operator. It achieves the same result as the previous line, creating a new tuple (1, 2, 3, 4, 5, 6, 7, 8) without modifying the original sampleTuple.
# print(sampleTuple[4])
# print(sampleTuple.count(3))
# print(sampleTuple.index(4))
# print(len(sampleTuple))
# print(3 in sampleTuple)
# print(sampleTuple.__contains__(3))
# print(sampleTuple * 2)
# print(sampleTuple[1:3])

# python dunder methods or Double UnderScore methods

# Demonstrating dunder methods on list
# my_list = [1, 2, 3]

# # These two are equivalent:
# print(len(my_list))          # 3 (Pythonic way)
# print(my_list.__len__())     # 3 (Dunder method directly)

# # These two are equivalent:
# print(2 in my_list)          # True
# print(my_list.__contains__(2)) # True

# # These two are equivalent:
# print(my_list[0])            # 1
# print(my_list.__getitem__(0)) # 1

# # These two are equivalent:
# print(my_list + [4, 5])      # [1, 2, 3, 4, 5]
# print(my_list.__add__([4, 5])) # [1, 2, 3, 4, 5]

# # Demonstrating dunder methods on tuple
# print("\n--- Tuple Dunder Methods ---")
# my_tuple = (1, 2, 3)

# # These two are equivalent:
# print(len(my_tuple))          # 3
# print(my_tuple.__len__())     # 3

# # These two are equivalent:
# print(2 in my_tuple)          # True
# print(my_tuple.__contains__(2)) # True

# # These two are equivalent:
# print(my_tuple[0])            # 1
# print(my_tuple.__getitem__(0)) # 1

# # These two are equivalent:
# print(my_tuple + (4, 5))      # (1, 2, 3, 4, 5)
# print(my_tuple.__add__((4, 5))) # (1, 2, 3, 4, 5)

# # Tuple is hashable (can be used as dict key)
# print(hash(my_tuple))         # Returns hash value
# print(my_tuple.__hash__())    # Same hash value

# # Demonstrating dunder methods on set
# print("\n--- Set Dunder Methods ---")
# my_set = {1, 2, 3}

# # These two are equivalent:
# print(len(my_set))            # 3
# print(my_set.__len__())       # 3

# # These two are equivalent:
# print(2 in my_set)            # True
# print(my_set.__contains__(2)) # True

# # Set operations using dunder methods
# other_set = {2, 3, 4}

# # These two are equivalent (intersection):
# print(my_set & other_set)     # {2, 3}
# print(my_set.__and__(other_set)) # {2, 3}

# # These two are equivalent (union):
# print(my_set | other_set)     # {1, 2, 3, 4}
# print(my_set.__or__(other_set)) # {1, 2, 3, 4}

# # These two are equivalent (difference):
# print(my_set - other_set)     # {1}
# print(my_set.__sub__(other_set)) # {1}

# # These two are equivalent (symmetric difference):
# print(my_set ^ other_set)     # {1, 4}
# print(my_set.__xor__(other_set)) # {1, 4}

# # Demonstrating dunder methods on dictionary
# print("\n--- Dictionary Dunder Methods ---")
# my_dict = {"a": 1, "b": 2, "c": 3}

# # These two are equivalent:
# print(len(my_dict))           # 3
# print(my_dict.__len__())      # 3

# # These two are equivalent:
# print("a" in my_dict)         # True
# print(my_dict.__contains__("a")) # True

# # These two are equivalent:
# print(my_dict["a"])           # 1
# print(my_dict.__getitem__("a")) # 1

# # Setting item using dunder method:
# my_dict["d"] = 4              # Pythonic way
# my_dict.__setitem__("e", 5)   # Dunder method
# print(my_dict)                # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# # Deleting item using dunder method:
# del my_dict["e"]              # Pythonic way
# my_dict.__delitem__("d")      # Dunder method
# print(my_dict)                # {'a': 1, 'b': 2, 'c': 3}



# class & objects

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

# obj=SampleClass("Sheik",30)
# obj.greet()            