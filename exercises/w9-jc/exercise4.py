"""
Create a function to convert currencies in an exchange office. It will have a local constant
containing a nested tuple with the exchange rates for the desired currencies (euro, yen, dollar
and sterling pound). It will receive the original currency, the target currency and the quantity to
change and will return the quantity of money in the target currency.

"""


def convert_currency(original, target, quantity):
    conversion = ((1, 130, 1.16, 0, 86), (0.0076, 1, 0.0088, 0.0065), (0.86, 112, 1, 0.73), (1.16, 151, 1.34, 1))

    original = original.lower()
    target = target.lower()
    i = 100
    j = 100

    if original == "euro":
        i = 0
    elif original == "yen":
        i = 1
    elif original == "dollar":
        i = 2
    elif original == "sterling pound":
        i = 3

    if target == "euro":
        j = 0
    elif target == "yen":
        j = 1
    elif target == "dollar":
        j = 2
    elif target == "sterling pound":
        j = 3

    return quantity * conversion[i][j]

