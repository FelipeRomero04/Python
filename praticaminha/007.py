lista = str(input('digite três números: '))
converter = list(map(int, lista.split(',')))

if min(converter) == converter[0] :    #em ordem crescente o minimo sempre vem primeiro
    print('Esta em ordem crescescente') 
if max(converter) == converter[0]: #em ordem descrescente o máximo sempre vem primeiro
    print('Esta em ordem descrescente')
if max(converter) != converter[0] and min(converter) != converter[0]: 
    print('Esta Desordenado')
#Negando todas condiçoes acima

''' 23234, 2321, 12424  DANDO ERRO RESOLVA'''





# 1, 2, 3
# 3, 2, 1
# 3, 5, 1


