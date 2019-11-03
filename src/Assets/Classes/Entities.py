class player:
    def __init__(self):
        self.name = ''
        self.xp = 0
        self.level = 0
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.money = 0
        self.armor = None
        self.weapon = None
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


class Monster:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.armor = None
        self.item = None
        self.quantity = 0
