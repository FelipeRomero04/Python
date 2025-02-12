

frase = str(input('Digite uma frase: '))
palavra = frase.split()
maior = ''

for x in palavra:  # A cada iteração o for(x) lê um split, maior sendo 0, a cada iteração
   if len(x) > len(maior): #a maior palavra é atualizada
        maior = x

print(maior)