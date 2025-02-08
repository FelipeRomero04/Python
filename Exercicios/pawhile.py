from os import system

system('cls')

print('=-'*20)
print(' '*11,'Gerador de PA')
print('-='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0

while cont < 10:
    print(f'{termo} => ',end='')
    termo += razao
    cont += 1
print('FIM')
    

