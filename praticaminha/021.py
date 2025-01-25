palavra = str(input('Digite uma palavra: '))
letra = str(input('Qual caractere você quer contar: '))

cont = 0

for i in range(len(palavra)):
    if palavra[i] in letra:
        cont += 1

if palavra[0] == letra.upper():
    cont += 1

print(f'O caractere "{letra}" aparece {cont} vezes na palavra "{palavra}"')