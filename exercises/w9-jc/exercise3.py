"""
Create a function that generates a random number between a minimum and a maximum. It will
have a third parameter to state if it must return an integer, float or complex number

"""

import random


def ram_num(min, max, type):
    ram = random.randint(min, max)

    if type == 0:
        return ram
    elif type == 1:
        return float(ram)
    else:
        return complex(ram)

