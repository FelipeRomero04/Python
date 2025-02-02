from random import randint

print('-----------Jogo da Adivinhação----------')
print('Acabei de pensar em um numero de 1 a 10! Consegue adivinhar?\n ')

computador = randint(1,10)

tentativas = 0

while True:
    usuario = int(input(f'{tentativas + 1}ª Tentativa:\nQual o seu palpite? '))

    if computador == usuario:
        print(f'Parabéns! Também pensei no número {computador}.')
        print(f'Você teve {tentativas} {'tentativa' if tentativas == 1 else 'tentativas'} {'errada' if tentativas == 1 else 'erradas'}.')
        break

    if computador > usuario:
        print('O número que eu pensei É MAIOR!')
        tentativas += 1
    else:
        print('O número que eu pensei É MENOR!')
        tentativas += 1
    print('----------------//-----------------')
