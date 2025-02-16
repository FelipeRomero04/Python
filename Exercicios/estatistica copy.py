from os import system

system('cls')

print('--' * 20)
print(' ' * 10, 'LOJAS SUPER BARATÃO')
print('--' * 20)

total = milhar = 0
barato = ''

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

    total += preco

   
        

    if preco > 1000:
        milhar += 1

    while True:
        opcao = str(input('Quer continuar[S/N]? ')).strip().upper()
        if opcao in ('S', 'SIM', 'N','NAO','NÃO'):
            break
    if opcao in ('N','NAO', 'NÃO'):
        break




























#IDEIA: CRIAR UM PROGRAMA EM QUE VOCE CRIA UM DICIONARIO DE PRODUTOS COM VALORES DEFINIDOS, E SELECIONA QUAL QUISER, E NO FIM PERGUNTA QUAL TIPO DEM PAGAMENTO, MOSTRANDO O VALOR FINAL DA COMPRA.