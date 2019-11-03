# Python Text RPG
# Roy Conn

import os
from pathlib import Path

filePath = Path(__file__).parent


def header(title):  # Draws a border around the specified title
    length = len(title)
    string = '#' * length
    string2 = string + ('#' * 4)
    whitelength = ' ' * length
    whitelength2 = f'# {whitelength} #'
    text = f'# {title} #'
    print(f"{string2}\n{whitelength2}\n{text}\n{whitelength2}\n{string2}")


def main_menu():
    os.system('clear')
    header('Welcome to Final Realm!')
    print()
    print('1. Log in')
    print('2. Create Account')
    print('3. Help')
    print('4. Quit')
    print()
    print()
    print('   Copyright 2019 RoyConn    \n')
    options = ["1", "2", "3", "4"]

    option = input("> ")
    option = str(option)
    if option == options[0]:
        login_menu()
    elif option == options[1]:
        create_account()
    elif option == options[2]:
        help_menu()
    elif option == options[3]:
        exit()

    else:
        while option not in options:
            print("Please enter a valid command.")
            option2 = input("> ")
            option2 = str(option2)
            if option2 == options[0]:
                login_menu()
            elif option2 == options[1]:
                create_account()
            elif option2 == options[2]:
                help_menu()
            elif option2 == options[3]:
                exit()
    main_menu()


def help_menu():
    os.system('clear')
    header("Final Realm | Help")
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    print('\nWould you like to return to the help menu? y/n\n')

    option = ['y', 'n', 'yes', 'no']
    shell = input('> ')
    if shell.lower() == option[0] or shell.lower() == option[2]:
        help_menu()
    elif shell.lower() == option[1] or shell.lower() == option[3]:
        main_menu()
    else:
        while shell.lower() not in option:

            print('Please enter a valid answer.\n')

            option = ['y', 'n', 'yes', 'no']
            shell = input('> ')
            if shell.lower() == option[0] or shell.lower() == option[2]:
                main_menu()
            elif shell.lower() == option[1] or shell.lower() == option[3]:
                help_menu()
    help_menu()


def login_menu():  # To Be Developed w/ YAML support
    return


def create_account():  # To Be Developed w/ YAML support
    return


main_menu()
