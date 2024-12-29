nome = str(input('Digite Seu nome completo: ')).strip()
n = nome.split()


print(f'Nome invertido: {nome[::-1]}')
print(f'Total de nomes: {len(nome)}')
print(f'Segundo nome: {n[1]}')
print(f'Contem a letra A: {'A' in nome.upper()}')

