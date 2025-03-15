brasil = []
estado = {}

for c in range(3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    for u in e.values():
        print(u, end='')
    print()



#Para não atualizar todos os valores da lista, ao atualizar o dicionario, alem de copy():


'''brasil = []

for e in range(3):
    estado = {}   #O dicionario (estado) é reiniciado
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado)
'''

