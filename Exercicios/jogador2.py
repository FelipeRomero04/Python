list_dados = []

while True:
    dados = {'nome': input('Nome do jogador: ')}
    num_part = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    list_gols = []

    for i in range(1, num_part + 1):
        list_gols.append(int(input(f'Quantos gols na {i}ª partida? ')))

    dados['gol'] = list_gols    
    dados['total'] = sum(list_gols)
    list_dados.append(dados)

    while True:
        opcao = input('Deseja continuar[S/N]: ').strip().upper()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        print('Erro! Preencha o campo corretamente.')
    if opcao in ('NAO', 'NÃO', 'N'):
        break

print('=-' * 30)

print('cod nome  gols total')

for d in list_dados:
    for i ,v in enumerate(d.values()):
        print(f'{i}, {v} ', end='')
    
#Fazer um for aninhado .values 
  
