"""



(a) Normal ticket: 9
Euros; (b) Children under 5: 60% discount; (c) People over 60: 55% discount; (d) Young people under 26: 20% discount.

"""

age = int(input("Enter the age: "))

if (age < 5):
    print(9 * 0.40)
elif (age > 60):
    print(9 * 0.45)
elif (age < 26):
    print(9 * 0.80)
else:
    print(9)

