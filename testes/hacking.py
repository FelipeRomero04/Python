

def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")

dados = {'nome': 'Fernando', 'idade': 21}

apresentar(**dados)
# Equivale a: apresentar(nome='Fernando', idade=21)
