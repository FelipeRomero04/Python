from os import system

system('cls')

saque = float(input('Valor do saque: '))
cedula = 200
cont200 = cont100 = cont50 = cont20 = cont10 = cont5 = cont2 = cont1 = 0


while True:
    if cedula < saque:
        saque -= cedula
        cont200 += 1
    elif cedula < saque:
        cedula = 100
        saque -= cedula
        cont100 += 1    
    elif cedula > saque:
        cedula = 50
        saque -= cedula
        cont50 += 1
    elif cedula > saque:
        cedula = 20
        saque -= cedula
        cont20 += 1
    elif cedula > saque:
        cedula = 10
        saque -= cedula
        cont10 += 1
    elif cedula > saque:
        cedula = 5
        saque -= cedula
        cont5 += 1
    elif cedula > saque:
        cedula = 2
        saque -= cedula
        cont2 += 1
    elif cedula > saque:
        cedula = 1
        saque -= cedula
        cont1 += 1
    if saque == 0:
        break

print(cont200)



#resetar sempre q a cedula muda e armazenar o valor