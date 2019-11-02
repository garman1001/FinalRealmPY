import os
import yaml
from pathlib import Path
from src import main


path = Path(__file__).parent.parent.parent
profile_path = f'{path}/Profiles/'


def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)


clear = lambda : os.system('clear')  # Clears the screen
command = lambda com: os.system(f"{com}")  # Runs a command in the Linux console


def menu():
    clear()
    command(f"cp {path}/Assets/Configs/Templates/player-template.yml {profile_path}")
    username = input("Enter a username:\n\n> ")
    command(f"mv {profile_path}/player-template.yml {profile_path}/{username}.yml")
    profile = yaml_loader(f"{profile_path}/{username}.yml")

    password = input("Enter a password:\n\n> ")
    profile['player.settings.password'] = password

    yaml_dump(f"{profile_path}/{username}.yml", profile)

    print("Profile Created!")
    main.menu()
