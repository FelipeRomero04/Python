from random import choice

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
sorteio = choice([al1, al2, al3, al4])


print(f'O aluno escolhido foi {sorteio}')


# PARA CRIAR LISTA E NECESSARIO USAR [] 
# lista = [n1, n2, n3, n4]