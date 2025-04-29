# Função auxiliar
def converter_para_reais(valor_em_dolar, taxa_de_cambio):
    return valor_em_dolar * taxa_de_cambio

# Função principal
def valor_final_em_reais(dolar, taxa):
    reais = converter_para_reais(dolar, taxa)
    return reais


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
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
    ace = False

    if card_one == 'A':
        ace = True
    
    elif card_two == 'A':
        ace = True
    

    return True if ace and card_one in ('10', 'J', 'Q', 'K') or card_two in ('10','J', 'Q', 'K') else False

print(is_blackjack('Q', 'K'))









# card_one = 10 if card_one in ('J', 'Q', 'K') else card_one
    # card_two =  if card_one in ('J', 'Q', 'K') else card_two
    # if card_one in ('J', 'Q', 'K'):
        
    #     card_one = (card_one, 10)
    # else:
        
    # return card_one
    
    # if card_one == 'A':
    #     card_one = 1
    # if card_two == 'A':
    #     card_two = 1        
    
    # return (card_one, card_two) if card_one != card_two else max(card_one, card_two)