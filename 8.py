list1=[]
list_lenght=int(input("enter the lenght:"))
for i in range(list_lenght):
    item=input("enter the string:")
    list1.append(item)
print(list1)
max_len = 0
for ele in list1:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
print("largest string is:",res)
