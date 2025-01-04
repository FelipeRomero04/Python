import time

meuano = time.localtime().tm_year
ano = int(input('Que ano quer analisar? Coloque zero pra analisar o ano atual: '))

if ano == 0:
    ano = meuano  # Atribui o ano atual caso o usuário coloque 0

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} NÃO é bissexto.')



