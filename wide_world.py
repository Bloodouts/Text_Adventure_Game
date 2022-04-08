import random
from player import *
from pip._vendor.distlib.compat import raw_input


class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(2, 10)
        self.attack = random.randint(2, 5)
        self.defense = random.randint(2, 5)
        self.xp = random.randint(2, 8)


class Room:
    def __init__(self, key):
        self.room_data = {
            "road": {"description": "A fork road lays out before you. The right path runs through a forest, "
                                    "on the left a lake", "exits": ["forest", "lake"]},
            "forest": {"description": "You're in a dark forest. It's fairly gloomy.", "exits": ["road", "lake"]},
            "lake": {"description": "You see a lake circled by rocks. It's too cold to swim.",
                     "exits": ["forest", "mountain"]},
            "mountain": {"description": "You can see for miles around. Don't fall off.", "exits": ["lake"]},
            }
        self.description = self.room_data[key]["description"]
        self.exits = self.room_data[key]["exits"]
        self.name = str(key)
        self.monster_list = {}


class Adventure:
    def __init__(self):
        self.command_list = ["look", "name", "fight", "heal", 'report', 'move', 'exit', '?']
        self.hero = Hero()
        self.current_room = Room("road")

    def list_commands(self):
        print('Commands are', ', '.join(self.command_list[:-1]), 'and', self.command_list[-1] + '.')

    def handle_input(self):
        com = raw_input(self.prompt()).lower().split()
        if len(com) < 1:
            print("Huh?")
        elif com[0] == "fight":
            if len(com) > 1:
                if com[1] in self.current_room.monster_list:
                    self.combat(self.hero, self.current_room.monster_list[com[1]])
            else:
                print("Fight what?")
        elif com[0] == "report":
            self.hero.look_self()
        elif com[0] == "look":
            if len(com) > 1:
                if com[1] in self.current_room.monster_list:
                    self.look_monster(self.current_room.monster_list[com[1]])
                else:
                    print("You don't see that monster.")
            else:
                self.look()
        elif com[0] == "move":
            if len(com) > 1:
                self.move(com[1])
            else:
                print("Move where?", "You can exit to: %s" % ', '.join(self.current_room.exits))
        elif com[0] == "name":
            self.hero.name_self()
        elif com[0] == "info":
            self.hero.look_self()
            self.look_monster(self.current_room.monster_list[com[1]])
        elif com[0] == "heal":
            self.hero.heal_self()
        elif com[0] == "exit":
            return
        else:
            self.list_commands()

    def combat(self, attacker, defender):
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
                print("The %s hit you for %s HP and it hurt real bad.") % (defender.name.capitalize(), str(attack))
                self.hero.hp -= attack
                if self.hero.hp < 2:
                    print("You attempt to escape...")
                    time.sleep(1)
                    break
            time.sleep(.5)
        if defender.hp < 1:
            print("You killed the %s. How sad for the %s's family." % (defender.name.capitalize(),
                                                                       defender.name.capitalize()))
            self.hero.xp_up(defender.xp)
            del self.current_room.monster_list[defender.name]
            self.list_commands()
            print(self.current_room.description)
            print("You can exit to: %s" % ', '.join(self.current_room.exits))
        if self.hero.hp < 1:
            self.hero.death()

    def level_up(self):
        if self.hero.xp > self.hero.level**2 * 10:
            self.hero.level += 1
            print("You've reached level " + str(self.hero.level))
            self.hero.max_hp += self.hero.level
            self.hero.hp = self.hero.max_hp

    def populate(self):
        for i in range(self.hero.level):
            new_monster = random.choice(["ogre", "orc", "goblin"])
            self.current_room.monster_list[new_monster] = Monster(new_monster)

    def look(self):
        self.list_commands()
        print(self.current_room.description)
        print("You can exit to: %s" % ', '.join(self.current_room.exits))
        monster_list = []
        for name in self.current_room.monster_list:
            monster_list.append(self.current_room.monster_list[name].name.capitalize())
        if monster_list:
            print("You see: %s" % ', '.join(monster_list))

    def look_monster(self, monster):
        print("The %s has %s HP, %s attack, %s defense, and is worth %s XP." % (monster.name.capitalize(),
                                                                                monster.hp,
                                                                                monster.attack,
                                                                                monster.defense,
                                                                                monster.xp))

    def move(self, exit):
        if exit in self.current_room.exits:
             self.current_room = Room(exit)
             self.populate()
             self.look()
        elif exit == self.current_room.name:
            print("You're already here.")
        else:
            print("You can't get there from here.")

    def update(self):
        self.level_up()
        if self.hero.hp <= 0:
            self.hero.death()
            time.sleep(2)
            adventure = Adventure()

    def prompt(self):
        return '\n' + self.hero.name + " HP:" + str(int(self.hero.hp)) + " XP:" + str(self.hero.xp) + " >"

    def output(self):
        pass











