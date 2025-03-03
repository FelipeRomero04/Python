lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('--' * 20)
print(f'{'LISTAGEM DE PREÇOS':^38}')
print('--' * 20)

# print(f'''
# {lista[0]} R${lista[1]:.2f}
# {lista[2]} R${lista[3]:.2f}
# {lista[4]} R${lista[5]:.2f}
# {lista[6]} R${lista[7]:.2f}
#)
print(f'{(lista for p in range(0,len(lista), 2))}')
#for p in range(0,len(lista), 2):
   # print(lista[p])
#for v in range(1,len(lista) + 1, 2):
    #print(lista[v])
