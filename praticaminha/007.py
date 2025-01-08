lista = str(input('digite três números: '))
converter = list(map(int, lista.split(',')))

if converter[0] < converter[1] < converter[2]:    
    print('Esta em ordem crescescente') 
elif converter[0] > converter[1] > converter[2] : 
    print('Esta em ordem descrescente')
    #elif é avaliado apenas se as condições anteriores (if ou outro elif) forem falsas.
else:
    print('Esta desordenado')
#Negando todas condiçoes acima









