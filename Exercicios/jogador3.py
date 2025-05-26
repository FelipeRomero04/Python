def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'

jogador = input('Nome do jogador: ')
quant_gols = int(input('Quantidade de gols: '))
print(ficha(jogador, quant_gols))