
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

print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal","coal", "iron", "iron"]))


    # colection = create_inventory(items)

    # if not inventory in colection:
    #     colection.update(items)
    #     return colection
    # if not inventory:
    #     return colection
    # items.append(list(inventory)[0])

    # return create_inventory(items)

    # if inventory:
    #     items.append(list(inventory)[0])
    
    # return create_inventory(items)

    

