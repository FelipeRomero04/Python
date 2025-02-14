from os import system 
from random import randint
system('cls')

print('=-' * 30)
print(' ' * 15, 'VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

v = 0

while True:
    while True:
        try:
            jogador = int(input('Diga um valor: '))
            if 0 <= jogador <= 10:
                break
            print(f'Você não tem {jogador} dedos nas mãos. Jogue novamente!')
        except ValueError:
                print('Entrada Inválida! Digite apenas números inteiros.')
    while True:
        opcao = str(input('Par ou Ímpar[P/I]? ')).strip().upper()
        if opcao in ('PAR', 'IMPAR', 'P', 'I'): #Ou while opcao not in 'PpIi'
             break #Mesmo str aceitando números, o loop só irá parar se a condicao for valida
        print('Opcão ínvalida! Tente Novamente')
    
    computador = randint(1,10)
    total = jogador + computador
    
    print('-='*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}! Deu {'PAR' if total % 2 == 0 else 'IMPAR'}')
    print('-='*30)
    
    if total % 2 == 0 and opcao in ('PAR', 'P') or total % 2 == 1 and opcao in ('IMPAR', 'I'): 
        print('Você VENCEU!')
        v += 1
        print('Vamos jogar novamente...')
        print('-='*30)
    else:
        print('Você PERDEU!')
        print('-='*30)
        break

print(f'GAME OVER! Você venceu {v} {'vez' if v == 1 else 'vezes'}.')



#Codigo acima esta otimizado e mais limpo(com ajuda chtgpt), abaixo original feito por mim

'''from os import system 
from random import randint
system('cls')

print('=-' * 30)
print(' ' * 15, 'VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    while jogador > 10:
        print(f'Você não tem {jogador} dedos nas mãos. Jogue novamente!')
        jogador = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar[P/I]? ')).strip()[0] #pode declarar uma string vazia, inves de repetir 
    while not opcao in 'PpIi': #Ou while opcao not in 'PpIi'
        print('Opcão ínvalida! Tente Novamente')
        opcao = str(input('Par ou Ímpar[P/I]? ')).strip()[0] #comando repetido 
    computador = randint(0,10)
    total = jogador + computador
    print('-='*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}! Deu {'PAR' if total % 2 == 0 else 'IMPAR'}')
    print('-='*30)
    if total % 2 == 0 and opcao in 'Pp' or total % 2 == 1 and opcao in 'Ii': 
        print('Você VENCEU!')
        v += 1
        print('Vamos jogar novamente...')
        print('-='*30)
    else:
        print('Você PERDEU!')
        print('-='*30)
        break

print(f'GAME OVER! Você venceu {v} {'vez' if v == 1 else 'vezes'}.')'''





