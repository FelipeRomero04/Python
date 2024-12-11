dia = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
final = (dia * 60) + (km * 0.15)

print(f'O total a pagar é de R${final:.2f}')