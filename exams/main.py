"""

Create a program that allows the user to work with lists of float numbers. The program will
offer the user the following options:

1) Fill randomly a list where the user selects the number of elements and the upper and lower bound.

2) Fill randomly a list where the number of elements and the upper and lower bound are in the range
[1,1000).

3) Manually enter a list: the user will select the number of elements and he/she will enter their values.

4) Shrink the list: the program will create a new list with half the size of the original list and that will be
the result of adding the elements of the original list by pairs (the first element of the resulting list
will be the result of adding the first and second elements of the original list, the second element will
be the sum of the third and the fourth, and so on). Consider the case where the original list has an
odd number of elements.

5) Invert the list (without using the reverse method): once the list has been introduced, the program
will return a list where the elements are placed in reverse order (the first will be the last and so on)

6) Print a list: the program will print the list, truncating the numbers to their integer values.

"""

import random

def option1():
    num = int(input("Enter the number of elements\n"))
    upperbound = int(input("Enter the upper bound\n"))
    lowerbound = int(input("Enter the lower bound\n"))

    l1 = []
    print("The generated list is")
    for i in range(num):
        l1.append(random.randint(lowerbound, upperbound))
        print(l1[-1], end = " ")
    return l1

def option2():
    num = random.randint(1,1000)
    upperbound = random.randint(1,1000)
    lowerbound = random.randint(1,1000)

    print("The generated list is\n")

    l2 = []
    for i in range(num):
        l2.append(random.randint(lowerbound, upperbound))
        print(l2[-1], end = " ")
    return l2

def option3():
    num = int(input("Enter the number of elements\n"))
    l3 = []

    for i in range(num):
        l3.append(int(input("Enter a number")))

    print("The generated list is")
    for i in l3:
        print(i, end = " ")
    return l3

def shrink(list):
    new_l = []
    if len(list)%2 != 0:
        list.append(0)

    for i in range(0, len(list), 2):
        new_l.append(list[i] + list[i + 1])
        print(new_l[-1], end = " ")
    return new_l

def invert(list):
    new_l = []
    for i in range(1,len(list)+1):
        new_l.append(list[-i])
        print(new_l[-1], end = " ")
    return new_l

def exercise1():
    print("How do you want to fill the list?")
    print("1) Partially random")
    print("2) Totally random")
    print("3) Manually")
    choice = int(input("\n"))
    if choice == 1:
        my_l = option1()
    elif choice == 2:
        my_l = option2()
    elif choice == 3:
        my_l = option3()
    else:
        print("Please, enter 1,2 or 3!")

    choice2 = "P"

    while choice2 != "C":
        choice2 = input("\nEnter the option \nA)Shrink the list\nB)Invert the list\nC)Quit\n").upper()
        if choice2.upper() == "A":
            my_l = shrink(my_l)
        elif choice2.upper() == "B":
            my_l = invert(my_l)
        elif choice2 != "C":
            print("Enter a right option!")

    print("Thanks")




exercise1()