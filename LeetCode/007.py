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
    mediana = len(hand) / 2
    media = sum(hand) / len(hand)
    return (hand[0] + hand[-1] / 2) or mediana == media

print(approx_average_is_average([1, 2, 3]))

#Copiar sobre desempacotamento
#Copiar a diferença de '**' e '*' na passagem de parâmetros
#Voltar ao exercício anterior e ler o código da comunidade