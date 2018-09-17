import random


class Hero():

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __stc__(self):
        return f"{self.name}, lvl:{self.level}"

    def attack(self, opponent):
        hero_roll = random.randint(1, 12) * self.level
        opponent_roll = random.randint(1, 6) * opponent.level

        if hero_roll >= opponent_roll:
            return True
        else:
            return False


class Opponent():

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"Opponent {self.name} at lvl {self.level}"
