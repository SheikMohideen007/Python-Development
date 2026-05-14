# Tuples and their methods

sampleTuple = (1, 2, 3, 4, 5)
print(sampleTuple + (6, 7, 8))
print(sampleTuple.__add__((6, 7, 8)))
print(sampleTuple[4])
print(sampleTuple.count(3))
print(sampleTuple.index(4))
print(len(sampleTuple))
print(3 in sampleTuple)
print(sampleTuple.__contains__(3))
print(sampleTuple * 2)
print(sampleTuple[1:3])

# Dunder => Double Underscore
# Dunder methods for tuples
my_tuple = (1, 2, 3)
print(len(my_tuple))
print(my_tuple.__len__())
print(2 in my_tuple)
print(my_tuple.__contains__(2))
print(my_tuple[0])
print(my_tuple.__getitem__(0))
print(my_tuple + (4, 5))
print(my_tuple.__add__((4, 5)))
print(hash(my_tuple))
print(my_tuple.__hash__())
