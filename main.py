#
# Added coded in main(),and create a function to ask for your name and return it.
#

from start_adventure import *
from player import *


def main():
    # '''
    # Gets the players name by calling get_player_name() before starting the adventure.
    # '''
    player_name = get_player_name()

    ####################################################################
    # ACTIVITIES
    #
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modify blue_door_room()'s if statement
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################

    start_adventure()

    print("\nThe end\n")
    print(f"Thanks for playing, {player_name.upper()}")


if __name__ == '__main__':
    main()
