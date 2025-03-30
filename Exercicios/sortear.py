from random import randint
from time import sleep

numeros = []

def sorteio():
    print('Sorteando os 5 valores: ',end='')
    for i in range(5):
        i = randint(1,10)
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
        numeros.append(i)
    print('PRONTO!')

def somarpar(lista):
    soma_par = sum(filter(lambda x: x % 2 == 0, lista))
    # soma = 0
    # for n in list:
    #     if n % 2 == 0:
    #         soma += n
    print(f'Somando os valores pares da lista {numeros}, temos {soma_par}.')

sorteio()
somarpar(numeros)
