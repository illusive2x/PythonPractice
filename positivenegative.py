"""

This program will let the user know if the numbers
entered in a list are positive or negative.

"""
# function to print out the title of the program
def title():
    print("This will let the user know if the numbers entered are positive or negative.")

# function to get the numbe of numbers to add to the list
def get_list_amount(): 
    number = int(input("How many number to enter: "))
    return number

# function to add the number to the list
def get_number_list():
    numbers = []
    number_list = get_list_amount()

    for i in range (0, number_list):
        list = int(input())
        numbers.append(list)
    return numbers

# function to check if the number is positive or negative
def check_number(number):
    for i in number:
        if i > 0:
            print(f"{i} is Positive")
        if i < 0:
            print(f"{i} is Negative")

# function to merge the othe functions together
def run():
    title()
    numbers = get_number_list()
    check_number(numbers)


# call the run function to run the program
run()
