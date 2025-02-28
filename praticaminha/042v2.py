from os import system

system('cls')

matriz = []

for l in range(3):
    lista = []
    for c in range(3):
        valor = int(input(f'Digite a {l + 1}ª coluna: '))
        lista.append(valor)
    matriz.append(lista)

for m in matriz:
    print(m)