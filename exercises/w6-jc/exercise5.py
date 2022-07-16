"""
Write a program that guesses the number that the user has thought (1 to 100). The program will
generate random numbers and must control that none of them is repeated. It will also be able to
detect if the user is lying (if it has already tried all the numbers and the user says it is none of
them). It has also to count how many attempts were needed to guess the number.

"""
import random

a = []

for i in range(1, 101):
    a.append(i)


correct = "False"

guess = 999
stop = False
attemps = 0

while correct != "True" and stop == False:

    if len(a) != 0:

        while guess not in a:
            guess = random.randint(0,100)

        print(guess)

        correct = input("Was this the number that you thought(True/False)? ")
        if correct == "True":
            print("You guessed the correct num")
        a.remove(guess)
        attemps += 1
    else:
        print("You lied")
        stop = "True"

print("Attemps: ", attemps)