print(f'{' Lojas Lipee ':=^40}')
compras = float(input('Valor das compras: R$'))

print('''FORMA DE PAGAMENTO:
[ 1 ] À Vista no dinheiro / cheque
[ 2 ] À Vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção: '))
desconto = compras - (compras * 10 / 100)

if opcao == 1:
    print(f'Pagando à vista, sua compra de R${compras:.2f}, vai custar R${desconto:.2f} com 10% de desconto!')
elif opcao == 2:
    desconto = compras - (compras * 5 / 100)
    print(f'Pagando no cartão, sua compra de R${compras:.2f}, vai custar R${desconto:.2f} com 5% de desconto!')
elif opcao == 3:
    print(f'Sua compra será parcelada 2x no cartão de R${compras / 2:.2f} SEM JUROS.')
elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    total_juros = compras + (compras * 20 / 100)
    print(f'Sua compra será parcelada em {parcela}x de R${compras / parcela:.2f} COM JUROS. ')
    print(f'Sua compra de R${compras:.2f}, terá o valor total de R${total_juros:.2f} com 20% de juros.')
else: 
    print('Opcão de pagamento INVÁLIDA. Tente Novamente!')
    exit()


#CODIGO DO GUANABARA MAIS LIMPO, POREM MENOS PROFISSIONAL

# print(f'{'Lojas Lipee' :=^40}')

# preco = float(input('Preço das compras: R$'))

# print('''FORMAS DE PAGAMENTO
# [ 1 ] À Vista dinheiro / cheque
# [ 2 ] À Vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão''')

# opcao = int(input('Qual é a opcão: '))

# if opcao == 1:
#     total = preco - (preco * 10 / 100)
# elif opcao == 2:
#     total = preco - (preco * 5 / 100)
# elif opcao == 3:
#     parcela = preco / 2
#     total = preco
#     print(f'Sua compra sera parcela em 2x de R${parcela:.2f} SEM JUROS')
# elif opcao == 4:
#     parcelax = int(input('Quantas parcelas: '))
#     parcela = preco / parcelax
#     total = preco + (preco * 20 / 100)
#     print(f'Sua compra sera parcelada em {parcelax}x de R${parcela:.2f} COM JUROS')
# else:
#     print('Opção de pagamento INVÁLIDA. Tente novamente!')
#     exit()

# print(f'Sua compra de R${preco:.2f}, vai custar R${total:.2f} no final.')