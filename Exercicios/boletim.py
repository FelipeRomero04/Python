dados = []

cont = 0
media = []
while True:
    nome = input('Nome: ')
    #fazer um try aki
    nt1 = int(input('Nota 1: '))
    nt2 = int(input('Nota 2: '))

    dados.append([nome, nt1, nt2])

    #Colocar as medias dentro das mesmas listas de dados, ou criar uma lista so pra medias?
    #Não seria dificil de manipular dentro de dados(ultimo item -1)


    while True:
        opcao = input('Quer continuar[S/N]: ').upper().strip()
        if opcao in ('S', 'SIM', 'NAO', 'NÃO', 'N'):
            break
    if opcao in ('N', 'NAO', 'NÃO'):
        break

    '''for u in range(len(dados)):
        if u != 0:
            media = u '''

print(media)






