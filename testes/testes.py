from os import system

system('cls')

dados  = []
usuarios = []
maior = menor = 0
while True:

    dados.append(input('Nome: '))

    while True:
        try:
            peso = float(input('Peso: '))
            if peso > 0:
                dados.append(peso)
                break
        except ValueError:
            print(f'Erro de validação. Tente novamente.')
    
    if len(usuarios) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1] #Melhoria feita apos ver video(mais simplificado) LER ABAIXO
        elif dados[1] <  menor:
            menor = dados[1]

    usuarios.append(dados[:])
    dados.clear()
    
    while True:
        opcao = input('Quer continuar[S/N]: ').strip().upper()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        print('Opção Inválida.')

    if opcao in ('N', 'NAO', 'NÃO'):
        break

for n, p in usuarios:
    print(n)
    print(p)