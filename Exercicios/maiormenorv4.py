lista = []

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))
print(f'Você digitou os valores: {lista}')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}...', end='  ')
    

'''lista = [4,2,6,6]

print(lista.index(max(lista)))'''

    
    