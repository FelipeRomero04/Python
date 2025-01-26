''''numeros = str(input('Digite uma lista de números, divididos por vírgula: '))
lista = list(map(int, numeros.split(',')))
maior_numero = int()
menor_numero = int()

for x in lista:
    if x == max(lista):
        maior_numero = x

    elif x == min(lista):
        menor_numero = x

media = (maior_numero + menor_numero) / 2

print(f'O maior numero é {maior_numero}, e o menor é {menor_numero}, e sua media é {media}')'''


numeros = str(input('Faça um lista, dividida por vírgula: '))
lista = list(map(int, numeros.split(',')))
maior_lista = lista[0]
menor_lista = lista[0]


for x in lista:
    if x > maior_lista:  
        maior_lista = x
    if x < menor_lista:
        menor_lista = x
''' Em uma lista de  [ 1, 2, 3] Se x > maior_lista(que é 1), x sendo 1 n ira mudar nada! No proximo loop, x sera 2, sendo maior que maior_lista(que e 1), sendo assim, maior_lista assumirá o valor de 2, e entao no proximo loop, x == 3, que e maior que maior_lista(que é 2) e assim por diante, a depender da lista '''

media = sum(lista) / len(lista)

print(f'O maior é {maior_lista}, e o menor é {menor_lista}, média sera de {media}')



    


