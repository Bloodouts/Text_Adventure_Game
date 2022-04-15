from Adventure.rooms import *


def start_adventure():
    # '''
    # This function starts the adventure by allowing two options for
    # players to choose from: red or blue door
    #
    # Chosen option will print out the door chosen.
    # '''
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ").lower()

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")
        start_adventure()
