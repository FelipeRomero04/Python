somidade = 0
velho = 0
nomevelho = ''
cont = 0
invalido = ['1','2','3','4','5','6','7','8','9','0']

for i in range(1,5):
    print(f'-------{i}ª Pessoa--------')
    nome = str(input('Nome: '))

    if any(inv in invalido for inv in nome):
        print('\nNome inválido. Tente novamete.')
        exit()

    idade = int(input('Idade: '))
    sexo = str(input('Sexo[F/M]: ')).upper()
    somidade += idade

    if idade > velho and sexo == 'M':
        nomevelho = nome
        velho = idade

    if idade < 20 and sexo == 'F':
        cont += 1

    if sexo != 'F' and sexo != 'M':
        print('Opcão inválida. Tente novamente.')
        exit()

media = somidade / i

print(f'\nA media de idades do grupo e de {media:.2f} anos\n-------//-------')
print(f'O homem mais velho tem {velho} anos e seu nome é {nomevelho}.\n-------//-------')
print(f'Ao todo tem {cont} {'mulher' if cont == 1 else 'mulheres'} com menos de 20 anos.')


#LOGICA DO GUANABARA// MINHA LOGICA ESTA NO PRATICMINHA 030






