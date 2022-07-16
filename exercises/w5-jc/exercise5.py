"""


@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Define a program that allows simulating the behavior of an ATM. The program must meet the
following requirements
- Randomly create a 4-digits PIN number and the account balance, which must be in the range
50 to 5,000 Euros. Notice that the PIN must be stored as string, otherwise any leading zero it
may have will be lost.
- Request the corresponding PIN code to the user, giving up to three attempts to enter the
correct number. In case of failing three times the program will show a message on the screen
and finish.

- If the pin is correct it must show a menu with the different operations that the ATM allows, as
seen in the next example:
Welcome
------------------------
1- Deposit
2- Cash withdrawal
3- Exit
Choose the operation:
After each operation, indicate on the screen the available balance in the account. If the cash
withdrawal operation exceeds the amount available in the bank account, the operation will be
denied and the corresponding message will be displayed.
"""
import random

PIN = str(random.randint(1000, 10000))

balance = random.randint(50,5001)

print(PIN)
print(balance)

times = 0
while times < 3:
    if PIN == input("Enter your pin: "):
        print("""
        1- Deposit
        2- Cash withdrawal
        3- Exit
        """)

        operation = input("Choose the operation(1,2,3): ")
        if operation == "1":
            balance += int(input("Enter the amount of money you want to deposit: "))
        elif operation == "2":
            money = int(input("Enter the amount of money you want to withdraw: "))

            if balance > money:
                balance = balance - money
            else:
                print("Operation denied, no enough money")
        else:
            print("")

        print("Current balance: ", balance)

        times = 3