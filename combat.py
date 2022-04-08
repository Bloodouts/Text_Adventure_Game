from player import *
import random


class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(2, 10)
        self.attack = random.randint(2, 5)
        self.defense = random.randint(2, 5)
        self.xp = random.randint(2, 8)
        self.monster_list = {}


class Game:
    def __init__(self):
        self.command_list = ["look", "name", "fight", "heal", 'report', 'quit', '?']
        self.hero = Hero()
        self.monster = Monster(" ")

    def list_commands(self):
        print('Commands are', ', '.join(self.command_list[:-1]), 'and', self.command_list[-1] + '.')

    def handle_input(self):
        com = raw_input(self.prompt()).lower().split()
        if len(com) < 1:
            print("Huh?")
        elif com[0] == "fight":
            if len(com) > 1:
                if com[1] in self.monster.monster_list:
                    self.fight_monster(self.hero, self.monster.monster_list[com[1]])
            else:
                print("Fight what?")
        elif com[0] == "report":
            self.hero.look_self()
        elif com[0] == "look":
            if len(com) > 1:
                if com[1] in self.monster.monster_list:
                    self.look_monster(self.monster.monster_list[com[1]])
                else:
                    print("You don't see that monster.")
            else:
                self.look()
        elif com[0] == "name":
            self.hero.name_self()
        elif com[0] == "info":
            self.hero.look_self()
            self.look_monster()
        elif com[0] == "heal":
            self.hero.heal_self()
        elif com[0] == "exit":
            return
        else:
            self.list_commands()

    def fight_monster(self, attacker, defender):
        while defender.hp > 0 and attacker.hp > 0:
            attack = int(random.random() * attacker.attack)
            defense = int(random.random() * defender.defense)
            print("Attack: %s vs Defense: %s" % (str(attack), str(defense)))
            if attack > defense:
                print("You hit the %s for %s HP." % (defender.name.capitalize(), str(attack)))
                defender.hp -= attack
            elif attack == defense:
                print("The attack missed. You feel kind of disappointed.")
            else:
                print(f"The {defender.name} hit you for {str(attack)} HP and it hurt real bad.")
                self.hero.hp -= attack
                if self.hero.hp < 2:
                    print("You attempt to escape...")
                    time.sleep(1)
                    break
            time.sleep(.5)
        if defender.hp < 1:
            print(f"You killed the {defender.name}. How sad for the {defender.name}'s family.")
            self.hero.xp_up(defender.xp)
            del self.monster.monster_list[defender.name]
            return
        if self.hero.hp < 1:
            self.hero.death()

    def level_up(self):
        if self.hero.xp > self.hero.level**2 * 10:
            self.hero.level += 1
            print("You've reached level " + str(self.hero.level))
            self.hero.max_hp += self.hero.level
            self.hero.hp = self.hero.max_hp

    def populate(self, name):
        for i in range(self.hero.level):
            new_monster = name
            self.monster.monster_list[new_monster] = Monster(new_monster)

    def look(self):
        monster_list = []
        for name in self.monster.monster_list:
            monster_list.append(self.monster.monster_list[name].name.capitalize())
        if monster_list:
            print("You see: %s" % ', '.join(monster_list))

    def look_monster(self, monster):
        print(f"The {monster.name.capitalize} has {monster.hp} HP, "
              f"{monster.attack} attack, {monster.defense} defense, and is worth {monster.xp} XP.")

    def update(self):
        self.level_up()
        if self.hero.hp <= 0:
            self.hero.death()
            time.sleep(2)

    def prompt(self):
        return '\n' + self.hero.name + " HP:" + str(int(self.hero.hp)) + " XP:" + str(self.hero.xp) + " >"

    def output(self):
        pass
