class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
       
    def adicionar_notas(self, *nota):
        try:
            for n in nota:
                if not 0 <= n <= 10:
                    return 'ERRO: As notas devem ser definidas de 0 á 10.'
                self.notas.append(n)

        except Exception:
            raise ('Erro: Os valores informados são inválidos...') 


    def media(self):
        media = float(sum(self.notas) / len(self.notas))
        return media
    
    def mostrar_notas(self):
        return f'Aluno: {self.nome} \nNotas: {self.notas} \nMédia: {self.media()}'
        

dados_aluno = Aluno('Felipe')

print(dados_aluno.adicionar_notas(10, -1, 4, 2))
print(dados_aluno.mostrar_notas())


#Arruma isso putaqpariu
        
#Ver como colocar listas nisso esqueci


#Por que não consigo mudar a tupla pra list?