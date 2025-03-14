from time import sleep
from random import sample, randint
'''
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)

palp = int(input('Número de palpites: '))
sort = []
print(f'-=-=-= SORTEANDO {palp} JOGOS -=-=-=')

for p in range(palp):
    while len(sort) <= palp: #Garantir que não haja repetições
        n = randint(1, 61)
        if n in sort:
            continue #se n ja tiver em lista, pula pra prox iteração
        sort.append(n)
    sleep(0.9)
    print(f'Jogo {len(sort)}: {sorted(sort)}')
    sort.clear()

print('-=' * 5, '< BOA SORTE >', '-='*5)
'''
#Forma simplificada:

print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)

palp = int(input('Número de palpites: '))
sort = []

print(f'\n-=-=-= SORTEANDO {palp} JOGOS -=-=-=')

for i in range(1, palp + 1):
    sort = sample(range(61), 6)
    print(f'Jogo {i}: {sorted(sort)}')
    sleep(0.9)
    


