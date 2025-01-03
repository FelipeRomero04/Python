import time

meuano = time.localtime().tm_year  #E UM ATRIBUTO DO localtime() ENTT N PRECISA DE () no final
ano = int(input('Que ano quer analisar? Coloque 0 se quiser analisar o ano atual: '))
bisexto = ano % 4 

if ano == 0: 
    ano = meuano

if bisexto != 0 or ano == 0 and meuano % 400 != 0 :
    print(f'O ano {ano} NÂO É BISSEXTO ')

else:
    print(f'O ano {ano} É BISSEXTO')

    #O ERRO TA NO CALCULO ARRUME!!!!!!

'''if ano == 0 and meuano % 4 == 0:
    print(f'O ano de {meuano} É BISSEXTO')
else:
    print(f'O ano {meuano} NÂO É BISSEXTO')'''

 


