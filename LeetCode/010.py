
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    value = 1
    for i in items:

        if i in inventory:
            inventory[i] += value
            continue
        inventory[i] = value
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
   

    pass

print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    
    return {item: inventory[item] - 1 for item in items if item in inventory and inventory[item] > 0 }


# Valores repetidos não são decrementados, pois o dict comprehession retorna o item como chave, ja que apenas uma chave e permitida, as proximas ocorrencias serão ignoradas



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    for i in inventory:
        if i == item:
            inventory.pop(item)
            return inventory
    return 


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    for k, v in inventory.values():
        print(k,v)
    


print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))