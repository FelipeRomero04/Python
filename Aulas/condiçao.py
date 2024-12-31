n1 = float(input('Insira a sua nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2) / 2

if m >= 6:
    print(f'Sua média é {m:.2f}. Você está na media! Parabéns')
if m <= 5:
    print(f'Sua média é {m:.2f}. Você está de recuperação!')
else m == 0:
    print(f'Sua média é {m:.2f}. Você repetiu!')
