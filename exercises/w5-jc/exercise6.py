"""
Define a program which requests the mark of the exam for each student in a class and
calculates the highest mark, the lowest, the average and the number of students attending the
exam. The data input must finish when a negative number is introduced.

@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0
"""

marks = []

continue1 = True
while continue1:
    marks.append(int(input("Enter the mark of the student: ")))

    if marks[-1] < 0: continue1 = False

    marks.pop

marks.sort()

print(marks[0], marks[-1], end = " ")

sum1 = 0

for i in marks:
    sum1 += i

print(sum1/len(marks))