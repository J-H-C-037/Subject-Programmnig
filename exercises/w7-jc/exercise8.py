"""


Create a dictionary with keys the names of the months of the year and values the number of
days of that month (‘January’: 31, etc). Create another dictionary with keys: day, month,
year and leapYear. Ask the user to fill the second dictionary. The value of leap year must be
automatically set. The value of the month and day must be correct taking into account leap
years (those years February has 29 days). If any value is not correct we will ask the user until a
correct value is entered. Print the date with format: March 23, 2019, non-leap year

"""

month = { "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}

dic = {"day":None, "month":None, "year":None, "leapYear":False}

dic["year"] = int(input("Enter the year: "))

if (dic["year"] %4 == 0):
    if(dic["year"] %100 == 0):
        if(dic["year"] %400 == 0):
            dic["leapYear"] = True
    else:
        leapYear = True

if dic["leapYear"]:
    month["feb"] = 29

monthvalid = False

while not monthvalid:
    dic["month"] = input("Enter the month(jan,feb,march,april,may,june,july,aug,sept,oct,nov,dec): ").lower()
    for i, j in month.items():
        if dic["month"] == i:
            monthvalid = True

dayvalid = False

while not dayvalid:
    dic["day"] = int(input("Enter the day: "))
    for i, j in month.items():
        if dic["day"] <= j:
            dayvalid = True

print(dic["month"],dic["day"],",",dic["year"], end = "")

if dic["leapYear"]:
    print(", leap year")
else:
    print(", non-leap year")