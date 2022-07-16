name1 = input("Enter a name: ")
age1 = int(input("Enter the age: "))

name2 = input("Enter another name: ")
age2 = int(input("Enter the age: "))

if (age1 < age2):
    print(name1 + " is younger than " + name2)
elif (age1 == age2):
    print(name1 + " has the same age has " + name2)
else:
    print(name1 + " is older than " + name2)

