'''num = input('Digite um número aleatório: ')
impar =  ['1', '3', '5', '7', '9']

if num[-1] in impar:
    print('É um número Impar')
else:
    print('É um número Par')  '''

#METODO GUSTAVO GUANABARA

'''num = int(input('Digite um número aleatorio: '))
result = num % 2

if result == 0:
    print('É um número PAR')
else:
    print('É um número IMPAR')'''


#OUTRO METEDO

num = int(input('Digite um número: '))
par = (num // 2) * 2

if par == num:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é IMPAR!')


