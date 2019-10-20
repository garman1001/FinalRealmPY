# Python Text RPG
# Roy Conn

import cmd
import os
import sys
import random
import json
from pathlib import Path

filePath = Path(__file__).parent
loadfolder = lambda num, path : sys.path.append(num, path)

# Imports Classes
loadfolder(1, f'{filePath}/Assets/Classes/')
from Classes import Entities
from Classes import Items
from Classes import Combat

# Import shops
loadfolder(1, f'{filePath}/Assets/Shops/')
from Shops import ArmorShop
from Shops import MaxShop
from Shops import TradingPost
from Shops import WeaponShop

profile_folder = f"{filePath}/Profiles"


myPlayer = Entities.player()

################ TITLE SCREEN ################


def title_screen_selections():
    options = ["play", "help", "log in", "new game", "quit"]

    option = input("> ")
    if option.lower() == options[0]:
        start_game() # placeholder until written
    elif option.lower() == options[1]:
        help_menu()
    elif option.lower() == options[2]:
        login()
    elif option.lower() == options[3]:
        create_account()
    elif option.lower() == options[4]:
        sys.exit()
    while option.lower() not in options:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == options[0]:
            start_game() # placeholder until written
        elif option.lower() == options[1]:
            help_menu()
        elif option.lower() == options[2]:
            login()
        elif option.lower() == options[3]:
            create_account()
        elif option.lower() == options[4]:
            sys.exit()


def title_screen():
    os.system('clear')
    print('#############################')
    print('#                           #')
    print('#  Welcome to Final Realm!  #')
    print('#                           #')
    print('#############################')
    print('         - Log in -           ')
    print('        - New Game -         ')
    print('          - Help -           ')
    print('          - Quit -           ')
    print('   Copyright 2019 RoyConn    \n')
    title_screen_selections()

################ HELP MENU ################


def help_selections():
    option = ['y', 'n', 'yes', 'no']
    shell = input('> ')
    if shell.lower() == option[0] or shell.lower() == option[2]:
        title_screen()
    elif shell.lower() == option[2] or shell.lower() == option[3]:
        help_menu()
    while shell.lower() not in option:

        print('Please enter a valid answer.\n')

        option = ['y', 'n', 'yes', 'no']
        shell = input('> ')
        if shell.lower() == option[0] or shell.lower() == option[2]:
            title_screen()
        elif shell.lower() == option[1] or shell.lower() == option[3]:
            help_menu()
    title_screen()


def help_menu():
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
    help_selections()

################ GAME CODE ################

def create_account():
    username = input("What would you like your username to be?\n\n> ")
    open(f"{profilePath}/{username}.json", "w")



def start_game():
    print("In development!")
    exit()


title_screen()
