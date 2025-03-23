list_dados = []

while True:

    dados = {'nome': input('Nome do jogador: ').title()}
    if any(l for v in dados.values() for l in v if l.isdigit()):
        print('Esse campo não pode ser preenchido por números')
        continue

    while True:
        try:    
            num_part = int(input(f'Quantas partidas {dados['nome']} jogou? '))
            if num_part > 0:
                break
            print('Número de partidas inválido')
        except ValueError:
            print('Valor inválido, tente novamente.')

    list_gols = []

    for i in range(1, num_part + 1):
        while True:
            list_gols.append(int(input(f'Quantos gols na {i}ª partida? ')))
            try:
                if list_gols[i-1] < 0:
                    print('ERRO')
                    break
            except ValueError:
                print('Erro')    


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
print(f'{'cod':<5} {'nome':<15} {'gols':<19}{'total':<5}')
print('==' * 30)

for i, d in enumerate(list_dados):
    gols_str = str(d['gol'])
    print(f'{i:<5} {d['nome']:<15}{gols_str:<20}{d['total']:<5}')
    
print('==' * 30)

while True:
    jogador = input('Mostrar dados de qual jogador[ENTER p/sair]? ').strip()
    if not jogador:
        break
    jogador = int(jogador)
    print(f' -- Levantamento do jogador {list_dados[jogador]['nome']}: ')
    performance = list_dados[jogador]['gol'] #Tentar deixar mais limpo
    for i in range(1, len(performance) + 1):
        print(f'    No jogo {i} fez {performance[i - 1]} gols. ')
    print('==' * 30)

#Usar o len(list_dados['gol'] pra fazer a contagem da partida)