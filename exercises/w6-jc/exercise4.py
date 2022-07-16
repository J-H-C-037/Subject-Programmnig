"""
Write a program to create a 20 elements int list and filling it randomly with numbers in the range
1 to 9. Ask the user for a number between 1 and 9 (the program must check that the number is
in the desired range) and print if the number is in the list and all the positions where it appears.
"""

import random

a = []

for i in range(20):
    a.append(random.randint(0, 9))


num = 99

while not 0 < num < 10:
    num = int(input("Enter a number between 1 and 9: "))
    if num in a:
        print("Num in the list position", a.index(num) + 1)
    else:
        print("Num not in the list")
