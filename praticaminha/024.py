frase = str(input('Digite uma frase: '))
palavra = frase.split()
cont = 0

for i in range(len(palavra)):
    cont += 1

print(f'A sua frase tem {cont} palavras')
    