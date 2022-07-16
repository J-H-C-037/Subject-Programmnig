"""


Create a list of 100 integer numbers in the range 1 to 1000 and print it. Next remove from it all
the even numbers and print it again.

"""

import random

a = []

for i in range(100):
    a.append(random.randint(1,1000))

for i in range(1,1000,2):
    if i in a: a.remove(i)

print(a)