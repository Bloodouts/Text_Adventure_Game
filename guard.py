from invent import *
from you_died import *
from combat import *


def guard():
    # '''
    # Encountering the guard, the player chooses to attack, check or sneak.
    # - attack: player dies and it is game over
    # - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    # - sneak: player sneaks past the guard and wins the game
    # '''
    # Actions on the guard
    actions_dict = {
        "check": "You see the guard is still sleeping, you need to get to that door on the right of him. "
                 "What are you waiting for?",
        "sneak": "You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
        "attack": "You swiftly run towards the sleeping guard and knock him out with the hilt of your shiny sword. "
                  "Unfortunately it wasn't hard enough.",
        "wake": "You approach the guard, he's still sleeping. You slightly push on the guard and he begins to open "
                "his eyes. "}
    talking_actions = {
        "taunt": "You insult the guard close family, partially his mother",
        "wave": "Waving slowly to the guard draws a confused stare back towards you.",
        "gift": "You give the guard a gift. Hoping he will let you pass."}
    gift_giving = {
        "sword": "You hand over the very shiny sword. Such a shame, hope he doesn't stab you with it.",
        "diamonds": "The hardest stone known to man, maybe... you can.. no, no ",
        "gold": "Well all tolls have to be payed some how",
        "silver": "You flip a coin to the guard. Just one more lost soul, you guess"
    }

    # While loop
    while True:
        action = input("What do you do? [attack | check | sneak | wake] > ").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the guard realised it.")
                print("You are now outside, home free! Huzzah!\n")
                return
            elif action == "wake":
                print("The Guard wakes with a grunt, and reaches for his dagger.")
                while True:
                    talk = input("What do you do? [taunt | wave | gift] > ").lower()
                    if talk in talking_actions.keys():
                        print(talking_actions[talk])
                        if talk == "gift":
                            print_inventory()
                            gift = input("What would you like to give the guard? > ").lower()
                            if gift in gift_giving.keys():
                                print(gift_giving[gift])
                                if not inventory:
                                    print("wait you don't have any inventory")
                                elif gift == "sword":
                                    you_died("The guard appears confused before he sticks the sword into your gut."
                                             " Almost like handing the murderer the knife yourself.  \n<GAME OVER>")
                                else:
                                    print("The guard is happy to see such a shiny gift and steps out of your way")
                                    print("You are now outside, home free! Huzzah!\n")
                                    del_inventory(gift)
                                    return
                        elif talk == "taunt":
                            you_died("Before you know it, the world goes dark and you have died. \n<GAME OVER>")
            elif action == "attack":
                game = Game()
                game.populate("guard")
                game.list_commands()
                game.look()
                while True:
                    game.handle_input()
                    game.update()
                    game.output()
                return

