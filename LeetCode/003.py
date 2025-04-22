'''Métodos para conversão de moedas'''

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)

    
def get_number_of_bills(amount, denomination):
    return amount // denomination
    

def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    

def exchangeable_value(budget, exchange_rate, spread, denomination):

    tottaxa_cambio = exchange_rate * (1 + spread / 100)
    valor = budget / tottaxa_cambio

    valor_notas = (valor // denomination) * denomination
    
    return valor_notas