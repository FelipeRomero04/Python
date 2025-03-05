lista = []



for v in range(5):
    n = int(input('Digite um valor: '))
    lista.append(n)
    maior = menor = lista[0]
    if maior > n:
        maior = n
    if menor < n:
        menor = n

    for i in lista:
        if maior >= n or v == 0:
            print(f'Adicionado ao final da lista...')
        elif maior < n > menor:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        elif n <= menor:
            lista.insert(0, n)
            print(f'Adicionado na posição 0 da lista...')
        
        