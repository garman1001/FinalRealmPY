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

# Import Menus
loadfolder(1, f'{filePath}/Assets/Menus')
from Menus import Help, Login, CreateAccount, GameMenu

"""
# Imports Classes
loadfolder(1, f'{filePath}/Assets/Classes/')
from Classes import Entities
from Classes import Items
from Classes import Combat

# Import shops
loadfolder(2, f'{filePath}/Assets/Shops/')
from Shops import ArmorShop
from Shops import MaxShop
from Shops import TradingPost
from Shops import WeaponShop

loadfolder(3, f'{filePath}/Assets/Menus/')
from Menus import Help
from Menus import TitleScreen
"""

def menu():
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
    selections()

def selections():
    options = ["play", "help", "log in", "new game", "quit"]

    option = input("> ")
    if option.lower() == options[0]:
        GameMenu.menu() # placeholder until written
    elif option.lower() == options[1]:
        Help.menu()
    elif option.lower() == options[2]:
        Login.menu()
    elif option.lower() == options[3]:
        CreateAccount.menu()
    elif option.lower() == options[4]:
        exit()
    while option.lower() not in options:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == options[0]:
            GameMenu.menu() # placeholder until written
        elif option.lower() == options[1]:
            Help.menu()
        elif option.lower() == options[2]:
            Login.menu()
        elif option.lower() == options[3]:
            CreateAccount.menu()
        elif option.lower() == options[4]:
            exit()


menu()