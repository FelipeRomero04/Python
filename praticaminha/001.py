nome = str(input('Digite Seu nome completo: ')).strip().split()



print(f'Total de nomes: {len(nome)}')
print(f'Segundo nome: {nome[1]}')
print(f'Contem a letra A: {'A' in nome.upper()}')