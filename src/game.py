# Python Text RPG
# Roy Conn

import os
import time
from ruamel.yaml import YAML
from pathlib import Path


filePath = Path(__file__).parent
profile_dir = f"{filePath}/Profiles"

yaml = YAML()

#################################### CLASSES ####################################

class Player:
    def __init__(self):
        self.name = ""
        self.perm_level = 1

        self.hp = 100
        self.mp = 0

        self.xp = 0
        self.level = 1

        self.money = 0

        self.monsters_defeated = 0
        self.stronghold_defeats = 0

        self.armor = {'name': "wooden", 'typeof': "basic", 'resistance': 10, 'durability': 100,
        'wear': 0, 'broken': False}
        self.weapon = {'name': "wooden", 'typeof': "basic", 'sharpness': 30, 'durability': 100,
        'wear': 0, 'broken': False}

        self.inventory = {
            'supplies': {
                'bait': 0,
                'uncooked-fish': 0,
                'wood': 0,
                'ore': 0,
                'ingots': 0
            },
            
            'food': {
                'cooked-fish': 0,
                'rations': 0,
                'steak': 0
            },

            'drops': {
                'fur': 0,
                'horns': 0,
                'crystal': 0,
                'orbs': 0
            }
        }

        self.skills = {
            'woodcutting': {
                'level': 0,
                'xp': 0
            },
            'fishing': {
                'level': 0,
                'xp': 0
            },
            'mining': {
                'level': 0,
                'xp': 0
            },
            'smithing': {
                'level': 0,
                'xp': 0
            },
            'thieving': {
                'level': 0,
                'xp': 0
            }
        }

        self.quests = {
            'monsters': {
                'one-hundred': False,
                'two-hundred': False
            },
            'levels': {
                'ten': False,
                'thirty': False,
                'fifty': False
            },
            'stronghold': {
                'defeated-one': False,
                'defeated-five': False
            }
        }

        self.bank = {
            'one': 0,
            'two': 0,
            'three': 0,
            'four': 0,
            'five': 0
        }

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


class Item:
    def __init__(self):
        self.name = ''
        self.price = 0
        self.description = ""

#################################### ITEMS ####################################

bait = Item()
bait.name = 'bait'
bait.price = 1
bait.description = "Needed to fish."

uncooked-fish = Item()
uncooked-fish.name = 'Uncooked Fish'
uncooked-fish.price = 5
uncooked-fish.description = "Obtained from the skill plot. Can be cooked into food."

wood = Item()
wood.name = 'Wood'
wood.price = 5
wood.description = "Obtained from the skill plot."

ore = Item()
ore.name = 'Ore'
ore.price = 10
ore.description = "Obtained from the skill plot; can be made into ingots."

ingot = Item()
ingot.name = 'Ingot'
ingot.price = 30
ingot.description = "Cooked Ore. Obtained from the skill plot."

# Food #

cooked-fish = Food()
cooked-fish.name = 'Cooked Fish'
cooked-fish.price = 10
cooked-fish.description = "Restores 10 hp."
cooked-fish.restorepoints = 10

rations = Food()
rations.name = 'Rations'
rations.price = 15
rations.description = "Restores 20 hp"
rations.restorepoints = 20

steak = Food()
steak.name = 'Steak'
steak.price = 30
steak.description = "Restores 50 hp"
steak.restorepoints = 50

# Drops #

fur = Item()
fur.name = 'Fur'
fur.price = 30
fur.description = "Dropped from beasts."

horns = Item()
horns.name = 'Horns'
horns.price = 40
horns.description = "Dropped from beasts."

crystal = Item()
crystal.name = 'Crystal'
crystal.price = 70
crystal.description = "Dropped from monsters."

orbs = Item()
orbs.name = 'Orbs'
orbs.price = 200
orbs.description = "Dropped from magical creatures."


#################################### MAIN MENU ####################################

global player
player = Player()

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


def help_menu():
    clearscr()
    header("Final Realm | Help")
    print('\n- Type in the number option given to perform an action')
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
    username = prompt("\nUsername:")

    profiles = os.listdir(profile_dir)
    global user_file
    user_file = f"{username}.yml"
    prof = f"{profile_dir}/{user_file}"

    if user_file in profiles:

        password = prompt("\nPassword:")

        with open(prof) as fd:
            global profile
            profile = yaml.load(fd)

        if password == profile['player']['settings']['password']:

            load_account()

            game_menu()

        else:
            print("Incorrect password.")

            ans = str(prompt("Return to menu? y/n").lower())

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
    else:
        print("Account does not exist.")
        ans = prompt("Create an account? y/n").lower()
        ans = str(ans)

        actions = {
            'y': create_account,
            'yes': create_account,
            'n': main_menu,
            'no': main_menu
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
    username = prompt("\nNew Username:")

    profile_dir = f"{filePath}/Profiles"

    if f"{username}.yml" in os.listdir(profile_dir):
        print("Profile exists!")
        main_menu()
    else:

        password = prompt("\nPassword:")

        global profilepath
        profilepath = f"{filePath}/Profiles/{username}.yml"

        command(f"cp {filePath}/Profiles/Template/player-template.yml {filePath}/Profiles/")
        command(f"mv {filePath}/Profiles/player-template.yml {profilepath}")

        with open(profilepath, 'r') as filed:
            profile = yaml.load(filed)

        profile['player']['name'] = username
        profile['player']['settings']['password'] = password

        with open(profilepath, 'w') as filed:
            yaml.dump(profile, filed)


        print("Account created!")

        ans = prompt('\nWould you like to return to the main menu? y/n').lower()

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


#################################### GAME MENU ####################################


def game_menu():
    os.system("clear")
    header("Final Realm")
    print()
    print("Stats:")
    print(f"- User: {player.name}")
    print(f"- Money: ${player.money}")
    print(f"- HP: {player.hp}")
    print(f"- MP: {player.mp}")
    print("\n")
    print("1. Wander the Wild\n")
    print("2. Skill Plot\n")
    print("3. Trading Post\n")
    print("4. Armor Shop\n")
    print("5. Weapons Shop\n")
    print("6. Legend's Store\n")
    print("7. Max's Shop\n")
    print("8. Bank\n")
    print("9. Quest Hall\n")
    print("10. The Stronghold\n")
    print("\n")
    print("100. Settings\n")
    print("101. Logout\n\n")

    ans = str(prompt("Choose an option"))

    menus = {
        '1': wild,
        '2': skill_plot,
        '3': trading_post,
        '4': armor_shop,
        '5': weapons_shop,
        '6': legend_store,
        '7': max_shop,
        '8': bank,
        '9': quest_hall,
        '10': stronghold,
        '100': settings,
        '101': logout
    }

    if ans in menus.keys():
        menus[ans]()
    else:
        while ans not in menus.keys():
            ans = prompt("Invalid choice. Choose an option")
            if ans in menus.keys():
                menus[ans]()


def wild():  # To be developed
    pass


def skill_plot():  # To be developed
    pass


def trading_post():  # To be developed
    pass


def armor_shop():  # To be developed
    pass


def weapons_shop():  # To be developed
    pass


def legend_store():  # To be developed
    pass


def max_shop():  # To be developed
    pass


def bank():
    
    clearscr()
    header("Bank")
    print("")
    print(f"Vault 1 | ${player.bank['one']}")
    print(f"Vault 2 | ${player.bank['two']}")
    print(f"Vault 3 | ${player.bank['three']}")
    print(f"Vault 4 | ${player.bank['four']}")
    print(f"Vault 5 | ${player.bank['five']}")
    print(f"Each vault is limited to $1M.")
    print(f"\nBalance: ${player.money}")
    print("\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit\n")
    ans = str(prompt("Choose an option."))

    if ans == '1' or ans == '2':

        bankv = str(prompt("\nWhich vault? 1/2/3/4/5"))

        vaults = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}
        
        if bankv in vaults.keys():
            amount = int(prompt("\nHow much?"))

            if ans is '1':

                if player.money >= amount:

                    if amount <= 1000000 and player.bank[vaults[bankv]] + amount <= 1000000:

                        player.bank[vaults[bankv]] += amount
                        player.money -= amount
                        bank()
                    
                    else:
                        
                        print("You are trying to deposit too much money!")
                        pause()
                        bank()
                else:

                    print("\nYou do not have enough to deposit!")
                    pause()
                    bank()
            
            elif ans is '2':

                if player.bank[vaults[bankv]] >= amount:

                    if amount <= 1000000 and player.bank[vaults[bankv]] - amount >= 0:
                    
                        player.bank[vaults[bankv]] -= amount
                        player.money += amount
                        bank()
                    
                    else:

                        print("You are trying to withdraw too much money!")
                        pause()
                        bank()
                    
                
                else:

                    print("\nYou do not have enough to withdraw!")
                    pause()
                    bank()
        else:

            print("Invalid vault!")
            pause()
            bank()

    elif ans == '3':
        
        game_menu()

    else:

        print("Invalid option...")
        pause()
        bank()

def quest_hall():

    determine_completed_quests()
    
    clearscr()

    header("Quest Hall")
    print("\n")
    print("[ Monsters ]")
    print(f"1. 100 Defeats: {determine_completed(player.quests['monsters']['one-hundred'])}")
    print(f"2. 200 Defeats: {determine_completed(player.quests['monsters']['two-hundred'])}")
    print()
    print()
    print("[ Levels ]")
    print(f"1. Level 10: {determine_completed(player.quests['levels']['ten'])}")
    print(f"2. Level 30: {determine_completed(player.quests['levels']['thirty'])}")
    print(f"3. Level 50: {determine_completed(player.quests['levels']['fifty'])}")
    print()
    print()
    print(f"[ Stronghold ]")
    print(f"1. 1 Defeat: {determine_completed(player.quests['stronghold']['defeated-one'])}")
    print(f"2. 5 Defeats: {determine_completed(player.quests['stronghold']['defeated-five'])}")
    
    ans = str(prompt("\nReturn to menu? y/n").lower())
    actions = {
        'y': game_menu,
        'yes': game_menu,
        'n': quest_hall,
        'no': quest_hall
    }

    if ans in actions.keys():

        actions[ans]()
    
    else:
        
        quest_hall()


def stronghold():  # To be developed
    pass


def settings():
    
    clearscr()
    header("Settings")

    print("1. Delete Account\n")
    print("2. Exit\n")

    ans = str(prompt("Choose an option:"))

    actions = {
        '1': delete_account_prompt,
        '2': game_menu
    }

    if ans in actions.keys():

        actions[ans]()
    
    else:
        while ans not in actions.keys():
            ans = str(prompt("Invalid choice. Choose an option:"))

            if ans in actions.keys():
                
                actions[ans]()


def delete_account_prompt():

    clearscr()
    header("Account Deletion")
    ans = str(prompt("Are you sure you want to delete your account? y/n").lower())

    actions = {

        'y': delete_acc,
        'yes': delete_acc,
        'n': game_menu,
        'no': game_menu

    }

    if ans in actions.keys():

        actions[ans]()

    else:
        game_menu()

def logout():

    save_account()
    main_menu()

#################################### FUNCTIONS ####################################

clearscr = lambda: os.system('clear')
command = lambda commander: os.system(f"{commander}")
prompt = lambda prompter: str(input(f"{prompter}\n\n> "))
pause = lambda: time.sleep(5)

def save_account():

    with open(f"{profile_dir}/{user_file}", "r") as f:

        prof = yaml.load(f)

    setting = prof['player']

    armor = setting['armor']
    weapon = setting['weapon']

    inventory = setting['inventory']
    supplies = inventory['supplies']
    food = inventory['food']
    drops = inventory['drops']

    skill = setting['skills']
    woodcutting = skill['woodcutting']
    fishing = skill['fishing']
    mining = skill['mining']
    smithing = skill['smithing']
    thieving = skill['thieving']

    quests = setting['quests']
    monsters = quests['monsters']
    levels = quests['levels']
    stronghold = quests['stronghold']

    bank = setting['bank']

    ######################################################
    setting['money'] = player.money
    
    setting['level'] = player.level
    setting['xp'] = player.xp
    
    setting['hp'] = player.hp
    setting['mp'] = player.mp
    
    setting['monsters_defeated'] = player.monsters_defeated
    setting['stronghold_defeats'] = player.stronghold_defeats

    armor['name'] = player.armor['name']
    armor['typeof'] = player.armor['typeof']
    armor['resistance'] = player.armor['resistance']
    armor['durability'] = player.armor['durability']
    armor['wear'] = player.armor['wear']
    armor['broken'] = player.armor['broken']

    weapon['name'] = player.weapon['name']
    weapon['typeof'] = player.weapon['typeof']
    weapon['sharpness'] = player.weapon['sharpness']
    weapon['durability'] = player.weapon['durability']
    weapon['wear'] = player.weapon['wear']
    weapon['broken'] = player.weapon['broken']

    supplies['bait'] = player.inventory['supplies']['bait']
    supplies['uncooked-fish'] = player.inventory['supplies']['uncooked-fish']
    supplies['wood'] = player.inventory['supplies']['wood']
    supplies['ore'] = player.inventory['supplies']['ore']
    supplies['ingots'] = player.inventory['supplies']['ingots']

    food['cooked-fish'] = player.inventory['food']['cooked-fish']
    food['rations'] = player.inventory['food']['rations']
    food['steak'] = player.inventory['food']['steak']

    drops['fur'] = player.inventory['drops']['fur']
    drops['horns'] = player.inventory['drops']['horns']
    drops['crystal'] = player.inventory['drops']['crystal']
    drops['orbs'] = player.inventory['drops']['orbs']

    woodcutting['level'] = player.skills['woodcutting']['level']  # Woodcutting
    woodcutting['xp'] = player.skills['woodcutting']['xp']
    fishing['level'] = player.skills['fishing']['level']  # Fishing
    fishing['xp'] = player.skills['fishing']['xp']
    mining['level'] = player.skills['mining']['level']  # Mining
    mining['xp'] = player.skills['mining']['xp']
    smithing['level'] = player.skills['smithing']['level']  # Smithing
    smithing['xp'] = player.skills['smithing']['xp']
    thieving['level'] = player.skills['thieving']['level']  # Thieving
    thieving['xp'] = player.skills['thieving']['xp']

    monsters['one-hundred'] = player.quests['monsters']['one-hundred']
    monsters['two-hundred'] = player.quests['monsters']['two-hundred']

    levels['ten'] = player.quests['levels']['ten']
    levels['thirty'] = player.quests['levels']['thirty']
    levels['fifty'] = player.quests['levels']['fifty']

    stronghold['defeated-one'] = player.quests['stronghold']['defeated-one']
    stronghold['defeated-five'] = player.quests['stronghold']['defeated-five']

    bank['one'] = player.bank['one']
    bank['two'] = player.bank['two']
    bank['three'] = player.bank['three']
    bank['four'] = player.bank['four']
    bank['five'] = player.bank['five']

    with open(f"{profile_dir}/{user_file}", 'w') as f:
        yaml.dump(prof, f)

    ######################################################


def load_account():

    with open(f"{profile_dir}/{user_file}", "r") as f:

        prof = yaml.load(f)

    setting = prof['player']

    armor = setting['armor']
    weapon = setting['weapon']

    inventory = setting['inventory']
    supplies = inventory['supplies']
    food = inventory['food']
    drops = inventory['drops']

    skill = setting['skills']
    woodcutting = skill['woodcutting']
    fishing = skill['fishing']
    mining = skill['mining']
    smithing = skill['smithing']
    thieving = skill['thieving']

    quests = setting['quests']
    monsters = quests['monsters']
    levels = quests['levels']
    stronghold = quests['stronghold']

    bank = setting['bank']

    ######################################################
    player.name = setting['name']
    player.money = setting['money']
    
    player.level = setting['level']
    player.xp = setting['xp']
    
    player.hp = setting['hp']
    player.mp = setting['mp']
    
    player.monsters_defeated = setting['monsters_defeated']
    player.stronghold_defeats = setting['stronghold_defeats']

    player.armor['name'] = armor['name']
    player.armor['typeof'] = armor['typeof']
    player.armor['resistance'] = armor['resistance']
    player.armor['durability'] = armor['durability']
    player.armor['wear'] = armor['wear']
    player.armor['broken'] = armor['broken']

    player.weapon['name'] = weapon['name']
    player.weapon['typeof'] = weapon['typeof']
    player.weapon['sharpness'] = weapon['sharpness']
    player.weapon['durability'] = weapon['durability']
    player.weapon['wear'] = weapon['wear']
    player.weapon['broken'] = weapon['broken']

    player.inventory['supplies']['bait'] = supplies['bait']
    player.inventory['supplies']['uncooked-fish'] = supplies['uncooked-fish']
    player.inventory['supplies']['wood'] = supplies['wood']
    player.inventory['supplies']['ore'] = supplies['ore']
    player.inventory['supplies']['ingots'] = supplies['ingots']

    player.inventory['food']['cooked-fish'] = food['cooked-fish']
    food['rations'] = player.inventory['food']['rations']
    food['steak'] = player.inventory['food']['steak']

    player.inventory['drops']['fur'] = drops['fur']
    player.inventory['drops']['horns'] = drops['horns']
    player.inventory['drops']['crystal'] = drops['crystal']
    player.inventory['drops']['orbs'] = drops['orbs']

    player.skills['woodcutting']['level'] = woodcutting['level']  # Woodcutting
    player.skills['woodcutting']['xp'] = woodcutting['xp']
    player.skills['fishing']['level'] = fishing['level']  # Fishing
    player.skills['fishing']['xp'] = fishing['xp']
    player.skills['mining']['level'] = mining['level']  # Mining
    player.skills['mining']['xp'] = mining['xp']
    player.skills['smithing']['level'] = smithing['level']  # Smithing
    player.skills['smithing']['xp'] = smithing['xp']
    player.skills['thieving']['level'] = thieving['level']  # Thieving
    player.skills['thieving']['xp'] = thieving['xp']

    player.quests['monsters']['one-hundred'] = monsters['one-hundred']
    player.quests['monsters']['two-hundred'] = monsters['two-hundred']

    player.quests['levels']['ten'] = levels['ten']
    player.quests['levels']['thirty'] = levels['thirty']
    player.quests['levels']['fifty'] = levels['fifty']

    player.quests['stronghold']['defeated-one'] = stronghold['defeated-one']
    player.quests['stronghold']['defeated-five'] = stronghold['defeated-five']

    player.bank['one'] = bank['one']
    player.bank['two'] = bank['two']
    player.bank['three'] = bank['three']
    player.bank['four'] = bank['four']
    player.bank['five'] = bank['five']

    ######################################################


def determine_completed(quest):

    if quest == True:
        return "Complete"
    else:
        return "Incomplete"


def determine_completed_quests():

    if player.monsters_defeated >= 100:
        player.quests['monsters']['one-hundred'] = True
    if player.monsters_defeated >= 200:
        player.quests['monsters']['two-hundred'] = True

    if player.level >= 10:
        player.quests['levels']['ten'] = True
    if player.level >= 30:
        player.quests['levels']['thirty'] = True
    if player.level >= 50:
        player.quests['levels']['fifty'] = True
    
    if player.stronghold_defeats >= 1:
        player.quests['stronghold']['defeated-one'] = True
    if player.stronghold_defeats >= 5:
        player.quests['stronghold']['defeated-five'] = True

def header(title):  # Draws a border around the specified title

    length = len(title)
    string = '#' * length
    string2 = string + ('#' * 4)
    whitelength = ' ' * length
    whitelength2 = f'# {whitelength} #'
    text = f'# {title} #'
    print(f"{string2}\n{whitelength2}\n{text}\n{whitelength2}\n{string2}")

def delete_acc():
    os.remove(f"{profile_dir}/{user_file}")
    main_menu()

def exit_game():

    clearscr()
    exit()


try:
    main_menu()
except KeyboardInterrupt:
    exit_game()
