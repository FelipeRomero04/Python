lista = []

for x in range(1,6):
    peso = float(input(f'Digite o peso da {x}ª pessoa: '))
    lista.append(peso) # ou lista += [peso]

maior = max(lista)
menor = min(lista)


print(f'O maior peso lido foi {maior}.')
print(f'O menor peso lido foi de {menor}.')
'''
lista = []

for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}ª pessoa: '))
    lista.append(peso)


maior = lista[0]
menor = lista[0]

for peso in lista:
#Para cada peso em lista:
    if maior > peso:
        maior = peso
    if menor < peso:
        menor = peso

print(f'O maior peso lido foi {maior}.')
print(f'O menor peso lido foi {menor}')
'''
'''
maior = 0
menor = 0

for x in range(1,6):
    peso = float(input(f'Digite o peso da {x}ª pessoa.'))
    if x == 1:  # Por ser um loop as variaveis mantem o valor do primeiro loop
        maior = peso  
        menor = peso  
    else:
        if maior > peso:
            maior = peso
        if menor < peso:
            menor = peso
'''