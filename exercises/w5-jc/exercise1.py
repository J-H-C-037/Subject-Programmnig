"""

@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Create a program that generates a random number between 1 and 20, do not show this number
on the screen and keep it hidden. Then try to find out its value. As you enter values the program
must indicate if the number entered is greater or less than the one that the program has
generated and also the number of tries

"""

import random

num = random.randint(1, 21)
guess = 0
count = 0

while num != guess:
    guess = int(input("Enter your guess: "))
    count += 1
    if num > guess:
        print("Too small")
    elif num < guess:
        print("Too big")

print("You guessed the correct number! Tries: ", count)
