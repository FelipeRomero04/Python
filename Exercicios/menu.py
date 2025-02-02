from time import sleep

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

while True:
    print('=-' * 30)
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros  
    [ 5 ] Sair do programa''')

    opcao = str(input('>>>>> Digite sua opção: '))

    if opcao == 1:
        r = n1 + n2
        print(f'A soma entre {n1} + {n2} = {r}')
    elif opcao == 2:
        r = n1 * n2
        print(f'A multiplicação entre {n1} X {n2} = {r}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O numero {n1} é maior que o {n2}.')
        else:
            print(f'O numero {n2} é mairo que o {n1}.')
    elif opcao == 4:
        print('Informe os número novamente.')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        break
   
print('Fim do programa! Volte sempre!')


