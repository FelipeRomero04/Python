num = str(input('Digite um número aleatório: '))

lista = ['1', '3', '5','7', '9' ]

if num[-1] in lista:
    print(f'O número {num} é IMPAR')
else:
    print(f'O número {num} é PAR')