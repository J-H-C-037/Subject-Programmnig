"""

Create a Dice class with fields name and rolls, to simulate a dice game. The rolls field
must be a list. Create an init method that receives the name of the player and an integer n,
which represents the number of rolls. It must assign the name to the corresponding field and
create a list of n elements randomly filled with numbers from 1 to 6. Create a two-player game
asking each player his/her name. It must print the results for each one and calculate the winner,
which will be the one with the highest number of equal dice. In case of a tie, the one with the
highest total score will win.

"""

import random


class Dice:

    def __init__(self, name, n):  # n = number of rows
        self.name = name
        self.n = n
        self.rolls = self.throw_dice()

    def throw_dice(self):
        list1 = []
        for i in range(self.n):
            list1.append(random.randint(1, 6))
        return list1

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: int):
        if type(n) != int:
            raise TypeError("Not an interger")
        else:
            self.__n = n

    def score(self):
        count1 = 0
        max1 = 0

        for i in range(1, self.n):
            if self.rolls[i - 1] == self.rolls[i]:
                count1 += 1
                if count1 > max1:
                    max1 = count1
            else:
                count1 = 0
        return max1

    def sum(self):
        sum1 = 0
        for i in range(1, self.n):
            sum1 += self.rolls[i]
        return sum1


player1 = Dice("Raul", 2)
player2 = Dice("Miguel", 2)

if player1.score() > player2.score():
    print("Player 1 won")
elif player2.score() > player1.score():
    print("Player 2 won")
elif player1.sum() > player2.sum():
    print("Player 1 won")
else:
    print("Player 2 won")
