"""
@author
@since: 21/10/2021
@versin: 1.0

A wood workshop sells wood boards of 10 different sizes, which they call size 0, size 1, etc.
Create a program that:
a. Generates 10 random numbers, between 0 and 10. Each one will represent the stock for
each available board size. It must print the number of boards of each size in the warehouse.
b. Asks the user about the number of customers that will buy boards. It will keep asking while it
is smaller than 1.
c. Automatically generates an order for each of the customers. Each order will contain for each
available size a random number of boards between 0 and 4.
d. Prints the orders into the screen.
e. Sells boards to the customers, starting by the first one, reducing the number of boards in the
stock.
f. Prints the pending orders for each customer (only if he/she has pending orders). A pending
order is the number of boards of each size that cannot be sold as there are not enough
boards in stock.
Example:
Stock: size0 size1 size2 size3 size4 size5 size6 size7 size8 size9
1 6 4 5 5 8 1 8 7 2
Enter the number of customers, please
3
Original orders
Customer 0: 3 3 1 0 3 0 2 3 3 3
Customer 1: 0 3 3 1 1 0 0 1 3 0
Customer 2: 2 3 0 1 0 2 0 0 0 3
Pending orders
Customer 0: 2 0 0 0 0 0 1 0 0 1
Customer 2: 2 3 0 0 0 0 0 0 0 3
"""

import random

stock = []
print("Stock: size0 size1 size2 size3 size4 size5 size6 size7 size8 size9")
print("       ", end="")
for i in range(10):
    stock.append(random.randint(0, 10))
    print(stock[i], end="     ")

print()

customers = 0

while customers < 1:
    customers = int(input("Enter the number of customers, please: "))

orders = []

print("Original orders: ")

for i in range(customers):
    orders.append([])
    print("Customer {}:".format(i), end=" ")
    for j in range(10):
        orders[i].append(random.randint(0, 4))
        print(orders[i][j], end=" ")
        if stock[j] >= orders[i][j]:
            stock[j] -= orders[i][j]
            orders[i][j] = 0
        else:
            orders[i][j] -= stock[j]
            stock[j] = 0
    print()

print("Pending orders")

for i in range(customers):
    pending = False
    for j in range(10):
        if orders[i][j] != 0:
            pending = True
    if pending == True:
        print("Customer {}:".format(i), end=" ")
        for j in range(10):
            print(orders[i][j], end=" ")

