from os import system
from math import ceil

system('cls')

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

termo = int(input('Quantos termos você quer mostrar: '))
cont = 0
f1 = 0
f2 = 1

while cont < termo:
    print(f'{f1}, ',end='')

    #f1, f2 = f2, f1 + f2 Método encurtado pelo chatgpt(Estudar como funciona)    
    #OU 
    soma = f1 + f2
    f1 = f2 
    f2 = soma 
    
    cont += 1
print('FIM')


    




