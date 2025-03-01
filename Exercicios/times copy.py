from os import system
import pandas as pd

system('cls')

brasileirao = {
    'time': ('Flamengo', 'Bahia', 'Botafogo', 'Vasco', 'Ponte Preta'),
    'pontos': (79, 73, 70, 68, 66)
}
#Criei a coluna da posicão antes de criar o datafreme

tabela = pd.DataFrame(brasileirao)

tabela.index = range(1, len(brasileirao['time']) + 1)
tabela = tabela.reset_index().rename(columns={'index': 'posicao' })
tabela.to_excel("tabelabrasil2.xlsx", index=False)


# TENTE INTERPRETAR TD ISSO DA MELHOR FORMA


#por que consegui colocar a posicao renomeando o index, sendo que coloquei o index=False?










        
       
        








