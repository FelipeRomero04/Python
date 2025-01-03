import time

meuano = time.localtime().tm_year
ano = int(input('Que ano quer analisar? Coloque zero pra analisar o ano atual: '))
bissexto =  ano % 4

if ano == 0:
    ano = meuano

if bissexto == 0 and ano % 400 == 0 and ano % 100 != 0 :
    
    print(f'esse ano e bissexto')
else:
    print(f'nao e bissexto')

 


