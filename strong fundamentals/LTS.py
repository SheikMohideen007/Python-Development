#List

list=[1,2,4,2,5,"Sheik","Hello",True,6.2]
list.append("3")
list.remove(4)
list.insert(2,"Mohideen")
list.pop()
print("List Elements:",list)
print("Count of 2:",list.count(2)  )
print("Index of Sheik:",list.index("Sheik"))
print("value of 2 index is",list[2])
list2=list+["Welcome","to","Python"]
print("New List Elements:",list2)

# TUPLE

tuple=(1,2,4,2,5,"Sheik","Hello",True,6.2)
print("Tuple Elements:",tuple)
tuple2=tuple+(7,8,9)
print("New Tuple Elements:",tuple2)
print(tuple2[1])
# tuple2[1]="Shemo"
# tuple2.remove(2)  
print(tuple2)


# SET
ids = {1, 2, 3, 3, 4,4}
print(ids)

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

#List to Set Conversion
lis=[1,3,4,2,5,3,2,1]
unique_set = set(lis)
print("Unique elements from list:", unique_set)