"""

@author: Jiahao Chen
@since: 21/10/2021
@versin: 1.0


Fill a 3x3 matrix with random numbers considering that the values cannot be repeated:

Put in order the previous matrix as in the example shown below without using max(), min(),
neither sort()

"""

import random

m = [[], [], []]

t = []
for i in range(3):
    for j in range(3):
        num = (random.randint(1, 10))
        m[i].append(num)
        t.append(num)

ordered = []


def biggest(num, list):
    biggest = True
    for i in list:
        if i > num:
            biggest = False

    return biggest


k = 0
while len(t) != 0:
    if biggest(t[k], t) == True:
        ordered.append(t[k])
        del t[k]
        k = 0
    else:
        k += 1

counter = 0

for i in range(3):
    for j in range(3):
        m[i][j] = ordered[counter]
        counter += 1

print(m)