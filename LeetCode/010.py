"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    
    for item in items:
        if item in inventory:
            inventory[item] += 1
            continue
        inventory[item] = 1
    return inventory
        
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory and inventory[item] > 0 :
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    # for value in inventory:
    #     if value == item:
    #         inventory.pop(item)
    #         return inventory
    # return inventory

    if item in inventory:
        inventory.pop(item)
    return inventory

print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

#    inventory.pop(item, None)
#     return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # lista = []

    # for key ,value in inventory.items():
    #     if value > 0:
    #         lista.append((key,value))
    # return lista
    

    return [(key, value) for key, value in inventory.items() if value > 0]


'''
TASK 3

Implemente a decrement_items(<inventory dict>, <items list>)função que recebe uma contagem listde itens. Sua função deve remover 1um item da contagem para cada vez que esse item aparecer em list:

>>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
As contagens de itens no inventário não devem cair abaixo de 0. Se o número de vezes que um item aparece na entrada listexceder a contagem disponível, a quantidade listada para esse item deve permanecer em 0. Solicitações adicionais para remoção de contagens devem ser ignoradas quando a contagem cair para zero.

>>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}


TASK 4 

Implemente a remove_item(<inventory dict>, <item>)função que remove um item e sua contagem inteiramente de um inventário:

>>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
{"wood":1, "diamond":2}
Se o item não for encontrado no inventário, a função deverá retornar o inventário original inalterado.

>>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
{"coal":2, "wood":1, "diamond":2}

TASK 5

Implemente a list_inventory(<inventory dict>)função que realiza um inventário e retorna uma lista de (item, quantity)tuplas. A lista deve incluir apenas os itens disponíveis ( com quantidade maior que zero ):

>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
'''