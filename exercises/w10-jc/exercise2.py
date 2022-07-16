"""Create three functions to: (a) ask the user for a positive number in the range (1, 10), (b)
generate a random list of this number of elements and (c) to find the minimum of the list.
Create a program that uses them."""

import random


def func():
    num = 0

    while 10 < num or num < 1:
        num = int(input("Write a number between 1 and 10: "))

    list = []

    for i in range(num):
        list.append(random.randint(1, 10))

    list.sort()

    return list[0]


print(func())
