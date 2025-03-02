from os import system
import pandas as pd

system('cls')

brasileirao = {
    'time': ("Palmeiras", "Grêmio", "Atlético Mineiro", "Flamengo", "Botafogo",
    "Bragantino", "Fluminense", "Athletico Paranaense", "Internacional",
    "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", 
    "Bahia", "Santos", "Vitória", "Juventude", "Atlético Goianiense",
    "Criciúma"),

    'pontos': (79, 73, 70, 68, 66, 64, 62, 61, 59, 57,  
    55, 54, 52, 51, 50, 48, 46, 44, 42, 40)}


tabela = pd.DataFrame(brasileirao)
tabela.index = range(1, len(brasileirao['time']) + 1)
#fazendo o indice começar em 1
tabela = tabela.reset_index().rename(columns={'index': 'posição' })
#converte o indice padrao do pandas em uma coluna
tabela.to_excel("tabelabrasil.xlsx", index=False)
#colocando o index=False para não aparecer a indexação padrão do pandas


#Outra forma possivel de fazer(abaixo)

'''from os import system
import pandas as pd

system('cls')

brasileirao = {
    'time': ('Flamengo', 'Bahia', 'Botafogo', 'Vasco', 'Ponte Preta'),
    'pontos': (79, 73, 70, 68, 66)
}
brasileirao['posição'] = range(1, len(brasileirao['time']) + 1)
#Crio a coluna da posição

tabela = pd.DataFrame(brasileirao)
#transformo em um Dataframe

tabela = tabela[['posição', 'time', 'pontos']]
#Tabela recebe uma nova tabela com as colunas reorganizadas

tabela.to_excel("tabelabrasil3.xlsx", index=False)'''



#Os [[]] são a sintaxe correta do pandas para selecionar multiplas colunas, caso fosse uma unica coluna apenas [] seria o correto










        
       
        








