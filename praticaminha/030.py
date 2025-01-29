homens = []
mulheres = []
total = []

for info in range(1,6):
    print(f'-------{info}ª PESSOA-------')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    total.append(idade)
    
    if sexo == 'M':
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



    














