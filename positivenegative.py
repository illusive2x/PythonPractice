"""

This program will let the user know if the numbers
entered in a list are positive or negative.

"""

def title():
    print("This will let the user know if the numbers entered are positive or negative.")

def get_list_amount(): 
    number = int(input("How many number to enter: "))
    return number

def check_number(number):
    for i in number:
        if i > 0:
            print(f"{i} is Positive")
        if i < 0:
            print(f"{i} is Negative")

def get_number_list():
    numbers = []
    number_list = get_list_amount()

    for i in range (0, number_list):
        list = int(input())
        numbers.append(list)
    return numbers

def run():
    title()
    numbers = get_number_list()
    check_number(numbers)


if __name__ == '__main__':
    run()
