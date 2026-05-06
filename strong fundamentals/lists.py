# Lists and their methods

sampleList = [1, 2, 3, 4, 5]
sampleList.append(6)
print(max(sampleList))
sampleList.insert(0, 0)
print(sampleList)
sampleList.remove(3)
print(sampleList)
sampleList.pop()
print(sampleList)
sampleList.reverse()
print(sampleList)
sampleList.sort()
print(sampleList)
sampleList.clear()
print(sampleList)
sampleList.extend([7, 8, 9])
print(sampleList)
sampleList2 = sampleList.copy()
print(sampleList2)
print(sampleList2.count(8))
print(sampleList2.index(7))
sampleList2[0] = 10
sampleList2[1:3] = [20, 30]
print(sampleList2)
print(sampleList2.__contains__(20))

# Dunder methods for lists
my_list = [1, 2, 3]
print(len(my_list))
print(my_list.__len__())
print(2 in my_list)
print(my_list.__contains__(2))
print(my_list[0])
print(my_list.__getitem__(0))
print(my_list + [4, 5])
print(my_list.__add__([4, 5]))