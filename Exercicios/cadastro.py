lista_dados = []
som_idades = 0

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


    som_idades += dados['idade']
    lista_dados.append(dados)
    
    while True:
        opcao = input('Quer continuar?\nPress[S] ou [ENTER P/SAIR]: ').upper().strip()
        if opcao in ('S', 'SIM') or not opcao:
            break
        print('ERRO! Responda apenas S ou N.')
    if not opcao:
        break

print('=-' * 30)

media = som_idades / len(lista_dados)

print(f'A) Ao todo temos {len(lista_dados)} pessoas cadastradas')
print(f'B) A média das idades é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')

list_mulher = ' / '.join(v['nome'] for v in lista_dados if v['sexo'] == 'F')

if list_mulher:
    print(list_mulher)
else:
    print(' - Nenhuma mulher foi cadastrada.')

print(f'D)Lista das Mulheres que estão acima da média: ')
acima_media = False

for d in lista_dados: 
    if d['idade'] > media and d['sexo'] == 'F':   #loop externo percorre um dict por vez
        acima_media = True
        for k, v in d.items():
            print(f'    {k} = {v}; ',end='') #loop interno executado completamente
        print() #linha d'baixo
    
if not acima_media:
    print('  - Todas as mulheres estão na média.')

print('<< ENCERRADO >>')

#Anotar sobre FLAG