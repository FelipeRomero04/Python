usuario = {}

nome = input('Nome: ')
media = float(input(f'Média do {nome}: '))

usuario.update({'nome': nome, 'media': media, 'situacao': 'REPROVADO'})
usuario['situacao'] = 'APROVADO' if media >= 7 else 'RECUPERAÇÃO' if 5 <= media < 7 else usuario['situacao']
    
print('=-' * 30)

for k ,v in usuario.items():
    print(f' - {k} é igual a {v}')

# DUAS FORMAS
# FORMA SIMPLIFICADA 
'''
aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
for key, value in aluno.items():
	print(f'{key}:', value)
'''
#A primeira linha cria um dict, ja adicionado chave e valor a ela. Apos isso e adicionado as demais keys and values de forma normal

# ATENÇÂO NO OPERADOR TERNÁRIO:
# O if apos o else da uma condição para esse else ocorrer()	