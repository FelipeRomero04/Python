from os import system

system('cls')

saque = float(input('Valor do saque: '))
cedula = 50
cont50 = cont20 = cont10 = cont1 = 0

while True:
    while True:
        if saque >= cedula:
            saque -= cedula
            cont50 += 1
        else: 
            break

    cedula = 20

    while True:
        if saque >= cedula:
            saque -= cedula
            cont20 += 1
        else:
             break
    
    cedula = 10             

    while True:
        if saque >= cedula:
            saque -= cedula
            cont10 += 1
        else:
            break
    
    cedula = 1

    while True:
        if saque >= cedula:
            saque -= cedula
            cont1 += 1
        else:
            break

    
    if saque == 0:
        break

print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont1} cédulas de R$1')



    
    




# Cada vez que o saque nao puder ser reduzido pela maior nota, a cedula atualiza para uma menor. Se

    
'''
if cedula < saque:
    cedula = 20
elif cedula < saque:
    cedula = 10


'''



'''while saque != 0:
    if saque >= cedula:
        saque -= cedula
        cont50 += 1
    elif saque < cedula:
        cedula = 20
        saque -= cedula
        cont20 += 1
    elif saque < cedula:
        cedula = 10
        saque -= cedula
        cont10 += 1
    else:
        cedula = 1
        saque -= cedula
        cont1 += 1'''







#resetar sempre q a cedula muda e armazenar o valor