"""

Create a program with the following functions:
a. createListNumbers: Creates a list of 10 random elements all even numbers and returns
it.
b. calculateFigures: receives a list as parameter and calculates the maximum, minimum
and average values of the list. It returns the calculated values

"""
import random


def createListNumbers():
    l = []

    for i in range(10):
        ram = random.randint(0, 10)
        while ram % 2 != 0:
            ram = random.randint(0, 10)

        l.append(ram)

    return l


def calculateFigures(list):
    list.sort()

    sum = 0
    for i in list:
        sum += i

    return list[0], list[-1], sum / len(list)


print(createListNumbers())
print(calculateFigures(([1, 2, 3])))
