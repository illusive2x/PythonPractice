import random

def computer_choice():
    choice = random.choice(['r', 'p', 's'])
    return choice


def main_menu():
    print("LET'S PLAY ROCK PAPER SCISSOR\n")
    print("Enter 'r' for rock \nEnter 'p' for paper \nEnter 's' for scissors\n")


def play():
    choice = computer_choice()
    main_menu()
    user = input("Enter you choice: ")

    winner(user, choice)


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


play()