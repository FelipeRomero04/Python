from random import choice 
from time import sleep

print(''' Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
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
    pedra = 1
    print(f'Jogador jogou {pedra}')
elif jogador == 2:
    papel = 2
    print(f'Jogador jogou {papel}')
elif jogador == 3:
    tesoura = 3
    print(f'Jogador jogou {tesoura}')
else:
    print('Opção inválida. Tente novamente!')
    exit()
print('=-'*20)

