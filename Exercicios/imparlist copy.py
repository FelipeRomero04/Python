'''list_completed = []
par = []
impar = []

while True:
    try:
        n = int(input('Digite um valor: '))
        list_completed.append(n)
        (par if n % 2 == 0 else impar).append(n)
    except ValueError:
        print('Entrada inválida. Tente novamente!')
        continue
    while True:
        opcao = str(input('Deseja continuar[S/N]: ')).strip().upper()
        if opcao in ('N', 'NÃO', 'NAO','S', 'SIM'):
            break
        print('Entrada incorreta...')
    if opcao in ('N', 'NAO', 'NÃO'):
        break



print(f'A lista completa é: {list_completed}')
print(f'A lista de pares é: {par}')
print(f'A lista de imapares é {impar}')

#TENTAR FAZER USANDO FUNÇÃO

#METODO COMEÇANDO COM UMA LISTA
'''

lista = []
par = []
impar = []

def insirir_valor():
    try:
        n = int(input('Digite um valor: '))
        (par if n % 2 == 0 else impar).append(n)
    except:
        raise ValueError('ERRO')



while True:
    
    insirir_valor()

    while True:
        opcao = input('Deseja continuar[S/N]: ').upper().strip()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
    
    if opcao in ('NAO', 'NÃO', 'N'):
        break

print(impar)
print(par)