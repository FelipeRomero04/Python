class Aluno:
    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = list(notas)
        

    def adicionar_notas(self, nota):
        list_nota = []
        for n in self.notas:
            list_nota.append(n)
        list_nota.append(nota)

        self.notas.append(nota)
        return f'As notas do aluno {self.nome} são {self.notas}'


dados_aluno = Aluno('Felipe', (4,2,5,1))

print(dados_aluno.adicionar_notas(4))

        
#Ver como colocar listas nisso esqueci