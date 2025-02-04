from time import sleep

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

if n1 == int(n1) and n2 == int(n2):
    n1 = int(n1)
    n2 = int(n2)

while True:
    print('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos numeros\n[ 5 ] Sair do programa''')

    opcao = str(input('>>>>> Digite sua opção: '))
    
    if opcao == '1':
        r = n1 + n2
        print(f'A soma entre {n1} + {n2} = {r}')
    elif opcao == '2':
        r = n1 * n2
        print(f'A multiplicação entre {n1} X {n2} = {r}')
    elif opcao == '3':
        if n1 > n2:
            print(f'O numero {n1} é maior que o {n2}.')
        elif n1 == n2:
            print(f'Os número {n1} e {n2} são iguais.')
        else:
            print(f'O numero {n2} é mairo que o {n1}.')
    elif opcao == '4':
        print('Informe os número novamente.')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        if n1 == int(n1) and n1 == int(n2):
            n1 = int(n1)
            n2 = int(n2)
    elif opcao == '5':
        print('Finalizando...')
        sleep(2)
        break
    else:
        print('Opção inválida. Tente Novamente.')
    sleep(2)
    print('=-' * 20)
   
print('Fim do programa! Volte sempre!')


