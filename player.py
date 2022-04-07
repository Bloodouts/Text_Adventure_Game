

def get_player_name():
    # '''
    # Gets players name, may or may not be renamed depending on player's choice.
    # Returns: Player name back (altered or unaltered)
    # '''
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You are fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure.")
    else:
        print(f"Trying to be funny? Well, you will now be called {alt_name.upper()} anyway.")
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.
    # This is why indentation is important, variables declared in this block only exists in that block
    return name


class Warrior:
    def __init__(self, health, attack_1, attack_2, attack_3, heal):
        self.health = health
        self.attack_1 = attack_1
        self.attack_2 = attack_2 # tuple ie (5,25) representing range for attack value
        self.attack_3 = attack_3 # tuple ie (10,20) representing range for attack value
        self.heal = heal # tuple ie (10,20) representing range for health value

    def attributes(self):
        # string containing the attributes of the character
        string = "Health: " + str(self.health) + " Attack 1: " + str(self.attack_1) + " Attack 2: " \
                 + str(self.attack_2[0]) + "-" + str(self.attack_2[1]) + " Attack 3: " + str(self.attack_3[0]) + "-"\
                 + str(self.attack_3[1]) + " Heal:" + str(self.heal[0]) + "-" + str(self.heal[0])
        return string

    def is_dead(self):
        return self.health <= 0


knight = Warrior(100, 10, (5, 15),  (5, 25),  (5, 10))
mage = Warrior(50,  15, (10, 20), (-5, 25), (10, 15))
healer = Warrior(150, 5,  (5, 10),  (5, 15),  (10, 20))

while True:
    print("\n1. Knight: ", knight.attributes())
    print("\n2. Mage:   ", mage.attributes())
    print("\n3. Healer: ", healer.attributes())
    player_class = input("\nSelect your class: 1, 2, or 3: ")
    if player_class == "1":
        player_class = knight
        print("You have selected the Knight class.")
        break
    elif player_class == "2":
        player_class = mage
        print("You have selected the Mage")
        break
    elif player_class == "3":
        player_class = healer
        print("You have selected the Healer")
        break
    else:
        print("Please select a valid class.")
        continue

player_heal_max = player_class.health
