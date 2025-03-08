par = []
impar = []


while True:
    while True:
        try:
            n = int(input('Digite um valor: '))
            if n % 2 == 0:
                par.append(n)
                break
            else:
                impar.append(n)
                break
        except ValueError:
            print('Entrada inválida. Tente novamente!')
    while True:
        opcao = str(input('Deseja continuar[S/N]: ')).strip().upper()
        if opcao in ('N', 'NÃO', 'NAO','S', 'SIM'):
            break
        print('Entrada incorreta...')
    if opcao in ('N', 'NAO', 'NÃO'):
        break

list_completed = par + impar

print(f'A lista completa é: {list_completed}')
print(f'A lista de pares é: {par}')
print(f'A lista de imapares é {impar}')