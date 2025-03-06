lista = []

for v in range(5 + 1):
    n = int(input('Digite um valor: '))
    
    if v == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao fim da lista...')
    if lista[0] < n:
        lista.insert(v, n)
        print('Adicionado posição zero')
        
            


   

    
    
    
    
    
    
    
    
    
    
    
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