lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0  or n >= lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista... ')
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#Forma de fazer o while percorrer a lista.
#Com o pos sendo usado como indice, todos os números da lista são percorridos

'''MINHA LOGICA(ERRADO)

lista = []

for v in range(0, 5):
    n = int(input('Digite um valor: '))
    
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao fim da lista...')
        print(f'{lista} Problema 1')

    elif n > lista[0] and n < lista[v - 1]:
        lista.insert(1, n)  
        print(f'Adicionado a posição {lista.index(n)}')
        print(f'{lista} Problema 3')

    elif n < lista[0]:
        lista.insert(0, n)
        print(f'Adicionado posição {lista.index(n)}')
        print(f'{lista} Problema 2')

print(lista)

'''
        
            

