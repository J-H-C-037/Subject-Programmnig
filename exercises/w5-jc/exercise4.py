"""

@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

As you know, when we ask the user to enter a number in Python using input, we need to cast
the number to int or float to be able to work with it. But if the user enters something which
is not a number the program fails. A possible solution is to use the isdigit() function of
strings, which returns True if the string is a number (for example '3434'.isdigit() returns
True). This works for integer numbers but not for float, as the point is not recognized as a
number ('34.22'.isdigit() returns False). Create a program that asks the user to
enter a number and keeps asking until a number is introduced. At the end it prints the square of
the entered number. It must work both for integer and float numbers.

"""
import math

is_num = False

while not is_num:
    is_num = True

    str1 = input("Enter an input: ")

    for char in str1:
        if not char in "1234567890.":
            is_num = False

print(math.sqrt(float(str1))) if is_num else print("Not a number")
