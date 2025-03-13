from time import sleep
from os import system

system('cls')

matriz = []

for l in range(3):
    temp = []
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        temp.append(n)
    matriz.append(temp)

for m in matriz:
    sleep(0.5)
    print(f'{m}')

#Dois metodos feitos por mim

'''matriz = []

for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz.append(n)

print('=-' * 30)

cont = 0

for l in range(3):
    sleep(0.5)
    for c in range(3):
        print(f'[ {matriz[cont]} ]',end= '')
        cont += 1
    print()'''
    
   










