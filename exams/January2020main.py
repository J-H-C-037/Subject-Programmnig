from January2020 import Warehouse, Order
import random

num_dr = int(input("Enter the number of drones: "))

rows = int(input("Enter the number of rows: "))

columns = int(input("Enter the number of columns: "))

house = int(input("Enter the number of houses: "))

warehouse1 = Warehouse("wh1", "area1")

warehouse1.createDrones(num_dr)

warehouse1.neighborhood.createAreaMap(warehouse1.name, rows, columns, house)

for n in range(5):
    for i in range(rows):
        for j in range(columns):
            if warehouse1.neighborhood.map[i][j] != "s" and warehouse1.neighborhood.map[i][j] != warehouse1.name:
                warehouse1.insertOrderInList(Order(random.randint(0,10), n,i,j))

warehouse1.processOrder()
