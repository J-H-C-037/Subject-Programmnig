"""Write a program that receives as input a positive number, which will correspond to a quantity of
money, and calculates and prints the minimum number of notes and coins for it, as in a previous
exercise. Use a tuple to store the different types of notes and coins that exist."""

"""
Create a program that receives as input a positive number, which will correspond to a
quantity of money, and calculates and prints the minimum number of notes and coins for it. If the quantity of
any coin or note is zero it must not be printed.

Notes: 500, 200, 100, 50, 20, 10 and 5€
● Coins: 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02 and 0.01€
Example, if 348.07 is introduced it should print:
200€: 1
100€: 1
20€: 2
5€: 1
2€: 1
1€: 1
0.05€: 1
0.02€: 1

"""
import math
money = float(input("Enter the quantity of money: "))

changes = ([200,0],[100,0],[50,0],[20,0],[10,0],[5,0],[2,0],[1,0],[.5,0],[.2,0],[.1,0],[0.05,0],[0.02,0],[0.01,0])

for i in range(len(changes)):
    while round(money,2) >= round(changes[i][0],2):
        money -= changes[i][0]
        changes[i][1] += 1
    print(changes[i], end = " ")
