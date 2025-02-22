from os import system

system('cls')

print('--' * 20)
print(' ' * 10, 'LOJAS SUPER BARATÃO')
print('--' * 20)

total = mil = 0
barato = ''
carrinho = []

while True:

    produto = str(input('Nome do produto: '))
    
    while True:
        try:
            preco = float(input('Preço R$ '))
            if preco > 0:
                break   
            print('Valor incorreto.')
        except ValueError:
            print('Erro. Tente Novamente!')

    total += preco

    if preco > 1000:
        mil += 1

    carrinho.append({ #Gera um dicionario a cada repeticao
        'produto': produto,
        'valor': preco
    })
        
    menor_valor = min(carrinho, key= lambda x: x['valor'])
    #Procura pelo menor ['valor'] percorrendo todos dicionarios

    while True:
        opcao = str(input('Quer continuar[S/N]? ')).strip().upper()
        if opcao in ('S', 'SIM', 'N','NAO','NÃO'):
            break
    if opcao in ('N','NAO', 'NÃO'):
        break

print(f'O total da compra foi de R${total}')
print(f'Temos {mil} {'produto' if mil == 1 else 'produtos'} custando mais de R$1000.00')
print(f'O produto mais barato foi {menor_valor['produto']} custando R${menor_valor['valor']}')

























#IDEIA: CRIAR UM PROGRAMA EM QUE VOCE CRIA UM DICIONARIO DE PRODUTOS COM VALORES DEFINIDOS, E SELECIONA QUAL QUISER, E NO FIM PERGUNTA QUAL TIPO DEM PAGAMENTO, MOSTRANDO O VALOR FINAL DA COMPRA.