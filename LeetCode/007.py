from math import floor

def get_rounds(number):
    return list(i + number for i in range(3))



def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2

def approx_average_is_average(hand):

    # O first_last(media da primeira e ultima carta) ou a carta no meio do baralho(index_mediana) tem q ser == media de hand

    media = sum(hand) / len(hand)
    first_last = (hand[0] + hand[-1]) // 2
    mediana = hand[len(hand) // 2] 

    return media in (first_last, mediana)

    

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    num_impar = []

    for i in range(1, len(hand), 2):
        num_impar.append(hand[i]) 
        
    media_impar = sum(num_impar) / len(num_impar)

    num_par = []

    for i in range(0, len(hand), 2):
        num_par.append(hand[i])

    media_par = sum(num_par) / len(num_par)

    return media_impar == media_par




#Copiar sobre desempacotamento
#Copiar a diferença de '**' e '*' na passagem de parâmetros
#Voltar ao exercício anterior e ler o código da comunidade
def maybe_double_last(hand):
    
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand

print(maybe_double_last([5, 9, 10]))

    
    