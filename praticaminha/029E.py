'''lista = []

for x in range(1,6):
    peso = int(input('Peso: '))
    lista.append(peso)

maior = max(lista)
menor = min(lista)


print(maior, menor)'''

for x in range(1, 6):
    peso = int(input(f'Digite o peso da {x}ª pessoa: '))
    lista = []
    lista.append(peso)

    
maior = lista[0]
menor = lista[0]

for x in range(1,6):
    print(lista)
    


