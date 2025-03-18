from time import localtime

ano_atual = localtime().tm_year

dados = {'nome': input('Nome: ')}.strip()
if any(l.isdigit() for l in dados['nome']):
    print(' - Valor Invalido! O nome não deve conter números...')
    exit()

try:
    nasc = int(input('Data de nascimento: '))
    dados['ctps'] = int(input('Carteira de Trabalho: '))
    if nasc < 0 or dados['ctps'] < 0:
        print('Dados inconsistentes. Tente Novamente!')
        exit()

except ValueError:
    print(' - Preencha o campo corretamente.')
    exit()

dados['idade'] = ano_atual - nasc

if dados['ctps'] == 0:
    print('=-' * 30)
    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')

else:
    while True:
        try:
            dados['contratacao'] = int(input('Ano de contratação: '))
            limit_idade = dados['contratacao'] - nasc

            if dados['contratacao'] <= nasc or limit_idade < 18:
                print('=-' * 30)
                print('Idade e Ano de contratação incorrespondentes.')
                exit()

            dados['salario'] = float(input('Salário: '))

            if dados['salario'] < 0:
                print('=-' * 30)
                print('Salário inválido, insira novamente.')
                continue
            break

        except ValueError:
            print('=-' * 30)
            print('Os campos não foram preechidos corretamente.')

    dados['aposentadoria'] = dados['idade'] + ( 35 - (ano_atual - dados['contratacao']))

    print('=-' * 30)

    for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')




