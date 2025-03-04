lista = (
   'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
   'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
   'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

'''print('--' * 20)
print(f'{'LISTAGEM DE PREÇOS':^38}')
print('--' * 20)

for p, v in zip(range(0,len(lista), 2), range(1,len(lista), 2)):
   print(f'{lista[p]:.<25} R${lista[v]:.2f}')
print('--' * 20)'''

#SEMPRE QUE TIVER UMA COLECÃO DE ELEMENTOS COM VALORES INTERCALADOS, USE A ESTRATEIA DO PAR OU IMPAR / TIPAGEM / RANGE DE 2 EM 2.

#Ler e entender o codigo do guanabara e o dos comentarios. reproduza-os tambem

#Implementar a opcao de voce mesmo colar mais itens

#Metodo guanabara

for p in range(len(lista)):
   if p % 2 == 0:
      print({lista[p]})
   else:
      print(lista[p])
