"""Create the Student class, which represents a first year student. Its fields will be: name,
surname, programming mark, algebra mark, calculus mark, physics mark,
skills mark and humanities mark. Create an init method that receives values for all the
fields and checks that the values for the marks are in the right range (if not, a zero will be
assigned to the mark). Write a program that creates an object of this type, fills the fields asking
the user by keyboard and prints them."""


class Student:
    def __init__(self, name: str, surname: str, programming_mark: float, algebra_mark: float, calculus_mark: float,
                 physics_mark: float, skills_mark: float, humanities_mark: float):
        self.name = name
        self.surname = surname
        self.programming_mark = programming_mark
        self.calculus_mark = calculus_mark
        self.skills_mark = skills_mark
        self.humanities_mark = humanities_mark
        self.physics_mark = physics_mark
        self.algebra_mark = algebra_mark

        if self.programming_mark < 0 or self.programming_mark > 10:
            self.programming_mark = 0

        if self.physics_mark < 0 or self.physics_mark > 10:
            self.physics_mark = 0

        if self.algebra_mark < 0 or algebra_mark > 10:
            self.algebra_mark = 0

        if self.humanities_mark < 0 or humanities_mark > 10:
            self.humanities_mark = 0

        if self.calculus_mark < 0 or calculus_mark > 10:
            self.calculus_mark = 0

        if self.skills_mark < 0 or skills_mark > 10:
            self.skills_mark = 0


student = Student(input("Write the name of the student: "), input("Write the surname: "),
                     float(input("Mark in programming: ")),
                     float(input("Mark in Algebra ")),
                     float(input("Mark in Physics: ")),
                     float(input("Mark in Calculus: ")),
                     float(input("Mark in humanities: ")),
                     float(input("Mark in skills: ")))

print(student.name)
print(student.surname)
print("Programming: ", student.programming_mark)
print("Algebra: ", student.algebra_mark)
print("Physics: ", student.physics_mark)
print("Calculus: ", student.calculus_mark)
print("Humanities: ", student.humanities_mark)
print("Skills: ", student.skills_mark)
