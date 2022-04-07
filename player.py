from pip._vendor.distlib.compat import raw_input
import time


class Hero:
    def __init__(self):
        self.level = 1
        self.max_hp = 3
        self.hp = self.max_hp
        self.attack = 5 + self.level
        self.defense = 5 + self.level
        self.name = ''
        self.xp = 0

    def name_self(self):
        self.name = raw_input("What do you call yourself, anyway? ")
        if self.name == "":
            self.name_self()

    def heal_self(self):
        amount = self.xp * .2
        self.hp += amount
        print("You attempt to heal yourself...")
        time.sleep(1)
        print("You healed yourself for %d HP, but used half your XP. Feels good, man." % amount)
        self.xp *= .5
        self.hp_limit()

    def hp_limit(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def death(self):
        print(f"Sorry, {self.name}, you is dead now.")
        time.sleep(1)
        print("Well, aren't you lucky, there is an afterlife after all.")

    def xp_up(self, xp):
        self.xp += xp
        print("You gain: %s XP" % xp)

    def look_self(self):
        print(f"Hello {self.name}")
        print(f"Your level is {self.level} with {self.attack} attack and {self.defense} defense.")
        print(f"You need {self.level**2 * 10} XP to level up.")

