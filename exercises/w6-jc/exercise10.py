"""

Exercise 10. To measure the time a program takes to execute we can use the time library and two variables.
In the first one we will store the time when our program starts executing (start =
time.time() in the first line of our program) and in the second one we will store the time
when it finishes (end = time.time() in the last line). Create a program that randomly fills
three different lists with 100,000 random values in the range 1 to 100:
a) For the first list use the append() method
b) For the second one use the += operator
c) For the third one use the + operator
Measure the time each one of these lists takes to fill. Is there any difference?

"""


import time
import random

start = time.time()

a = []

for i in range(100_000):
    a.append(random.randint(1,100))

print(time.time()-start)
a.clear()

start = time.time()

for i in range(100_000):
    a += [(random.randint(1,100))]

print(time.time() - start)
a.clear()

start = time.time()

for i in range(100_000):
    a = a + [(random.randint(1,100))]

print(time.time() - start)
