def value_of_card(card):
    
    try:
        card = int(card)
    except ValueError:
        if card in ('K', 'Q', 'J'):
            card = 10
        elif card == 'A':
            card = 1
    return card   


def higher_card(card_one, card_two):
   

    return (card_one, card_two) if value_of_card(card_one) == value_of_card(card_two) else card_one if value_of_card(card_one) > value_of_card(card_two) else card_two



def value_of_ace(card_one, card_two):
    if card_one == 'A':
        card_one = 11
        
    
    elif card_two == 'A':
        card_two = 11
        
    return 1 if value_of_card(card_one) + value_of_card(card_two) > 10 else 11

'''Os cards assumindo o valor de 11 na função não altera nada. O 11 sera passado com parametro para value_of_card, a função value_of_card retorna o valor do card como int. Como o 11 ja é um int ele sera apenas retornado novamente'''


def is_blackjack(card_one, card_two):
    
    return (
        (card_one == 'A' and card_two in ('10', 'J', 'Q', 'K')) or 
        (card_two == 'A' and card_one in ('10', 'J', 'Q', 'K'))
    )


def can_split_pairs(card_one, card_two):
    return True if value_of_card(card_one) == value_of_card(card_two) else False 


def can_double_down(card_one, card_two):
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11

