from random import choice 

print(''' Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

jogador = int(input('Qual é a sua jogada?'))
computador = choice(['Pedra', 'Papel', 'Tesoura'])

print(computador)
