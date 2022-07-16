"""
Create a new type named RightTriangle to represent a right triangle, with fields base
and height. Create an init method that receives both fields as parameters and checks if they
are bigger than 0 (if not they will be set to 1). Write a program that uses the keyboard to read
the base and the height and store them in a RightTriangle object. Next it should ask
the user whether the area or the perimeter of the triangle has to be calculated and print the
resulting value.
"""


class RightTriangle:
    def __init__(self, base, height, info=None):
        self.base = base
        self.height = height

        if self.base <= 0:
            self.base = 1

        if self.height <= 0:
            self.height = 1

        self.info = int(input("Do you want to calculate the area (0) or the perimeter (1):"))

        if self.info == 0:  # area
            self.info = (self.base * self.height) / 2

        elif self.info == 1:  # perimeter
            l = (self.base * self.base + self.height * self.height) ** (1 / 2)
            self.info = self.base + self.height + l


triangle = RightTriangle(10,10)
print(triangle.info)
