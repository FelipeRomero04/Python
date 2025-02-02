from random import randint

print('------ Bem Vindo ao jogo da adivinhação! ------')
print('Tente acertar o numero que o computador ta pensando')

computador = randint(1, 50)
tentativas = 0

while True:
    usuario = int(input(f'{tentativas + 1}ª Tentativa:\nDigite seu palpite: '))
    
    if usuario == computador:
        print(f'Você acertou! Também pensei no número {computador}!')
        print(f'Você teve {tentativas} {'tentativa' if tentativas <= 1 else 'tentativas'} {'errada' if tentativas <= 1 else 'erradas'}.')
        break
    elif computador <  usuario:
        print('O numero que eu pensei É MENOR!')
        tentativas += 1
    else:
        print('O número que eu pensei É MAIOR')
        tentativas += 1
    
    print('--------------------//---------------------')

