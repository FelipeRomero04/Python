frase = str(input('Digite uma frase: '))
palavra = frase.split()
maior = ''

for x in palavra:
    if len(x) > len(maior):
        maior = x

print(maior)