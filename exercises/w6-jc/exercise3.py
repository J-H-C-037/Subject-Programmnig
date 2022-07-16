"""

Write a program that:
a) Asks the user to enter the length of the float list to create. It must check that the number is
greater than 0, if not, it will continue asking for the length.
b) Fills it randomly with numbers between 1 and 49.
c) Creates a variable called total, it will store the addition of the integer part of all the elements
of the list.
d) Prints the list and the value of total.

"""
import random

length = int(input("Enter the length of the list: "))

a = []
total = 0

for i in range(length):
    a.append(random.randint(0, 49))
    total += a[i]

print(a, total)





