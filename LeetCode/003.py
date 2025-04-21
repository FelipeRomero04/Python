def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)





def exchangeable_value(budget, exchange_rate, spread, denomination):

    tottaxa_cambio = exchange_rate + (spread / 100)
    valor = budget / tottaxa_cambio

    
    return valor

print(exchangeable_value(127.25, 1.20, 10, 20))