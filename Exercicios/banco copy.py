from os import system

system('cls')

saque = float(input('Valor do saque: '))

cedula = [50, 20, 10, 1]
indice = 0   #Variavel para ser usada com indice
cont = [0, 0, 0, 0]

while saque != 0:
    if saque >= cedula[0]:
        saque -= cedula[0]
        cont[indice] += 1
            
    else:
        cedula.remove(cedula[0]) 
        indice += 1 #Atualizando o indice para andar pra frente, conforme as cedula mudam
           
for c, qnts in cedula, cont:
    
    print(f'Total de {qnts} cédulas de R${c}')

#VAI NO CHATGPT E LEIA A EXPLICAÇÂO NO ULTIMO CHAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    #print(f'Total de {cont[0]} cedula de R$50')

  






            
            

    












        





'''
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