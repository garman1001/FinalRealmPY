import sys
import cmd
import os
import random
from ruamel.yaml import YAML
from src.main import main_menu
from pathlib import Path

user = "placeholder"
balance = "placeholder"
hp = "placeholder"
perm_level = 0


def header(title):  # Draws a border around the specified title
    length = len(title)
    string = '#' * length
    string2 = string + ('#' * 4)
    whitelength = ' ' * length
    whitelength2 = f'# {whitelength} #'
    text = f'# {title} #'
    print(f"{string2}\n{whitelength2}\n{text}\n{whitelength2}\n{string2}")


def game_menu():
    os.system("clear")
    header("Final Realm")
    print()
    print("Stats:")
    print(f"User: {user}")
    print(f"Balance: {balance}")
    print(f"HP: {hp}")
    print("\n\n\n")
    print("1. Wander the Wild\n")
    print("2. Skill Plot\n")
    print("3. Trading Post\n")
    print("4. Armor Shop\n")
    print("5. Weapons Shop\n")
    print("6. Legend's Store\n")
    print("7. Max's Shop\n")
    print("8. Bank\n")
    print("9. Quest Hall")
    print("10. The Stronghold")
    print("\n\n\n\n\n")
    if perm_level > 0:
        print("99. Admin Console")
    print("100. Settings")
    print("101. Logout")

    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "99", "100", "101"]

    ans = input("Please try again.\n\nChoose an option\n> ")
    if ans == options[0]:  # Wander the wild
        print("1")  # Placeholder

    elif ans == options[1]:  # Skill plot
        print("1")  # Placeholder

    elif ans == options[2]:  # Trading Post
        print("1")  # Placeholder

    elif ans == options[3]:  # Armor Shop
        print("1")  # Placeholder

    elif ans == options[4]:  # Weapons Shop
        print("1")  # Placeholder

    elif ans == options[5]:  # Legend's Store
        print("1")  # Placeholder

    elif ans == options[6]:  # Max's Shop
        print("1")  # Placeholder

    elif ans == options[7]:  # Bank
        print("1")  # Placeholder

    elif ans == options[8]:  # Quest Hall
        print("1")  # Placeholder

    elif ans == options[9]:  # The Stronghold
        print("1")  # Placeholder

    elif ans == options[10]:  # Admin Console
        print("1")  # Placeholder

    elif ans == options[11]:  # Settings
        print("1")  # Placeholder

    elif ans == options[12]:  # Logout
        main_menu()

    else:
        while ans not in options:
            ans = input("Please try again.\n\nChoose an option\n> ")
            if ans == options[0]:  # Wander the wild
                print("1")  # Placeholder

            elif ans == options[1]:  # Skill plot
                print("1")  # Placeholder

            elif ans == options[2]:  # Trading Post
                print("1")  # Placeholder

            elif ans == options[3]:  # Armor Shop
                print("1")  # Placeholder

            elif ans == options[4]:  # Weapons Shop
                print("1")  # Placeholder

            elif ans == options[5]:  # Legend's Store
                print("1")  # Placeholder

            elif ans == options[6]:  # Max's Shop
                print("1")  # Placeholder

            elif ans == options[7]:  # Bank
                print("1")  # Placeholder

            elif ans == options[8]:  # Quest Hall
                print("1")  # Placeholder

            elif ans == options[9]:  # The Stronghold
                print("1")  # Placeholder

            elif ans == options[10]:  # Admin Console
                print("1")  # Placeholder

            elif ans == options[11]:  # Settings
                print("1")  # Placeholder

            elif ans == options[12]:  # Logout
                main_menu()
