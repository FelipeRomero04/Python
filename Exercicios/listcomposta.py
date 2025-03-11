dados  = []

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
    
    while True:
        opcao = input('Quer continuar[S/N]: ').strip().upper()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        print('Opção Inválida.')

    if opcao in ('N', 'NAO', 'NÃO'):
        break

cont = int(len(dados) / 2)

print(f'Ao todo, você cadastrou {cont} pessoas')

maior = menor = dados[1]

for p in range(1, len(dados), 2):
    if dados[p] >= maior:
        maior = dados[p]
        
    if dados[p] <= menor:
        menor = dados[p]

print(f'O maior peso foi {maior}Kg. Peso de ',end='')
for n in range(0, len(dados), 2):
    if dados[n + 1] == maior:
        print(f'{dados[n]}', end='')
    if dados[n + 1] == menor:
        print(f'{dados[n]}\n',end='')
        


        


# if x for o maior peso mostre a pessoa que esta atras [indice - 1] 

