"""
Exercise 10. Create a program that calculates and shows the final salary of a worker depending on the
base salary and seniority according to the following rules:

a. Ask the user about the base salary. If the base salary is bigger or equal than 1000 just show it as
the final salary.
b. If the base salary is less than 1000, ask the user about the seniority (only ask about it in this
case!)
● If seniority is at least 10 years, the salary will be increased by 20%.
● If seniority is less than 10 years, the salary will be increased by 5%.
Example of output:
Final salary of the worker is:
XXX Euros

"""

salary = int(input("Enter the base salary: "))

if (salary < 1000):
    seniority = int(input("How many years have you been working in this company?: "))
    if (seniority >= 10):
        salary *= 1.2
    else:
        salary *= 1.05

print("Final salary: " + str(salary))
