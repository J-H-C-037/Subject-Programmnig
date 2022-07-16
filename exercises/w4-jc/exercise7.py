"""
Create a program receiving by keyboard a number of seconds and converting it to its hours
equivalent (for example 3680 seconds are 1 hour, 1 minute and 20 seconds and will be printed like
01:01:20). Notice the leading zeros

"""

seconds = int(input("Enter a number of seconds: "))


hour = (seconds/3600) % 24
minutes = ((hour - int(hour)) * 60) % 60
seconds = ((hour - int(hour)) * 3600) % 60

if (hour < 10):
    print("0" + str(int(hour)) + ":", end = "")
else:
    print(int(hour) + ":", end = "")
if (minutes < 10):
    print("0" + str(int(minutes)) + ":", end = "")
else:
    print(int(minutes) + ":", end = "")
if (seconds < 10):
    print("0" + str(int(seconds)), end = "")
else:
    print(str(int(seconds)), end = "")
