list1 = []
n= int(input("enter the limit of list1:"))
print("enter the elements")
for i in range(0, n):
     element = int(input())
     list1.append(element)
print(list1)
list2 = []
m= int(input("enter the limit of list2:"))
print("enter the colors")
for i in range(0, m):
     element = int(input())
     list2.append(element)
print(list2)
if len(list1)==len(list2):
    print("same lenght")
else:
    print("different lenght")
if sum(list1)==sum(list2):
    print("sum is same")
else:
    print("different sum")
