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
loadfolder(2, f'{filePath}/Assets/Shops/')
from Shops import ArmorShop
from Shops import MaxShop
from Shops import TradingPost
from Shops import WeaponShop

loadfolder(3, f'{filePath}/Assets/Menus/')
from Menus import Help
from Menus import TitleScreen

profile_folder = f"{filePath}/Profiles"

def create_account():
    username = input("What would you like your username to be?\n\n> ")
    open(f"{profilePath}/{username}.json", "w")



def start_game():
    print("In development!")
    exit()


title_screen()
