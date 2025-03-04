n1 = float(input('Primero valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
lista = [n1 , n2 , n3]

if max(lista) > min(lista): 
    print(f'O maior número digitado foi {max(lista)}')
    print(f'O menor número digitado foi {min(lista)}')

if n1 == n2 == n3:
    print('Todos número digitados são iguais!')


#Método GUANABARA


'''n1 = float(input('Primero valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
menor = n1

#verificando o menor

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

if n1 == n2 == n3:
    print('São todos iguais')
else:
    print(f'O maior é {maior}')
    print(f'O menor é {menor}')'''


#METODO POLUIDO,SEM EFICIENCIA E PRATICIDADE

'''n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

if n1 > n2 > n3:
    print(f'O maior valor digitado foi {n1}')
    print(f'O menor valor digitado foi {n3}')

if n1 > n3 > n2:
    print(f'O maior número é {n1}')
    print(f'O menor número é {n2}')

if n2 > n1 > n3:
    print(f'O maior numero é {n2}')
    print(f'O menor numero é {n3}')

if n2 > n3 > n1:
    print(f'O maior numero é {n2}')
    print(f'O menor número é {n1}')   

if n3 > n1 > n2:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n2}')

if n3 > n2 > n1:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n1}')

if n1 == n2 == n3:
    print('São todos iguais')'''



