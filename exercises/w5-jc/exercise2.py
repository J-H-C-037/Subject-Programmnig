"""

@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Ask the user two integer numbers A and B such as A + 5 < B. Keep asking until the former
condition is met. Then randomly generate and print 5 integer numbers in the interval [A,B] such
as they are even and odd in an alternative way. It does not matter if the values are repeated;
the aim is alternatively printing odd and even numbers.
Example: for the interval [3,9] a valid sequence of numbers is: 6, 7, 6, 3, 4

"""
a = 10
b = 0

while not (b > a + 5):
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

a += 1 if a % 2 == 1 else a

for i in range(a, a + 5):
    print(i, end=" ")
