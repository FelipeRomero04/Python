jogador = {'nome': input('Nome do jogador: ')}
num_part = int(input(f'Quantas partidas {jogador['nome']} jogou: '))

list_gols = []

for g in range(1, num_part + 1):
    list_gols.append(int(input(f'Quantos gols na {g}ª partida? ')))

jogador['gols'] = list_gols
jogador['total'] = sum(list_gols)

print('=-' * 30)
print(jogador)
print('=-' * 30)

for k, v in jogador.items():
    if k == 'gols':
        print(f'O campo {k} tem o valor {' / '.join(str(v) for v in jogador['gols'])}')
        continue
    print(f'O campo {k} tem o valor {v} ')

print('=-' * 30)

print(f'O jogador {jogador['nome']} jogou {num_part} partidas.')

for i ,g in enumerate(list_gols, start=1):
    print(f'   => Na partida {i}, fez {g} gols.')
print(f'Foi um total de {jogador['total']} gols.')








    
