"""Write a program that creates a tuple with the names of the months of the year. Then, the program
will ask the user for a number. If the number is between 1 and the maximum length of the tuple,
it will show the corresponding month of the year. Otherwise, it will show an error message and
will ask for another number. The program will run until the user enters a 0.
"""


months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

month_num = 99


while month_num != 0:
    month_num = int(input("Enter a number between 1-12: "))

    if 13 > month_num > 0:
        print(months[month_num-1])
    else:
        print("Error")

