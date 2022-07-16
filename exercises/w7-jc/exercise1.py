"""
@author: Jiahao Chen
@since: 21/10/2021
@version: 1.0

Create a NxN matrix (represented as list of lists) where the first N - 1 columns have random
numbers in the range 1 to 10 and the last column contains the result of adding the numbers in
previous columns. Show the matrix as follows:
10 + 9 + 3 = 22
4 + 8 + 7 = 19
1 + 9 + 7 = 17
2 + 8 + 8 = 18

"""

import random

matrix = []

n = int(input("Enter the dimension of the matrix: "))

sumlist = [0] * n
for i in range(n):
  matrix.append([])
  for j in range(n):
    if i == n-1:
      matrix[i].append(sumlist[j])
    else:
      matrix[i].append(random.randint(1,10))
      sumlist[j] += matrix[i][j]

for i in range(n):
  for j in range(n):
    if j == n - 1:
      print(matrix[j][i])
    elif j == n - 2:
      print(matrix[j][i], "=", end = " ")
    else:
      print(matrix[j][i], "+",end = " ")



