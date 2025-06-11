class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
       
    def adicionar_notas(self, *nota):
        try:
            for n in nota:
                self.notas.append(n)
            return f'As notas do aluno {self.nome} são {self.notas}'
        except Exception:
            raise ('Erro: Os valores informados são inválidos...') 


    def media(self):
        media = float(sum(self.notas) / len(self.notas))
        return f'Média do aluno: {self.nome} - {media:.2f}'
        

dados_aluno = Aluno('Felipe', [4,2,5,1])

print(dados_aluno.adicionar_notas(4,4,2,1))
print(dados_aluno.media())

        
#Ver como colocar listas nisso esqueci


#Por que não consigo mudar a tupla pra list?