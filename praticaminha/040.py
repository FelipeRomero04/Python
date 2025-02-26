from os import system

system('cls')

print('=' * 30)
print('LOJAS SUPER BARATÃO')
print('=' * 30)

total = mil = 0
carrinho = []

while True:
    produto = str(input('Nome do Produto: '))

    while True:
        try:
            preco = float(input('Preço: R$'))
            if preco > 0:
                break
            print('Valor incorreto. Tente novamente!')
        except ValueError:
            print('Valor inexistente. Tente novamente!')
    
    total += preco

    if preco > 1000:
        mil += 1

    carrinho.append({
        'produto': produto,
        'valor': preco
    })
        
    menor_preco = min(carrinho, key=lambda x: x['valor']) #usando key(critério) o valor do dicionario, para retornar o menor dicionario
    
    #le o dicionario(x) e retorna o valor dele

    while True:
        opcao = str(input('Quer continuar[S/N]: ')).upper().strip()
        if opcao not in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            print('Escolha uma das opcões acima.')
        else:
            break
    if opcao in ('N', 'NAO', 'NÃO'):
        break

print(f'O total da compra foi de R${total}.')
print(f'Temos {mil} produto custando mais de R$1000,00.')
print(f'O produto mais barato foi {menor_preco['produto']} custando R${menor_preco['valor']}')
