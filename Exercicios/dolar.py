dol=float(input('Qual a cotação do Dolar atual: US$'))
eu=float(input('Qual a cotação do Euro atual: €'))
reais=float(input('Valor para compra: R$'))

print(f'É possivel comprar US${reais/dol:.2f} e {reais/eu:.2f}€')