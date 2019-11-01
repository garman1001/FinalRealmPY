# Python Text RPG
# Roy Conn

import cmd
import os
import sys
import random
import json
import importlib
import Assets.Menus.Help as Help
from pathlib import Path

filePath = Path(__file__).parent

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