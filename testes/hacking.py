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
    return card   

print(value_of_card('K'))

