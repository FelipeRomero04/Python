frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace('á', 'a')



print(f'A letra A aparece {frase.count('a')} vezes')
print(f'A primeria letra A apareceu na posição {frase.find('a') + 1 }')
print(f'A Ultima letra A apareceu na posição {(frase.rfind('a') + 1) - (frase.count(' '))}')

