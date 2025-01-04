from time import localtime

ano = int(input('Que ano quer analisar? Coloque 0 pra analisar o ano atual: '))

if ano == 0:
    ano = localtime().tm_year #O tm_year nao possui (), pois é um atributo de localtime, tendo varios(year, day, hour... ). Essa e a forma correta de selecionar um

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NÂO É BISSEXTO')



