frase = str(input('Digite uma palavra ou frase: '))
vogais = "aeiouAEIOU"
cont = 0
palavra = frase.split()

for c in range(len(frase)):
    if frase[c] in vogais :
        cont += 1

print(f'Essa {'frase' if len(palavra) >= 2 else 'palavra'} tem {cont} vogais.')


