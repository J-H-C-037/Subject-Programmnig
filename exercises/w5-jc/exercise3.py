"""
@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Create a program to generate and print on screen the N perfect numbers smaller than the value
that the user introduces using the keyboard. A number is a perfect number when it is equal to
the addition of all its divisors except itself (You can rely on the flow diagram of the similar
exercise of a previous week). Example:
Introduce the top limit to generate perfect numbers and press Enter
10000
The number 6 is perfect
The number 28 is perfect
The number 496 is perfect
The number 8128 is perfect

"""


def perfect_num(number):
    sum_divisors = 0
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            sum_divisors += i

    return True if sum_divisors == number else False


limit = int(input("Enter the limit: "))

num = 6
sec = []

while num <= limit:
    if perfect_num(num):
        sec.append(num)
    num += 1

print(sec)
