class Aluno:
    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = notas

    def adicionar_notas(self, *notas):
        self.notas.append(notas)
        return f'As notas do aluno {self.nome} são {self.notas}'


dados_aluno = Aluno('Felipe', [8, 5, 2])

print(dados_aluno.adicionar_notas([10, 4, 2]))

        
#Ver como colocar listas nisso esqueci