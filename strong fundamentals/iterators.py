# lis=[1,2,4,4]
# it=iter(lis)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# Important Internal Mechanism

# A for loop internally does:

# it = iter(obj)

# while True:
#     try:
#         item = next(it)
#     except StopIteration:
#         break

class Reverse():
    def __init__(self,data):
        self.data=data
        self.len=len(data)

    def __iter__(self):
        return self    

    def next(self):
        if self.len==0:
            raise ValueError("No more items to iterate")
        finData=self.data[self.len-1]
        self.len-=1
        return finData

rev=Reverse("abcd")
print(rev.next())
print(rev.next())
print(rev.next())
print(rev.next())
print(rev.next())