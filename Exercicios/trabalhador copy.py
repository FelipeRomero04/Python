from time import localtime
from os import system

system('cls')

ano_atual = localtime().tm_year

dados = {'nome': input('Nome: ')}
if any(l.isdigit() for l in dados['nome']):
    print(' - Valor Invalido! O nome não deve conter números...')
    exit()

try:
    nasc = int(input('Data de nascimento: '))
    dados['ctps'] = input('Carteira de Trabalho[0 se não tem]: ')
    if nasc < 0 or int(dados['ctps']) < 0 or len(dados['ctps']) < 11:
        print('Dados inconsistentes. Tente Novamente!')
        exit()

except ValueError:
    print(' - Preencha o campo corretamente.')
    exit()

dados['idade'] = ano_atual - nasc

if dados['ctps'] != 0:
    while True:
        try:
            dados['contratacao'] = int(input('Ano de contratação: '))
            limit_idade = dados['contratacao'] - nasc

            if dados['contratacao'] <= nasc or limit_idade < 18:
                print('=-' * 30)
                print('Idade e Ano de contratação incorrespondentes.')
                exit()

            dados['salario'] = float(input('Salário: R$'))

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
    if k == 'salario':
        print(f'  - {k} tem o valor R${v}') 
        continue
    print(f'  - {k} tem o valor {v}')




