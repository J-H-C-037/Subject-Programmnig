"""

@author: Jiahao Chen
@since: 21/10/2021
@version: 1.0


Create a program to generate two matrixes (as lists of lists) of integers M1 and M2, which can
be of different size, by requesting the sizes and the values by keyboard. Then it should show the
elements of M1 that are included on M2.

Specify the number of rows of the M1 matrix and press Enter: 2

Specify the number of columns of the M1 matrix and press Enter: 3

Introduce the term in the 0, 0 position and press Enter: 1
Introduce the term in the 0, 1 position and press Enter: 3
Introduce the term in the 0, 2 position and press Enter: 5
Introduce the term in the 1, 0 position and press Enter: 7
Introduce the term in the 1, 1 position and press Enter: 9
Introduce the term in the 1, 2 position and press Enter: 11
The M1 matrix is:
1 3 5
7 9 11
Specify the number of rows of the M2 matrix and press Enter: 3
Specify the number of columns of the M2 matrix and press Enter: 2
Introduce the term in the 0, 0 position and press Enter: 1
Introduce the term in the 0, 1 position and press Enter: 2
Introduce the term in the 0, 2 position and press Enter: 3
Introduce the term in the 1, 0 position and press Enter: 4
Introduce the term in the 1, 1 position and press Enter: 5
Introduce the term in the 1, 2 position and press Enter: 6
The M2 matrix is:
1 2
3 4
5 6
The term 1 is included in both matrixes
The term 3 is included in both matrixes
The term 5 is included in both matrixes

"""

row1 = int(input("Specify the number of rows of the M1 matrix and press Enter: "))

column1 = int(input("Specify the number of columns of the M1 matrix and press Enter:"))

m1 = []

for i in range(row1):
    m1.append([])
    for j in range(column1):
        m1[i].append(int(input("Introduce the term in the {}, {} position and press Enter:".format(i, j))))

print("The M1 matrix is: ")
for i in range(row1):
    for j in range(column1):
        print(m1[i][j], end=" ")
        if j == column1 - 1:
            print()

row2 = int(input("Specify the number of rows of the M1 matrix and press Enter: "))

column2 = int(input("Specify the number of columns of the M1 matrix and press Enter:"))

m2 = []

for i in range(row2):
    m2.append([])
    for j in range(column2):
        m2[i].append(int(input("Introduce the term in the {}, {} position and press Enter:".format(i, j))))

print("The M2 matrix is: ")
for i in range(row2):
    for j in range(column2):
        print(m2[i][j], end=" ")
        if j == column2 - 1:
            print()

both = []

for i in range(row1):
    for j in range(column1):
        for z in range(row2):
            if m1[i][j] in m2[z] and m1[i][j] not in both:
                both.append(m1[i][j])
                print("The term {} is included in both matrixes".format(m1[i][j]))