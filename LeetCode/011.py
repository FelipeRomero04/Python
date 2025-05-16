def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for k, v in current_cart.items():
        



    # return {current_cart.setdefault(items_to_add[i], 1) if items_to_add[i] not in current_cart else k: v + items_to_add.count(k) for i, (k, v) in enumerate(current_cart.items())}

    

    return {k: v + items_to_add.count(k) if items_to_add[i] in current_cart else current_cart.setdefault(items_to_add[i], 1) for i, (k ,v) in enumerate(current_cart.items())} #Ver no chatgpt depois de fazer da forma normal se e possivel
    # return {k: v + items_to_add.count(k) for k, v in current_cart.items()}

print(add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
              ('Apple', 'Apple', 'Orange', 'Apple', 'Banana', 'Pessego')))


    