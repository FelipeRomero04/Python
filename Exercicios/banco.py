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
    
    cedula = 10             #ARRUME UM JEITO DE SIMPLIFICAR TUDO! OBSERVE AS REPETIÇÕES NO CODIGO 

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



print(cont50, cont20, cont10, cont1)


#resetar sempre q a cedula muda e armazenar o valor