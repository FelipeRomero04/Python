s = 0
cont = 0

for n in range(1, 7):
    numb = int(input(f'Digite o {n}º número: '))
    if numb % 2 == 0:
        s += numb
        cont += 1

    '''elif numb % 2 != 0:   # ESSA PARTE E REDUNDANTE E DESNECESSARIA
        s += 0'''

print(f'Você informou {cont} {'número' if cont == 1 else 'números'} {'par' if cont == 1 else 'pares'} e a soma foi de {s}')

