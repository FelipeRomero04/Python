from random import choice 
from time import sleep

playervic = 0
pcvic = 0

print(''' Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
if jogador > 3:
    print('Opção inválida. Tente novamente!')
    exit()

computador = choice(['Pedra', 'Papel', 'Tesoura'])

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('=-'*20)
print(f'Computador jogou {computador}')
if jogador == 1:
    jogador = 'Pedra'
    print(f'Jogador jogou {jogador}')
elif jogador == 2:
    jogador = 'Papel'
    print(f'Jogador jogou {jogador}')
elif jogador == 3:
    jogador = 'Tesoura'
    print(f'Jogador jogou {jogador}')
print('=-'*20)

if 'Papel' in computador and jogador == 'Pedra' or 'Pedra' in computador and jogador == 'Tesoura' or 'Tesoura' in computador and jogador == 'Papel':
    print('Computador venceu')
    pcvic += 1

elif jogador == computador:
    print('Empatou')
    pcvic += 0
    playervic += 0

else:
    print('O jogador venceu')
    playervic += 1





# OUTRO MÉTODO NA PASTA 'PRATICAMINHA'