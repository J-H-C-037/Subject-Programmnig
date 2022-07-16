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
money = float(input("Enter the quantity of money: "))

for i in 200,100,20,5,2,1,0.05,0.02:
    times = 0
    while(money >= i):
        money -= i
        times += 1
        print(str(i), end=", ")

    if times > 0: print(i, times, end = ": ")


