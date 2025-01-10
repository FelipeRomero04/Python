casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do sálario: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao =  casa / (anos * 12)

print(f'Para pagar um imóvel de R${casa:.2f}, com o sálario de R${salario:.2f}, financiando em {anos:.0f} anos. O valor da prestaçâo seria de R${prestacao:.2f}.')

if prestacao > salario * 30 / 100:
    print(f'Imprestimo NEGADO! Excedeu o limite de 30%')

elif prestacao < salario * 30 / 100:
    print('Impréstimo CONCEDIDO!')