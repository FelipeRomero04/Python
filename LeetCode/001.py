EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutos):
    '''Recebe o parâmetro 'minutos', que sera usada como meio de retornar, quantos ainda faltam para lasanha ficar pronta'''
    if minutos < EXPECTED_BAKE_TIME:
        return EXPECTED_BAKE_TIME - minutos
    raise ValueError('Sua Lasanha passou do ponto.')
    # return 'Sua lasanha passou do ponto!'

def preparation_time_in_minutes(number_of_layers):
    '''Calcula quantos minutos adicionais a lasanha terá que ficar no forno, de acordo com a quantidade de camadas/ cada camada +2 min'''
    return 2 * number_of_layers
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Calcula o tempo total de cozimento da lasanha''' 
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

print(EXPECTED_BAKE_TIME)
print(bake_time_remaining(30))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3, 20))

