from random import randint
from time import sleep

computador = randint(1, 3) 
opcao = ('','Pedra', 'Papel', 'Tesoura') 

playervic = 'JOGADOR VENCEU'
pcvic = 'JOGADOR VENCEU'

print('''SUAS OPÇÕES:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

jogador = int(input('Qual a sua jogada? '))

print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!!')

print('=-' * 11)
print(f'Computador jogou {opcao[computador]}') #computador gera um numero, que fica na posição da variavel opcao
print(f'Jogador jogou {opcao[jogador]}') # jogador escolhe um número, que fica na posição da variavel opcao
print('=-' * 11)

if jogador == computador:
    print('EMPATOU')

elif computador == 1:   #Pedra
    if jogador == 2:
        print('JOGADOR VENCEU!')
    elif jogador == 3:
        print('COMPUTADOR VENCEU!')

elif computador == 2: #Papel
    if jogador == 3:
        print('JOGADOR VENCEU!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU!')

elif computador == 3: #Tesoura
    if jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
       
else:
    print('JOGADA INVÁLIDA')
    exit()



