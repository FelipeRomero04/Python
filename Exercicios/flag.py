from os import system

system('cls')

soma = cont = 0

while True:
    num = int(input('Digite um número[999 p/parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} valores é de {soma}')