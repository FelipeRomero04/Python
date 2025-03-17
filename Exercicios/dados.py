from random import randint
from time import sleep
from os import system
from operator import itemgetter

system('cls')

jogo = {}

for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1,6)

print('== VALORES SORTEADOS ==')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

print('=-' * 30)

ranking = dict(sorted(jogo.items(), key= lambda item: item[1], reverse=True))
#lambda diz pro sorted como deve ordenar, baseado no jogo.items(), pegando o valor [1]

# ranking = dict(sorted(jogo.items(), key= itemgetter(1), reverse=True))

print(f'{'<<RANKING >>':^33}')


for posicao, (k, v) in enumerate(ranking.items(), start=1):
    print(f' {posicao}º Lugar: {k} com {v} pontos.')
    sleep(1)