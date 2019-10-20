import os
import TitleScreen

def menu():
    os.system('clear')
    print('#############################')
    print('#                           #')
    print('#  Welcome to Final Realm!  #')
    print('#                           #')
    print('#############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    print('\nWould you like to return to the help menu?\n')
    selections()

def selections():
    option = ['y', 'n', 'yes', 'no']
    shell = input('> ')
    if shell.lower() == option[0] or shell.lower() == option[2]:
        TitleScreen.menu()
    elif shell.lower() == option[2] or shell.lower() == option[3]:
        menu()
    while shell.lower() not in option:

        print('Please enter a valid answer.\n')

        option = ['y', 'n', 'yes', 'no']
        shell = input('> ')
        if shell.lower() == option[0] or shell.lower() == option[2]:
            TitleScreen.menu()
        elif shell.lower() == option[1] or shell.lower() == option[3]:
            menu()
    selections()