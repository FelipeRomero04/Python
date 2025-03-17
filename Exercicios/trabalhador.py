from time import localtime

ano_atual = localtime().tm_year

dados = {'nome': input('Nome: ')}
dados['idade'] = ano_atual - int(input('Data de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho: '))

if dados['ctps'] == 0:
    print('=-' * 30)
    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')

else:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ( 35 - (ano_atual - dados['contratacao']))

    print('=-' * 30)

    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')

#ADICIONAR VERFICAÇÕES DE TIPAGEM


