item=float(input('Valor do produto: R$'))
desc=float(input('Quantos % de desconto: '))
final= item-(item*desc/100)

print(f'O produto que custava R${item:.2f}, com o desconto de {desc:.0f}%, passou a custar R${final:.2f}.')