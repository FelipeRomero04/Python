from os import system
system('cls')

num = int(input('Digite um número [999 p/parar]: '))
s = 0
cont = 0

while num != 999:
    s += num
    num = int(input('Digite um número [999 p/parar]: '))
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é de {s}.')


    