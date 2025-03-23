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
print(f'{'cod':<5} {'nome':<12}{'gols'}{'total':>15}')
print('==' * 30)

for i, d in enumerate(list_dados):
    print(f'{i:<5} {d['nome']:<15} {d['gol']}{d['total']:>15}')
    
print('==' * 30)

while True:
    jogador = input('Mostrar dados de qual jogador[ENTER p/sair]? ').strip()
    if not jogador:
        break
    jogador = int(jogador)
    print(f' -- Levantamento do jogador {list_dados[jogador]['nome']}: ')
    performance = list_dados[jogador]['gol']
    for i in range(1, len(list_dados[jogador]['gol']) + 1):
        print(f'    No jogo {i} fez {performance[i - 1]} ')
    print('==' * 30)

#Usar o len(list_dados['gol'] pra fazer a contagem da partida)