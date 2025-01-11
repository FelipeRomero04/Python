num1 = str(input('Digite o primeiro valor: '))
num2 = str(input('Digite o segundo valor: '))


if '.' in num1:
    if num1 > num2:
        print(f'O {float(num1)} é maior que {num2}')
    elif num2 > num1:
        print(f'O {num2} é maior que {num1}')
    else:
        print('Eles são IGUAIS')

elif '.' in num2:
    if num2 < num1:
        print(f'O número {num1} é maior que o {float(num2)}')
    elif num2 > num1:
        print(f'O número {float(num2)} é maior que o número {num1}')
    else:
        print('Os dois são IGUAIS')

elif '.' in num1 and '.' in num2:
    if float(num1) > float(num2):
        print(f'O número {num1} é maior que o {num2}')
    elif float(num1) < float(num2):
        print(f'O número {num2} menor que o {num1}')
    else:
        print('Os dois são IGUAIS')

elif not '.' in num1 and not '.' in num2:
    if int(num1) > int(num2):
        print(f'O número {num1} é maior que {num2}')
    elif int(num2) > int(num1):
        print(f'O número {num2} é maior que {num1}')
    else:
        print('Eles são IGUAIS')



    






    



