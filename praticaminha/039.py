from os import system

system('cls')

termos = int(input('Quantos termos você quer mostrar? '))
cont = 0
f1 = soma = 0
f2 = 1


while cont < termos:
    
    print(f'{f1}{' ' if cont == termos - 1 else ' => '}', end='')
    soma = f1 + f2
    f1 = f2 
    f2 = soma  
    cont += 1

''''''
'''Seguindo a sequência e perceptivel que o valor de f1 sempre sera f2, entretanto, a soma não pode ocorrer antes de f1 receber o real valor de f2(que e numero seguinte), assim f2 será atualizado para o proximo e prosseguira a sequência, caso contrário, ocorreria uma sequência logica(0, 1, 2 ,4 , 8, 16...)'''

#0    1    1    2      5     8
#               f1   f2