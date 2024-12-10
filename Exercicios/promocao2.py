valor=float(input('Valor do produto: R$'))
parc=float(input('Quantos % de aumento ao parcelar: '))
vista=float(input('Quantos % de desconto à vista: '))
finalp= valor + (valor * parc / 100)
finalv= valor - (valor * vista / 100)

print(f'O valor do produto é de R${valor:.2f}, pagando a vista, obtem um desconto de {vista:.0f}%. Pagando ao todo R${finalv:.2f}.')
print(f'Caso queira parcelar, terá um aumento de {parc:.0f}%. O total a ser pago será de R${finalp:.2f}.')
