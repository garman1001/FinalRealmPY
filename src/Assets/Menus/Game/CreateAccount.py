import cmd
import os
import sys
import random
import json
import importlib
import Assets.Menus.Help as Help
from pathlib import Path

path = Path(__file__).parent.parent.parent

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yamp.dump(data, file_descriptor)

if __name__ == "__main__":
    file_path = 'Profiles/'