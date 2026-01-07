name="Sheik"
age=24
is_dev=True

print(name,age,is_dev)


nums = [1, 2, 3]
nums.append(4)

print('\n...',len(nums))
user = {"name": "Shemo", "role": "Flutter Dev"}

print(nums[2])
user.update({'name':'Sheik'})
print(user.__contains__('role'))
print(user)

age=1

if age > 18:
    print("Adult")
elif age==1:
    print("Kutty kunjan")
else:
    print('Minor')    


for n in nums:
    print(n)

while age < 30:
    print(age)
    age += 1
