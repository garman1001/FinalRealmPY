# Python Text RPG
# Roy Conn

import os
import sys
from ruamel.yaml import YAML
from pathlib import Path

filePath = Path(__file__).parent

yaml = YAML(typ='safe')

clearscr = lambda: os.system('clear')
command = lambda commander: os.system(f"{commander}")
prompt = lambda prompter: str(input(f"{prompter}\n\n> "))

################## CLASSES ##################
class Player:
    def __init__(self):
        self.name = ""
        self.perm_level = 1

        self.hp = 100
        self.mp = 0
        self.status_effect = ""

        self.xp = 0
        self.level = 1

        self.money = 0

        self.armor = ""
        self.weapon = ""
        self.inventory = []

class NPC:
    def __init__(self):
        self.name = ''
        self.hp = ''
        self.money = 0
        self.occupation = ''
        self.mood = ''
        self.item = None
        self.price = 0
        self.quantity = 0


class Enemy:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.armor = None
        self.item = None
        self.quantity = 0


class Armor:
    def __init__(self):
        self.price = 0
        self.helmet = ''
        self.chestplate = ''
        self.leggings = ''
        self.boots = ''

        self.helmet.durability = 0
        self.chestplate.durability = 0
        self.leggings.durability = 0
        self.boots.durability = 0

        self.helmet.damage = 0
        self.chestplate.damage = 0
        self.leggings.damage = 0
        self.boots.damage = 0


class Weapon:
    def __init__(self):
        self.price = 0
        self.durability = 0
        self.damage = 0
        self.attackdamage = 0


class Food:
    def __init__(self):
        self.name = ''
        self.price = 0
        self.description = ""
        self.restorepoints = 0
        self.saturation = 0


class Item:
    def __init__(self):
        self.name = ''
        self.price = 0
        self.description = ""
        self.quantity = 0


################## MENUS ##################


def header(title):  # Draws a border around the specified title

    length = len(title)
    string = '#' * length
    string2 = string + ('#' * 4)
    whitelength = ' ' * length
    whitelength2 = f'# {whitelength} #'
    text = f'# {title} #'
    print(f"{string2}\n{whitelength2}\n{text}\n{whitelength2}\n{string2}")


def main_menu():
    clearscr()
    header('Welcome to Final Realm!')
    print()
    print('1. Log in')
    print('2. Create Account')
    print('3. Help')
    print('4. Quit')
    print()
    print()
    print('Copyright 2019 RoyConn    \n')

    ans = prompt("Enter an option:")

    ans = str(ans)

    actions = {
        '1': login_menu,
        '2': create_account,
        '3': help_menu,
        '4': exit_game
    }

    if ans in actions.keys():
        actions[ans]()

    else:
        while ans not in actions.keys():
            ans = int(prompt("Invalid choice. Enter an option:"))
            ans = int(ans)

            if ans in actions.keys():
                actions[ans]()


def exit_game():

    clearscr()
    exit()


def help_menu():
    clearscr()
    header("Final Realm | Help")
    print('- Type in the number option given to perform an action')
    print('- Don\'t die')
    ans = str(prompt('\nWould you like to return to the help menu? y/n').lower())

    actions = {
        'y': help_menu,
        'yes': help_menu,
        'n': main_menu,
        'no': main_menu
    }

    if ans in actions.keys():
        actions[ans]()

    else:
        while ans not in actions.keys():
            ans = prompt("Invalid choice. Would you like to return to the help menu? y/n").lower()
            ans = str(ans)
            if ans in options:
                actions[ans]()


def login_menu():

    clearscr()
    header("Login")
    username = prompt("Username:")
    password = prompt("Password")

    profiles = os.listdir(f"{filePath}/Profiles")
    file = f"{username}.yml"
    if file in profiles:
        profile = yaml.load(file)

        if password == profile['settings']['password']:
            player = Player
            game_menu(player)

        else:
            print("Incorrect password.")
            main_menu()
    else:
        print("Account does not exist.")
        ans = prompt("Return to menu? y/n").lower()
        ans = str(ans)

        actions = {
            'y': main_menu,
            'yes': main_menu,
            'n': exit,
            'no': exit
        }

        if ans in actions.keys():
            actions[ans]()
        else:
            while ans not in actions.keys():
                ans = prompt("Invalid choice. Return to menu? y/n")

                if ans in actions.keys():
                    actions[ans]()


def create_account():

    clearscr()
    header("Account Creation")
    username = prompt("New Username:")
    password = prompt("Password:")

    command(f"cp {filePath}/Configs/Templates/player-template.yml {filePath}/Profiles/")
    command(f"mv {filePath}/Profiles/player-template.yml {filePath}/Profiles/{username}.yml")

    profile = yaml.load(f"{filePath}/Profiles/{username}.yml")
    profile['player']['name'] = username
    profile['settings']['password'] = password

    yaml.dump(profile)

    global player
    player = Player
    player.name = username


    print("Account created!")

    ans = prompt('\nWould you like to return to the help menu? y/n').lower()

    actions = {
        'y': main_menu,
        'yes': main_menu,
        'n': exit,
        'no': exit
    }

    if ans in actions.keys():
        actions[ans]()

    else:
        while ans.lower() not in actions.keys():

            ans = prompt('Please enter a valid answer.')
            if ans in actions.keys():
                actions[ans]()


def game_menu(player_account):
    os.system("clear")
    header("Final Realm")
    print()
    print("Stats:")
    print(f"User: {player_account.name}")
    print(f"Balance: {player_account.money}")
    print(f"HP: {player_account.hp}")
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
    if player_account.perm_level > 0:
        print("99. Admin Console")
    print("100. Settings")
    print("101. Logout")

    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99, 100, 101]

    ans = str(prompt("Choose an option"))

    menus = {
        '1': wild(),
        '2': skill_plot(),
        '3': trading_post(),
        '4': armor_shop(),
        '5': weapons_shop(),
        '6': legend_store(),
        '7': max_shop(),
        '8': bank(),
        '9': quest_hall(),
        '10': stronghold(),
        '99': admin_console(),
        '100': settings(),
        '101': main_menu()
    }

    if ans in options:
        menus.get(ans, default='1')
    else:
        while ans not in options:
            ans = prompt("Invalid choice. Choose an option")
            if ans in options:
                menus.get(ans, default='1')


def wild():
    pass


def skill_plot():
    pass


def trading_post():
    pass


def armor_shop():
    pass


def weapons_shop():
    pass


def legend_store():
    pass


def max_shop():
    pass


def bank():
    pass


def quest_hall():
    pass


def stronghold():
    pass


def admin_console():
    pass


def settings():
    pass


try:
    main_menu()
except KeyboardInterrupt:
    exit_game()