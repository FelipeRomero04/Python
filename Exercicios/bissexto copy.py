import time

meuano = time.localtime().tm_year
ano = int(input('Que ano quer analisar? Coloque 0 pra analisar o ano atual: '))

if ano == 0:
    ano = meuano

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NÂO É BISSEXTO')


