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
    
    
    create_inventory(items)

    return 

print(create_inventory({"coal":1}, ["wood", "iron", "coal", "wood"]))