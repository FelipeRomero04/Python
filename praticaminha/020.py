frase = str(input('Escreva uma frase: '))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

print(f'Frase: {junto}\nInvertido: {inverso}')

if inverso == junto:
    print(f'Essa {'frase' if len(palavra) >= 2 else 'palavra'} é um palíndromo')
else:
    print(f'Essa {'frase' if len(palavra) >= 2 else 'palavra'} não é um palíndromo')