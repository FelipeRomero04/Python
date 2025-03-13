from time import sleep
from os import system

system('cls')

'''matriz = []

for l in range(3):
    temp = []
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        temp.append(n)
    matriz.append(temp)

for m in matriz:
    sleep(0.5)
    print(f'{m}')
'''
#Dois metodos feitos por mim

matriz = []
par = 0

for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        if n % 2 == 0:
            par += n
        matriz.append(n)

print('=-' * 30)

cont = 0
somcol = 0
maior = matriz[0]

for l in range(3): 
    for c in range(3):
        print(f'[ {matriz[cont]} ]',end= '')
        if c == 2:
            somcol += matriz[cont]
        if l == 1 and matriz[cont] > maior:
            maior = matriz[cont]
        cont += 1
    print()
# maior = matriz[cont] if l == 1 and matriz[cont] > maior else maior / OPERADOR TERNARIO 
print('=-' * 30)

print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {somcol}')
print(f'O maior valor da segunda linha é {maior}')


'''ANOTE SOBRE OPERADOR TERNARIO, E FAÇA O MESMO COM A MATRIZ ACIMA'''









