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