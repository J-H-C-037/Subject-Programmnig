"""

Create a list of any type, with length greater than 20. Initialize all its elements to random values.
Create a second list and make it equal to the first one (with a = b). Change the value of an element
of the first list. Print both lists. Does the corresponding element of the second list change? Why?
Create two additional lists and repeat the previous steps, but instead of = copy the elements of
the first into the second one by one. Can you see any difference?

"""
import random

a = []

for i in range(21):
    a.append(random.randint(0, 10))

b = a

a[0] = 99

print(a[0], b[0])

print("Both elements changed because both list point to the same memory location")

c = []
d = []

for i in range(21):

    c.append(random.randint(0, 10))

    d.append(c[i])

c[0] = 99

print(c[0], d[0])

print(
    "They result is different, because is a copy of the elements in c and it is stored in a different memory position")
