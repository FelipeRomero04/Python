homens = []
mulheres = []
total = []
invalido = ['1','2','3','4','5','6','7','8','9','0']

for info in range(1,5):
    print(f'-------{info}ª PESSOA-------')
    nome = str(input('Nome: ')).title()
    if any(inv in invalido for inv in nome):
        print('Nome inválido. Tente novamente.')
        exit()

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    total.append(idade)
    
    if sexo == 'M': #cria uma lista de dicionarios
        homens.append({'nome': nome, 'idade': idade, 'sexo': sexo})
        maior_idade = homens[0]

    if sexo == 'F':
        mulheres.append({'nome': nome, 'idade': idade, 'sexo': sexo})

    if sexo != 'M' and sexo != 'F':
        print('Opção Invalida. Tente novamente')
        exit()

media = sum(total) / len(total)

print(f'\nA media de idade do grupo e de {media}\n----------//-----------')

cont = 0

for h in homens: #Percorreu todas os dicionarios dentro da lista homens
    if h['idade'] > maior_idade['idade']:
        maior_idade = h #Não recebe somente idade,mas sim o dicionario inteiro com a maior idade, com nome,sexo...
for m in mulheres:
    if m['idade'] < 20:
        cont += 1

print(f'A homem mais velho tem {maior_idade['idade']} anos e seu nome é {maior_idade['nome']}\n----------//-----------')
print(f'Ao todo tem {cont} mulheres com menos de 20 anos\n')



    














