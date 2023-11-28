import math
square=lambda a: a*a
circle=lambda r: math.pi*r*r
triangle=lambda b,h: 1/2*b*h
rectangle=lambda l,b: l*b
n=int(input("enter lenght of square:"))
print("area of square:",square(n))
m=int(input("enter the radius:"))
print("area of circle:",circle(m))
b=int(input("enter the breadth of triangle:"))
h=int(input("enter the height of triangle:"))
print("area of triangle:",triangle(b,h))
rl=int(input("enter the length of rectangle:"))
rb=int(input("enter the breadth of rectangle:"))
print("area of triangle:",rectangle(rl,rb))
