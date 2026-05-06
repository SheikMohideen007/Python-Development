# Loops in Python

# For loop
for i in range(0, 5, 2):
    print(i)

# While loop
num = 10
while num > 0:
    print(num)
    num -= 1

# Do-while loop (emulated in Python)
num = 10
while True:
    print(num)
    num -= 1
    if not (num > 0):
        break

for i in range(10):
    print("Iteration:",(i+1))

arr=[1,3,4,5]
for ele in arr:
    print("Array Element:",ele)

for i in range(len(arr)):
    print("Array Element:",arr[i])

count=0

while(count<10):
    print('Count is :',count)
    count +=1

for ch in "Sheik Mohideen":
    print("Character:",ch)

char=["Hello","welcome","How are you?","Fine"]

for word in char:
    for letter in word:
        print("Letter:",letter)
    print("\n")        