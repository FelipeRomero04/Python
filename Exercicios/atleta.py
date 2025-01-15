from time import localtime

nasc = int(input('Ano de nascimento: '))
idade = localtime().tm_year - nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')  







