"""

City:
    streets

Streets:
    - horizontal/vertical
    - starting coordinate (x,y)
    - length
    - temperature


Snowplows
    - coordinate (x,y)
    - amount of fuel

Snowflakes
    - coordinate (x,y)
    - if street.temperature < 2: they will melt
"""

import random


class Snowflake:
    def __init__(self, x, y, temperature):
        self.x = x
        self.y = y
        self.__temperature = temperature

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("It must be a interger")
        elif x < 0:
            raise ValueError("It must be equal of greater than 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("It must be an interger")
        elif y < 0:
            raise ValueError("It must be equal or greater than 0")
        else:
            self.__y = y

    @property
    def melted(self):
        if self.__temperature < 2:
            return False
        else:
            return True


class Street:
    def __init__(self, horizontal_or_vertical, starting_x, starting_y, length, temperature):
        self.horizontal_or_vertical = horizontal_or_vertical
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.length = length
        self.temperature = temperature
        self.snowflakes = []

    def __str__(self):
        if self.horizontal_or_vertical == "horizontal":
            return ("\"Street H-" + str(self.starting_y) + ", goes from (" + str(self.starting_x) + ", " + str(
                self.starting_y) + ") to (" + str(self.starting_x + self.length) + ", " + str(self.starting_y) + "). Temperature: " + str(self.temperature) + "\"\n")
        elif self.horizontal_or_vertical == "vertical":
            return ("\"Street V-" + str(self.starting_x) + ", goes from (" + str(self.starting_x) + ", " + str(
                self.starting_y) + ") to (" + str(self.starting_x) + ", " + str(self.starting_y + self.length) + "). Temperature: " + str(self.temperature) + "\"\n")

    def needs_cleaning(self):  # belongs to the class Street
        amount_snow = 0
        for snow in self.snowflakes:
            if not snow.melted:
                amount_snow += 1
        if amount_snow >= 2:
            return True
        else:
            return False


class Snowplow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fuel = random.randint(1, 20)


class City:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.street = None
        self.snowplow = None

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("It must be a interger")
        elif height <= 5:
            raise ValueError("It must be bigger than 5")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("It must be a interger")
        elif width <= 5:
            raise ValueError("It must be bigger than 5")
        else:
            self.__width = width

    def create_streets(self):  # it belongs to the class City
        self.street = tuple()
        for i in range(self.height):
            self.street += (Street("horizontal", 0, i, random.randint(5, self.width), random.randint(-5, 4)),)

        for j in range(self.width):
            self.street += (Street("vertical", j, 0, random.randint(5, self.height), random.randint(-5, 4)),)

    def create_snowplows(self):  # belongs to the class City
        self.snowplow = tuple()
        for i in range(self.height):
            self.snowplow += (Snowplow(0, i),)
        for j in range(self.width):
            self.snowplow += (Snowplow(j, 0),)

    def snow(self, number: int):  # belongs to the class City

        for i in range(number):
            ram_street = self.street[random.randint(0, len(self.street) - 1)]
            if ram_street.horizontal_or_vertical == "horizontal":
                x = random.randint(0, ram_street.length)
                ram_street.snowflakes.append(Snowflake(x, ram_street.starting_y, ram_street.temperature))
            elif ram_street.horizontal_or_vertical == "vertical":
                y = random.randint(0, ram_street.length)
                ram_street.snowflakes.append(Snowflake(ram_street.starting_x, y, ram_street.temperature))

    def streets_to_clean(self):  # belong to class City
        str = ""
        for street in self.street:
            if street.needs_cleaning():
                str += (street.__str__())
        return str

    def clean_street(self):  # belnog to class City
        for snowplow in self.snowplow:
            for i in range(snowplow.fuel):
                if snowplow.y == 0:
                    for street in self.street:
                        if street.starting_x == snowplow.x and snowplow.y == street.starting_y:
                            l = len(street.snowflakes)
                            j = 0
                            while j < l:
                                if street.snowflakes[j].y == i:
                                    del (street.snowflakes[j])
                                    l -= 1
                                j += 1
                elif snowplow.x == 0:
                    for street in self.street:
                        if street.starting_y == snowplow.y:
                            l = len(street.snowflakes)
                            j = 0
                            while j < l:
                                if street.snowflakes[j].x == i:
                                    del (street.snowflakes[j])
                                    l -= 1
                                j += 1

                snowplow.fuel -= 1
