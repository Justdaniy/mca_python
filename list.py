
# creating an empty list
list = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
print("enter the elements")
for i in range(0, n):
    element = int(input())
    # adding the element
    list.append(element)  
 
print(list)
for i in range(len(list)) :
    if list[i]>100:
        list[i]="over"

print(list)
