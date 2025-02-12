palavra = str(input('Digite uma palavra: '))

for x in range(1, len(palavra) + 1):
    print(f'{palavra[x]}: {x}')