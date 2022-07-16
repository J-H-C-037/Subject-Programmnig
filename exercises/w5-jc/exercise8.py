"""
@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Create a program that plays "Twenty 0ne”, a simple dice version of Blackjack. For this game two
dices will be rolled. The points will be calculated as the sum of the rolls of the two dices.
Although the game can be played with several players, to simplify it we will play only with two.
The rules are as follows:
● Each player plays only once per game.
● The player can roll the dice as many times as desired and can stop at any time if the
score is no higher than 21. Numbers obtained in each roll are added to the previous in
order to establish the score.
● If a player reaches a score greater than 21 she loses immediately, so the other player is
automatically the winner.
● If no player has exceeded 21, the participant whose total is nearest to 21 points, wins. If
the two players reach the same score, then it will be declared a tie.
● The number of games to be played will be a value defined as a constant in the program.
Taking into account the specifications established and the example provided:
▪ Program the move corresponding to player 1 until she decides to stop, or the score is
higher than 21, in this last case player 1 has lost.
▪ Program also the move corresponding to player 2 and display the winner (or the tie)
▪ Modify the exercise to run multiple games as indicated in the statement.
"""
import random

Num_of_games = 3


def roll_the_dice():
    dice = random.randint(1, 7)
    print("The number of points obtained is: ", dice)
    return dice


player1 = 0
player2 = 0
continue1 = True
continue2 = True

for i in range(Num_of_games):

    while continue1:
        print("Player1: ")
        player1 += roll_the_dice()
        player1 += roll_the_dice()
        if player1 > 21:
            print("Player 2 won")
            continue1 = False
        else:
            if input("Would you like to roll the dice again? (yes/no):") == "no":
                continue1 = False
                while continue2:
                    print("Player2: ")
                    player2 += roll_the_dice()
                    player2 += roll_the_dice()
                    if player2 > 21:
                        print("Player 1 won")
                        continue2 = False
                    else:
                        if input("Would you like to roll the dice again? (yes/no):") == "no":
                            continue2 = False
                            result1 = 21 - player1
                            result2 = 21 - player2
                            if result1 > result2:
                                print("Player 2 won")
                            elif result1 > result2:
                                print("Player 1 won")
                            else:
                                print("TIE")


