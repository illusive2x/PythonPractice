"""

Plays a game of rock, paper, scissors
between the user and the computer.

"""

import random

# function to generate the computers choice
def computer_choice():
    choice = random.choice(['r', 'p', 's'])
    return choice

# function to print the programs main menu and description of input
def main_menu():
    print("LET'S PLAY ROCK PAPER SCISSOR\n")
    print("Enter 'r' for rock \nEnter 'p' for paper \nEnter 's' for scissors\n")

# functiont to get the user's choice
def user_input():
    user = input("Enter you choice: ")
    return user

# function to start the game
def play():
    main_menu()
    choice = computer_choice()
    user = user_input()
    winner(user, choice)

# function to determine the winner
def winner(player, opponent):
    if player == opponent:
        print("\nIt's a tie!")
        print(f"Computer: {opponent} \nUser: {player}")
    elif (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        print("\nCongrats! You win!")
        print(f"Computer: {opponent} \nUser: {player}")
    else:
        print("\nYou lose!")
        print(f"Computer: {opponent} \nUser: {player}")


# call the play function to run the program
play()