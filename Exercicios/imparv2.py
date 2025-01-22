'''s = 0

for c in range(3, 501, 3):
    if c % 2 != 0:  # Filtrando tds os numero multiplos de 3 para somente multiplos e impares
        s += c      # Fazendo a somatoria de todos os números
    c = (c / 3) / 2  
print(f'A soma de todos os {c:.0f} valores solicitados sao {s}')'''

#-----------------------Minha tentativa(acima)--------------------------------------

# CODIGO MAIS LÓGICO
s = 0 
cont = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(cont, s)

#----------------------CODIGO MAIS LIMPO(ABAIXO)--------------------------------------

'''s = 0
cont = 0
for c in range (3,501,6):
    s += c
    cont += 1  # Toda repetiçao que o programa fizer, o cont irá contabilizar
print (cont, s) '''

        





 





    

              
    