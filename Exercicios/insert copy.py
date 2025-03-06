from os import system

system('cls')

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




    
        
            


#se nao der certo tente criar um for aninhado com append(input) como for externo, depois percorrendo a lista printando as msg corretas

    
    
  
    
    
    
    
    
    
    
    
'''for i in lista:
        if maior >= n or v == 0:
            print(f'Adicionado ao final da lista...')
        elif maior < n > menor:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        elif n <= menor:
            lista.insert(0, n)
            print(f'Adicionado na posição 0 da lista...')'''
        
'''
1. Usar append para colocar o item no final da lista

2. Usar insert para colocar na posição 0 ou 1, para que as lista se ordene sozinha
'''      