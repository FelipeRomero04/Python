from os import system

system('cls')

saque = float(input('Valor do saque: '))
cedula = [50, 20, 10 , 1]
cont50 = cont20 = cont10 = cont1 = 0

while True:
    for c in cedula:
        while c == 50:
            if saque >= c:
                saque -= c
           


            
            

    












        





'''while True:
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
'''



    
    




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