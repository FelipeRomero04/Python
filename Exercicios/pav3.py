from os import system

system('cls')

print('=-'*20)
print(' '*11,'Gerador de PA')
print('-='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
mais = 10

while cont < mais:
    print(f'{termo} => ',end='')
    termo += razao
    cont += 1
    if cont == mais:
        print('PAUSA')
        mais += int(input('Quantos termos quer a mais? '))

print(f'Progressão finalizada com {cont} termos mostrados.')

    
   

    



