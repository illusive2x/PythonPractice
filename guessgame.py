"""

This a guess game. The user will try to guess 
a random number generated by the program.

"""
# import random class to generate a random number
import random

# fucntion to print the title of the program
def title():
    print('Welcome to Guessing Game')
    print('Choose a number between 1 and 100\n')

# function to generate a random number and return the value
def generate_random():
    number = random.randint(1, 100)
    return number

# function to get the user's input number and return the value
def user_number():
    number = int(input('Enter a number: '))
    return number
    
# function to check if the user guess the number correctly or not
def play():
    title()
    random_num = generate_random()
    attempts = 1

    while True:
        guess = user_number()
        if guess == random_num:
            print(f'Congrat! You guess the number in {attempts} attempts')
            break
        elif guess < random_num:
            print('Your guess was lower -- try again.\n')
        
        elif guess > random_num:
            print('Your guess was higher -- try again.\n')
        
        attempts += 1


# call the play function to run the game
play()