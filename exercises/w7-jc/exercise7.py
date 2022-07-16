"""

@author: Jiahao Chen
@since: 21/10/2021
@version: 1.0


Create a list called students with the dictionaries of Exercise 1. For each element in the list:
a. Calculate the average of the weekly exercises and weekly tests, their maximum and their
minimum and add them as a 3-elements list at the last position of each list.
b. Add to each dictionary a new key called mark which contains the mark of the student
calculated as follows: WeeklyExercises are 10%, weeklyTests are 30%, and exam is
60%.
c. Add a new key called letterGrade whose value is:
 ’A’, if the score is 9 or above;
 ’B’ if the score is 8 or above;
 ’C’, if the score is 7 or above;
 ’D’, if the score is 6 or above.
 ‘E’ if the score is 5 or above.
 ‘F’ in any other case.
d. Print each element in students, one key per line.
e. Calculate and print the average mark of the class (average mark of the students)

"""


import random

maria = {"name": "Maria","weeklyExercises": [], "weeklyTests": [], "exam": []}
peter = {"name": "Peter","weeklyExercises": [],"weeklyTests": [], "exam": []}
mike = {"name": "Mike","weeklyExercises": [],"weeklyTests": [], "exam": []}


for j in [maria["weeklyExercises"],maria["weeklyTests"],maria["exam"],peter["weeklyExercises"],peter["weeklyTests"],peter["exam"],mike["weeklyExercises"],mike["weeklyTests"],mike["exam"]]:
    sum = 0
    for i in range(10):
        j.append(random.randint(0,10))
        sum += j[i]
        if i == 9:
            j.append([sum/10,max(j),min(j)])


maria["mark"] = maria["weeklyExercises"][-1][0] * 0.10 + maria["weeklyTests"][-1][0] * 0.30 + maria["exam"][-1][0] * 0.60
peter["mark"] = peter["weeklyExercises"][-1][0] * 0.10 + peter["weeklyTests"][-1][0] * 0.30 + peter["exam"][-1][0] * 0.60
mike["mark"] = mike["weeklyExercises"][-1][0] * 0.10 + mike["weeklyTests"][-1][0] * 0.30 + mike["exam"][-1][0] * 0.60

for student in maria, peter, mike:
    if student["mark"] >= 9:
        student["letterGrade"] = "A"
    elif student["mark"] >= 8:
        student["letterGrade"] = "B"
    elif student["mark"] >= 7:
        student["letterGrade"] = "C"
    elif student["mark"] >= 6:
        student["letterGrade"] = "D"
    elif student["mark"] >= 5:
        student["letterGrade"] = "E"
    else:
        student["letterGrade"] = "F"

for key, value in maria.items():
    print(key, value)

for key, value in peter.items():
    print(key, value)

for key, value in mike.items():
    print(key, value)

print("Average", (maria["mark"]+peter["mark"]+mike["mark"])/3)