from start_adventure import *
from combat import *


def main():
    # '''
    # Gets the players name by calling get_player_name() before starting the adventure.
    # '''
    game = Game()

    print("Welcome, adventurer.")
    game.list_commands()
    game.hero.name_self()
    game.hero.look_self()

    start_adventure()


if __name__ == '__main__':
    main()
