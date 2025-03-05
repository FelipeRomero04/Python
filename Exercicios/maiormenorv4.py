lista = []


#FORMA COM GERADOR
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))
print('-=' * 25)

maior = max(lista)
menor = min(lista)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} na posição: {' e '.join(str(pos) for pos, v in enumerate(lista) if v == maior)}')
print(f'O menor valor digitado foi {menor} na posição: {' e '.join(str(pos) for pos, v in enumerate(lista) if v == menor)}')

#Para melhor Otimização, é necessario declarar o max/min(lista) fora dos loops. caso contrario, cada loop a lista e percorrida novamente para encontrar o indice do menor e do maior(loops desnecessarios)

'''for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))
print('=-' * 20)
print(f'Os valores digitados foram: {lista}')

maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {maior} na posição: ',end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}... ',end='')
    
print(f'\nO menor valor digitado foi {menor} na posição: ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}... ',end='')'''





    
    