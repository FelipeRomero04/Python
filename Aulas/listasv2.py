galera = []
dados = []

for p in range(2):
    galera.append(input('Digite seu nome: '))
    galera.append(int(input('Digite sua idade: ')))
    dados.append(galera[:]) 
    galera.clear() # Sem [:] mostraria listas aninhadas vazia,o clear apaga as duas(conexão)

print(dados)
