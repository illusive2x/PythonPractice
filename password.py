import random


# function to get number of passwords to generate
def get_number_passwords():
    number_passwords = int(input('Enter number of passwords to generate: '))
    return number_passwords


# function to get the length of the passwords
def get_passwords_length():
    password_length = int(input('Enter password length: '))
    return password_length


# function to generate the passwords
def generate_passwords():
    num_passwords = get_number_passwords()
    password_length = get_passwords_length()

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

    passwords = []

    for i in range(num_passwords):
        password = ''.join(random.sample(letters, password_length))
        passwords.append(password)

    return passwords


def run():
    print('Welcome to Password Generator\n')
    passwords = generate_passwords()
    print('')
    print(*passwords, sep= '\n')


if __name__ == '__main__':
    run()