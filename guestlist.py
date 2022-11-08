"""

This Program will create a guest list from the user
and allow the user to remove the guest or add a new one.

"""
# import only system from os
from os import system, name

# import sleep to show output for some time
from time import sleep

# define clear funcion (clears screen)
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux   
    else:
        _ = system('clear')


# function to print the title of the program
def title():
    print("Welcome to the Guest List program")
    print("You will be able to able to add or remove")
    print("guests from list.")
    sleep(2)
    
# function to add a new guest to the list
def add_guest(list):
    guest = input("Enter a guest to add: ")
    print(f"Adding '{guest}' to the guest list ...")
    list.append(guest)
    sleep(2)

# function to remove a guest from the list
def remove_guest(list):
    if not list:
        print("List is empty!")
        sleep(2)
    else:
        print(f"\n{list}")
        guest = input("Enter a guest to remove: ")
        if guest not in list:
            print(f"'{guest}' is not in the list!")
            sleep(2)
        else:
            print(f"Removing '{guest}' from the guest list ...")
            list.remove(guest)
            sleep(2)

# function to print the list
def print_list(list):
    if not list:
        print("List is empty!")
        sleep(2)
    else:
        print(*list, sep=", ")
        sleep(2)

# function to the size of the guest list
def get_list_size(list):
    size = len(list)
    return f"Number of guests: {size}\n"

# function get the user's selection
def get_user_selection():
    print("1. Add a guest")
    print("2. Remove a guest")
    print("3. Print the list")
    print("4. Exit")
    user_selection = int(input("\nEnter selection: "))
    return user_selection

# function to get user selection
def make_selection(selection, list):
    if selection == 1:
        add_guest(list)
    elif selection == 2:
        remove_guest(list)
    elif selection == 3:
        print_list(list)
    elif selection == 4:
        print("Exiting program ...")
        sleep(2)
        exit()
    else:
        print("Invalid selection!")
        sleep(2)

#create a function to exit the program
def exit_program():
    exit = input("Exiting the program? (y/n): ")
    if exit == "y":
        return True

# function to run the program
def main():
    list = []
    title()
    while True:
        clear()
        print(get_list_size(list))
        selection = get_user_selection()
        make_selection(selection, list)
        
        
if __name__ == "__main__":
    main()