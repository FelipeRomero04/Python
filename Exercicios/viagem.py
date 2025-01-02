km = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a inciar uma viajem de {km:.1f}Km.')
if km <= 200:
    print(f'O preço da sua viagem sera de R${km * 0.50:.2f}')
else:
    print(f'O preço da sua viagem será de R${km * 0.45:.2f}')