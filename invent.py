

inventory = ["crappy sword"]


def add_to_inventory(item):
    inventory.append(item)


def print_inventory():
    print(inventory)


def del_inventory(item):
    inventory.remove(item)


def del_all_inventory():
    for i in inventory:
        inventory.pop(i)
