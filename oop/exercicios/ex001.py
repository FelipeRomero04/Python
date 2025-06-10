class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f'Olá! meu nome é {self.nome} e tenho {self.idade} anos.'
    


usuario = Pessoa('Felipe', 18)

print(usuario.apresentar())