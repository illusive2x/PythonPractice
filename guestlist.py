"""

This Program will create a guest list from the user
and allow the user to remove the guest or add a new one.

"""

# function to print the title fo the program
def title():
    print("Welcome to the Guest List program")
    
# function to add a new guest to the list
def add_guest(list):
    guest = input("Enter a guest to add: ")
    print(f"Adding '{guest}' to the guest list ...")
    list.append(guest)

#function to remove a guest from the list
def remove_guest(list):
    if not list:
        print("List is empty!")
    else:
        print(f"\n{list}")
        guest = input("Enter a guest to remove: ")
        print(f"Removing '{guest}' from the guest list ...")
        list.remove(guest)

# function to print the list
def print_list(list):
    print(f"\n{list}")

# function to the size of the guest list
def get_list_size(list):
    size = len(list)
    return f"\nNumber of guests: {size}\n"

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
        exit()
    else:
        print("Invalid selection!")

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
        print(get_list_size(list))
        selection = get_user_selection()
        make_selection(selection, list)
        
        
if __name__ == '__main__':
    main()