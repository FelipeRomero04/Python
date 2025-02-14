from os import system
from random import randint

# Limpa o terminal antes de iniciar o jogo
system('cls' if system == 'nt' else 'clear')

print('=-' * 30)
print(' ' * 15, 'VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

v = 0  # Contador de vitórias

while True:
    # Validação para garantir que o jogador insira um número válido
    while True:
        try:
            jogador = int(input('Diga um valor (0 a 10): '))
            if 0 <= jogador <= 10:
                break               #Se o numero for valido, o programa break esse loop...
            print('Número inválido! Escolha um valor entre 0 e 10.')
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')

    # Validação da escolha "P" ou "I"
    while True:
        opcao = input('Par ou Ímpar [P/I]? ').strip().upper()
        if opcao in ('P', 'I'):
            break                   # E vai para esse
        print('Opção inválida! Escolha P para Par ou I para Ímpar.')

    computador = randint(0, 10)
    total = jogador + computador
    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR'

    print('--' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, deu {resultado}!')
    
    # Verificação de vitória
    if (total % 2 == 0 and opcao == 'P') or (total % 2 == 1 and opcao == 'I'):
        print('Você VENCEU! 🎉')
        v += 1
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU! 😢')
        break

print('--' * 30)
print(f'GAME OVER! Você venceu {v} {"vez" if v == 1 else "vezes"}.')
