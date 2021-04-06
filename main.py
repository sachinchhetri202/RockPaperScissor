''' 
    * Rock, Paper, Scissor Game with Python.
    * @author Sachin Chhetri <sachinchhetri202@gmail.com>
    * Use of Random, creating functions, if/elif clause, and calling a function.  
'''

import random


def play():
    print("Choose: 'r' for Rock\n\t    'p' for Paper\n\t    's' for Scissor")
    user = input("ENTER: ")
    comp = random.choice(['r', 'p', 's'])  # computer chooses randomly from those three letters

    if user == comp:  # While the comp and user chooses the same option
        print(f"Computer choose {comp}.")
        return "It's a tie"

    if isWin(user, comp):
        print(f"Computer choose {comp}")
        return "You won"

    return f"Computer choose {comp}.\nYou lose.Try again."


def isWin(player, opponent):
    # return true if player wins
    # r -> s, s -> p, p -> r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())  # calling out the function
