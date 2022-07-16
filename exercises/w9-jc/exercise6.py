"""

Write a function that determines how many days there are in a particular month. The function
will receive two parameters: the month, as an integer between 1 and 12, and the year as a fourdigit integer. Consider the existence of leap years. Create a main program that reads a month
and a year from the keyboard and displays the number of days in that month on the screen.

"""


def days(month, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    months[1] = 29
            else:
                months[1] = 29

    return months[month-1]
