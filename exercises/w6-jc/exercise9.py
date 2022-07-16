"""

A gymnast can receive a score between 1 and 10 from each judge; nothing lower, nothing higher.
All scores are integer values; there are no decimal scores from a single judge. There are 5 judges.
Write a program that stores the possible scores a gymnast can get in a list (randomly generated).

Print out the following sentences using the values of the list:

Judge i gave the gymnast n points (or Judge i gave the gymnast 1 point)

The lowest score is x, and the highest score is y
Note: the max() function, returns the largest number in a given list or tuple. That is, given the
tuple t = (1,2,3) max(t) returns 3. On the other hand, the min(), returns the smallest
number in a given list or tuple. That is, given the tuple t = (1,2,3) min(t) returns 1. It is
forbidden to use these functions in this program.

Example, assuming the list of scores is (8,6,8,4,1), the output of your program would be:
Judge 1 gave the gymnast 8 points
Judge 2 gave the gymnast 6 points
Judge 3 gave the gymnast 8 points
Judge 4 gave the gymnast 4 points
Judge 5 gave the gymnast 1 point
The lowest possible score is 1, and the highest possible score is 8

"""
import random

scores = ()

for i in range(5):
    scores+= (random.randint(1,10),)
    print("Judge", i +1, "gave the gymnast", scores[i], "points")


print("The lowest possible score is", min(scores), "and the highest possible score is", max(scores))