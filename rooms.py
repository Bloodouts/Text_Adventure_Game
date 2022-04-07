from start_adventure import *
from guard import *
from invent import *


# ROOMS #
def blue_door_room():
    # '''
    # The player finds a treasure chest, options to investigate the treasure chest or guard.
    #
    # If player chooses
    # - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
    # - Guard: After checking treasure chest, ignoring treasure chest to check guard, it calls guard() function
    # '''
    # So our treasure_chest list contains 4 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print(
        "You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in "
        "front of the door")

    # Ask player what to do.
    action = input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            # Get number of items in treasure chest with len))
            num_items_in_chest = len(treasure_chest)

            print(f"Take all {num_items_in_chest} treasure, press '1'")
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                treasure_chest.remove("sword")
                print("\tYou take the shinier sword from the treasure chest. It does looks exceedingly shiny.")
                print("\tWoohoo! Bounty and a shiny new sword. /drops your crappy sword in the empty treasure chest.")

                temp_treasure_list = treasure_chest[:]
                treasure_contents = ", ".join(treasure_chest)
                # Add treasure to inventory
                add_to_inventory(treasure)
                print(f"\tYou also receive {treasure_contents}.")

                # Removing all the rest of the items in the treasure chest
                for treasure in temp_treasure_list:
                    # Use list remove() function to remove each item in the chest.
                    treasure_chest.remove(treasure)

                # Add the old sword in place of the new sword
                del_inventory("crappy sword")
                treasure_chest.append("crappy sword")
                print(f"\tYou close the lid of the chest containing {treasure_chest} for the next adventurer. /grins")
                print("Now onward to get past this sleeping guard and the door to freedom.")
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
        elif choice == "2":
            print("Who needs treasure, let's get out of here.'")
    elif action.lower() in ["guard", "right"]:
        print("Let's have fun with the guard.")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
    guard()


def red_door_room():
    # '''
    # The red door room contains a red dragon.
    #
    # If a player types "flee" as an answer, player returns to the room with two doors,
    # otherwise the player dies.
    # '''
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
