class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []


    def adicionar_notas(self, *notas):
        
        invalid_grade = 0
        
        for i, n in enumerate(notas):
            
            if 0 <= n <= 10:
                self.notas.append(n)
                continue
    
            invalid_grade += 1

        if invalid_grade > 0:
            print(f'Notas inválidas removidas: {invalid_grade}')

      
    def media(self):
        if not self.notas:
            return None

        try:
            media = sum(self.notas) / len(self.notas)
            return media
        except ZeroDivisionError:
            return 'Houve um erro na validação das notas'
    

    def mostrar_notas(self):
        media = self.media()
        if media is None:
            return f'Aluno: {self.nome}\nNotas: (Sem notas disponiveis)\nMédia: 0'
        return 


dados_aluno = Aluno('Felipe')
try:
    dados_aluno.adicionar_notas()
    print(dados_aluno.mostrar_notas())
except TypeError:
    print ('ERROR: Apenas digitos são permitidos no campo.')






# def adicionar_notas(self, *notas):
#         self.notas = list(n if 0 <= n <= 10 else -1 for n in notas )
#         if -1 in self.notas:
#             self.notas = 'Notas inválidas! Tente novamente.'



