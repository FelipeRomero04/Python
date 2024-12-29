nome = str(input('Digite seu nome completo: ')).strip().split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')

# Outro metodo

'''
nome = str(input('Digite seu nome completo: ')).strip().split()

print('Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome) - 1]}')

Explicando a logica: Vai mostrar a variavel (nome) na posição len(nome), mostrando a posiçao 4, um nome de dividido em uma lista de 4. Porém o python o python começa a conta do 0, portanto o 4 não existe, sendo necessario colocar -1.



'''