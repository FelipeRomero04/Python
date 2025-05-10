def round_scores(student_scores):

    '''Round score of student'''
    
    return list(round(a) for a in student_scores)


def count_failed_students(student_scores):
    #Verifica se o estudante foi reprovado
    return sum(1 for reproved in student_scores if reproved <= 40)

def above_threshold(student_scores, threshold):
    '''Verificando o the best of score'''
    return list(student for student in student_scores if student >= threshold
)

def letter_grades(highest):
    '''Convertendo notas númericas em letras'''
    
    acrescimo = int((highest-40)/4) # - calcula o intervalo da nota para proximo
    return [41 + acrescimo*i for i in range(4)]  # - incrementa o acrescimo ao limite de pontuação(acumulativo)

print(letter_grades(100))

def student_ranking(student_scores, student_names):
    '''Retorna uma lista rankeando os alunos de acordo com suas respectivas notas'''
    list_ranks = []
    for index, (name, nota) in enumerate(zip(student_names, student_scores), start=1):
        rank = f'{index}. {name}: {nota}'
        list_ranks.append(rank)
    return list_ranks

def perfect_score(student_info):
    
    return next((student for student in student_info if student[1] == 100), [])
#next recebe dois parâmetros, o iterador, e o valor padrão caso o iterador se esgote!


print(perfect_score([['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60], ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]]))

 

'''step = int((highest-40)/4) - calculou o intervalo da nota para proximo
    return [41 + step*i for i in range(4)]  - incrementou        '''


''' return [f"{i + 1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]'''