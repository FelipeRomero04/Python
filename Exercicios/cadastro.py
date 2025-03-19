lista_dados = []
idades = []

while True:
    dados = {'nome': input('Nome: ')} #dicionario reiniciado a cada iteração
    if any(l for l in dados['nome'] if l.isdigit()):
        print('Apenas carcateres são permitidos nesse campo.')
        continue
    
    while True:
            dados['sexo'] = input('Sexo[M/F]: ').upper().strip()
            if dados['sexo'] in ('M','MASCULINO', 'F', 'FEMININO'):
                break
            print('Erro! Responda apenas com M ou F.')

    while True:
        try:
            dados['idade'] = int(input('Idade: '))
            if dados['idade'] > 0 and len(str(dados['idade'])) <= 3:
                dados['idade']
                break
            print('Erro! Os dados informados acima estão incorretos.')
        except ValueError:
            print('Somente números devem preencher o campo acima!')


    idades.append(dados['idade'])
    lista_dados.append(dados)
    
    while True:
        opcao = input('Quer continuar[S/N]? ').upper().strip()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao in ('N', 'NAO', 'NÃO'):
        break

print('=-' * 30)

media = sum(idades) / len(idades)

print(f'A) Ao todo temos {len(lista_dados)} pessoas cadastradas')
print(f'B) A média das idades é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ',end='')

f_cadastradas = False

for i, v in enumerate(lista_dados, start=1):

    if v['sexo'] == 'F':
        f_cadastradas = True
        if i == len(lista_dados):
            print(v['nome'], end=' ')
        else:
            print(v['nome'], end=', ')

if not f_cadastradas:
    print('\n  - Nenhuma mulher foi cadastrada.')

acima_media = False

print(f'D)Lista das Mulheres que estão acima da média: ')

for d in lista_dados: #VOLTE AKI
    if d['idade'] > media and d['sexo'] == 'F':   #loop externo percorre um dict por vez
        acima_media = True
        for k, v in d.items():
            print(f'{k} = {v}; ',end='') #loop interno executado completamente
        print() #linha d'baixo
    
if not acima_media:
    print('  - Todas as mulheres estão na média.')
