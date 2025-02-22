from os import system

system('cls')

print('='*30)
print(f'{'Banco CEV':^30}')
print('='*30)

saque = float(input('Valor do saque: '))

cedula = [50, 20, 10, 1]
indice = 0   #Variavel para ser usada com indice(ESTRATÉGIA INTERESSANTE!!!!!! COPIAR)
cont = [0, 0, 0, 0]

while saque != 0:
    if saque >= cedula[0]:
        saque -= cedula[0]
        cont[indice] += 1
            
    else:
        cedula.remove(cedula[0]) 
        indice += 1 #Atualizando o indice para andar pra frente, conforme as cedula mudam

cedula = [50, 20, 10, 1]

for notas, c in zip(cedula, cont): #Para percorrer duas listas ao mesmo tempo zip()
    if c > 0:
        print(f'Total de {c} cédulas de R${notas}') 
print('==' * 20)
print('Volte Sempre! Ao banco CEV')
    





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

