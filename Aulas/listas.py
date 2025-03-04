'''lista = [3, 6, 2, 1, 5]

lista[1] = 5
#lista.sort(reverse=True)
lista.insert(2, 8)

lista.pop(2) #sem parâmetro, o ultimo item seria eliminado
print(lista)'''


#criando conexão entre listas 

# criando uma lista nova que receba a anterior, qlqr mudança na nova lista tbm mudara a lista original(conexão)

lista = [3, 6, 2, 1, 5]
lista_2 = lista #Se precisar so criar uma copia (lista[:])'lista_2 recebe todos os itens de lista'
lista_2.insert(1,7)



print(lista_2, lista)

# Pode conseguir o índice usando, range no for, enumerate ou index 

if 6 in lista:
    print(f'O número 4 esta na posição {lista.index(6)}')

for i, v in enumerate(lista):
    print(f'{i} - {v}...')