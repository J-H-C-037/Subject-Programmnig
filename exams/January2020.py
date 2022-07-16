"""
Warehouse

- name
- drones
- neighborhood
- orders

Drone

- id
- current power (0 to 100)
- status (available or busy)
- order = 0 (initially)

Order

- priority
- id
- address

Map
- name (neighborhood)
- matrix of string of id/s (if more than 1 house in a position) of house

a drone for each order of a warehouse
"""

import random

class Drone:
    def __init__(self,id):
        self.id = id
        self.available = True
        self.power = random.randint(0,100)

class Warehouse:
    def __init__(self, name, neighborhood):
        self.name = name
        self.neighborhood = Map(neighborhood)
        self.drones = []
        self.orders = []

    def createDrones(self, Num: int):
        aux = []
        for i in range(Num):
            aux.append(Drone(i))

        self.drones = aux

    def insertOrderInList(self, order):
        for i in len(self.orders):
            if self.orders[i].priority < order.priority:
                self.orders.insert(i, order)

    def pickDrone(self, orderAddr):
        the_drone = None
        highest_power_drone = self.drones[0]
        d = self.neighborhood.computeDistance(self.name,orderAddr)
        pos = None

        for i in len(self.drones):
            if self.drones[i].power >= 2 * d and self.drones[i].available and pos == None:
                the_drone = self.drones[i]
                pos = i
            if self.drones[i].power > highest_power_drone.power:
                highest_power_drone = self.drones[i]
                pos = i

        if the_drone == None:
            highest_power_drone.power = 100
            the_drone = highest_power_drone

        return [pos, d]

    def processOrder(self, ord):
        for order in self.orders:
            info = self.pickDrone(order.address)
            self.drones[info[0]].available = False


class Order:
    def __init__(self, priority, id, address):
        self.priority = priority
        self.id = id
        self.address = address


class Map:
    def __init__(self,name):
        self.name = name
        self.map = None

    def createAreaMap(self, WhId, rows, cols, NumH):
        aux = []
        house = 0
        options = ["s", "h", WhId]
        while house < NumH:
            for i in range(rows):
                aux.append([])
                for j in range(cols):
                    ram = options[random.randint(0, 2)]
                    if ram == 1:
                        aux[i][j].append( ram + str(house))
                        house += 1
                    elif ram == 2 and WhId in options:
                        aux[i][j].append(ram)
                        del (options[2])
                    else:
                        aux[i].append(ram)

        self.map = aux

    def computeDistance(self, whId, houseId):
        whpos = []
        housepos = []
        for row in range(len(map)):
            for column in range(len(map[0])):
                if map[row][column] == houseId:
                    housepos.append(row)
                    housepos.append(column)
                elif map[row][column] == whId:
                    whpos.append(row)
                    whpos.append(column)
        return (((housepos[0]-whpos[0])**2 + (housepos[1]-whpos[1])**2)**0.5)

