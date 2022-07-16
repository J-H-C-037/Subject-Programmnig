"""
@author: Jiahao Chen
@since: Oct 10th, 2021
@version: 1.0

Create a program which plays "Rock, paper, scissors", with the next specifications:
● There will be one player who plays against the machine.
● The number of games will be a constant in the program. The game will be repeated the
number of times indicated in this constant.
● The following message will be shown in order to ask the user for the move:
ROCK, PAPER OR SCISSORS?
● The program will randomly obtain the move (rock, paper or scissors). The program will show
the winner according to the following rules:
▪ Rock crushes scissors (Rock wins)
▪ Scissors cuts paper (Scissors wins)
▪ Paper wraps stone (Paper wins)
▪ In case of tie, the message “TIE” will be shown.
"""
import random

Num_of_games = 3

for i in range(Num_of_games):

    user_action = input("ROCK, PAPER OR SCISSORS?: ").lower()

    computer_action = ["rock", "paper", "scissors"][random.randint(0, 3)]

    print("Computer ACTION: ", computer_action)
    if user_action == computer_action:
        print("TIE")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose.")