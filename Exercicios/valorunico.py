from os import system

system('cls')

lista = []

while True:
    while True:
        try:
            num = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Esse valor não existe.')

    if num not in lista:
        lista.append(num)
        print('Valor armazenado com sucesso...')
    else:
        print('Valor duplicado! Não adicionado a lista...')

    print('=' * 30)

    while True:
        opcao = input('Quer continuar[S/N]? ').upper().strip()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        print('Valor invalido. Tente novamente...')

    print('=' * 30)

    if opcao in ('NAO', 'N', 'NÃO'):
        break

lista.sort()
print(f'Você digitou os valores {lista}')
    
        