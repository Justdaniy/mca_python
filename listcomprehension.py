list=[-1,2,-3,4,-5,6]
positive_num=[num for num in list if num>0]
print("positive numbers are:",positive_num)

n=4
square=[i**2 for i in range(1,n+1)]
print("squares of numbers upto n are:",square)

word="helo world"
vowels=[char for char in word if char.lower() in 'aeiouAEIOU']
print("vowels int the word are:",vowels)
