from player import *
import random as r


################################
# Difficulty/Upgrade Functions #
################################

def level_up(player, health_max):
    while True:
        lv_choice = input("\nWould you like to:\n 1. Increase max health \n 2. Increase Healing Factor"
                          "\n 3. increase your damage\n 4. Leave \n")
        if lv_choice == "1":
            health_max += r.randint(1, 20)
            player.health = health_max
            return player, health_max
        elif lv_choice == "2":
            player.heal += (5, 5)
            player.health = health_max
            return player, health_max
        elif lv_choice == "3":
            player.attack_1 += r.randint(1, 5)
            player.attack_2 += (5, 5)
            player.attack_3 += (5, 5)
            player.health = health_max
            return player, health_max
        elif lv_choice == "4":
            return
        else:
            print("Please enter in a valid number")
            continue


def difficulty(ai, health_max, level):
    if level == 1:
        return ai
    else:
        ai.health = health_max + 15 * round(0.5 * level + 0.5)
        ai.attack_1 += 5 * round(0.5 * level + 0.5)
        ai.attack_2 += (5 * round(0.5 * level + 0.5), 5 * round(0.5 * level + 0.5))
        ai.attack_3 += (5 * round(0.5 * level + 0.5), 5 * round(0.5 * level + 0.5))
        ai.heal += (5 * round(0.5 * level + 0.5), 5 * round(0.5 * level + 0.5))
        return ai


def randomize_ai(ai):
    ai.health += r.randint(-20, 20) // 2
    ai.attack_1 += r.randint(-5, 3)
    ai.attack_2 += (r.randint(-5, 3), r.randint(-5, 3))
    ai.attack_3 += (r.randint(-5, 3), r.randint(-5, 3))
    ai.heal += (r.randint(-5, 3), r.randint(-5, 3))
    return ai