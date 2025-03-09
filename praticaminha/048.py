lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    if not lista or n >= lista[-1]:
        lista.append(n)
        print('valor adicionado na ultima posição...')
        continue

    for pos, v in enumerate(lista):
        if n <= lista[pos]:
            lista.insert(pos, n)
            print(f'Valor adicionado na posição {pos}')  
            break

print(f'Os valores digitados foram {lista}')