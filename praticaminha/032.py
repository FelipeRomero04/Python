frase = str(input('Digite uma frase: ')).strip()
vogais = 'aeiouAEIOU'
cont = 0

for v in frase:
    if v in vogais:
        cont += 1

print(f'A frase digitada possui {cont} vogais')


# ou vogais = {'a','e','i','o','u'} verificao mais rapida quando usado (if v in frase)