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

print('=-' * 30)
print(f'Ao todo, você cadastrou {len(usuarios)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de {' '.join(f'[{p[0]}]' for p in usuarios if p[1] == maior)}')
print(f'O menor peso foi {menor}Kg. Peso de {' '.join(f'[{n}]' for n, p in usuarios if p == menor)}') #For com 2 var

'''SEMPRE FIQUE ATENTO ONDE É POSSIVEL SIMPLIFICAR O CODIGO.

ja que declarar o maior e o menor é necessario apenas um loop que atualize os valores a cada iteração. Tendo um loop(while) que ja gera valores, manteria o codigo mais limpo, atualizando os valores(maior,menor) a medida que os valores são gerados.
 '''