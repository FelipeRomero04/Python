from random import randint
from time import sleep

jogadores = [{'nome': 'jogador1'}, {'nome': 'Jogador2'}, {'nome': 'Jogador3'}, {'nome': 'Jogador4'}]


for j in jogadores:
    j['valor'] = randint(1, 7)
    print(f'O {j['nome']} tirou {j['valor']}')
        
for j in jogadores:
    for v in j.values():
        print(v[0])
'''pontos = []  

print('Ranking')
for j in jogadores:
    j.pop('nome')
    for v in j.values():
        pontos.append(v)

for p in range(1, 4):
    print(f'{p}ª ')'''







#pra cada dicionario vou adicionar um valor randint

#For pra percorrer cada dicionario

#Primeira parte key and values(aninhado com de cima)

#Para organizar o dic provavelmente vou ter q usar for values

    