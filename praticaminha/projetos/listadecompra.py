from os import system

system('cls')

carrinho = ()
total = 0

print('=-' * 20)
print(f'{'LOJAS LIPEE':^40}')
print('=-' * 20)

while True:
    produto = input('\nPesquisar por materiais: ')
    while True:
        try:
            valor = float(input('Valor: R$'))
            if valor > 0:
                break
            print('Valor Inválido!')
        except ValueError:
            print('Entrada Incorreta.')
    
    carrinho += (produto, valor,)
    total += valor

    while True:
        opcao = input('Mais alguma coisa[S/N]? ')
        if opcao.upper() in ('S','SIM', 'N','NAO', 'NÃO'):
            break 
        print('Valor inserido não corresponde.')
    if opcao.upper() in ('N', 'NAO', 'NÃO'):
        break

print('=-' * 20)

for i in range(0, len(carrinho), 2):
   print(f'{carrinho[i]:.<25} R${carrinho[i + 1]:.2f}')
print('=-' * 20)
print(f'Total das compras R${total:.2f}')