'''lista = []
lista2= []

for info in range(1,4):
    print(f'-------{info}ª PESSOA-------')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    lista.append(idade)
    lista.append(idade,sexo)

media = sum(lista) / len(lista)

print(f'A media da idade das pessoas é de {media:.2f}')

# lista2.append({'sexo': sexo, 'idade': idade})

# if lista2[sexo] == M and lista2[idade] == max(lista):

if max(lista) in lista and sexo == M:

'''
homens = []
mulheres = []

for info in range(1,4):
    print(f'-------{info}ª PESSOA-------')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M':
        homens.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    if sexo == 'F':
        mulheres.append({'nome': nome, 'idade': idade, 'sexo': sexo})

print(sum(homens, mulheres))






