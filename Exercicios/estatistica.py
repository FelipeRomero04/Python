from os import system

system('cls')

print('--' * 20)
print(' ' * 10, 'LOJAS SUPER BARATÃO')
print('--' * 20)

total = milhar = menor_valor = 0
barato = ''
carrinho = []


while True:

    produto = str(input('Nome do produto: '))
    #fazer um dicionario de produtos
    
    while True:
        try:
            preco = float(input('Preço: '))
            if preco > 0:

                break   
            print('Valor incorreto.')
        except ValueError:
            print('Erro. Tente Novamente!')

    carrinho.append(preco)
    menor_valor = carrinho[0]
    
    if preco < menor_valor:
        menor_valor = preco
        



    total += preco

    
    
    


    while True:
        opcao = str(input('Quer continuar[S/N]? ')).strip().upper()
        if opcao in ('S', 'SIM', 'N','NAO','NÃO'):
            break
    if opcao in ('N','NAO', 'NÃO'):
        break

print(barato)


























#IDEIA: CRIAR UM PROGRAMA EM QUE VOCE CRIA UM DICIONARIO DE PRODUTOS COM VALORES DEFINIDOS, E SELECIONA QUAL QUISER, E NO FIM PERGUNTA QUAL TIPO DEM PAGAMENTO, MOSTRANDO O VALOR FINAL DA COMPRA.