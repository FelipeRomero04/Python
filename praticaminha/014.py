frase = str(input('Digite uma frase: '))
substituir = str(input('Digite a palavra que deseja substituir: '))
nova_palavra = str(input('Digite a nova palavra: '))

if substituir in frase: # condição completamente desnecessaria(funciona sem)
    nova_frase = frase.replace(substituir, nova_palavra)

print(nova_frase)