# def ficha(nome : str = '<desconhecido>', gols : int = 0):
#     if not nome:
#         nome = '<desconhecido>'
#     if not gols:
#         gols = 0
#     return f'O jogador {nome} fez {gols} gol(s) no campeonato!'


# jogador = input('Nome do jogador: ').strip()
# try:
#     quant_gols = int(input('Quantidade de gols: '))
# except Exception:
#     quant_gols = ''

# print(ficha(jogador, quant_gols))

#METODO GUANABARA:

def ficha(jogador : str = '<desconhecido>', gols : int = 0):
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato!'

nome = input('Nome do jogador: ')
quant_gols = input('Número de gols: ')

if not quant_gols.isnumeric():
    quant_gols = 0

if nome.strip() == '':
    print(ficha(gols=quant_gols))
else:
    print(ficha(nome, quant_gols))