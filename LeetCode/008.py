def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    
    

    return list(round(a) for a in student_scores)

def count_failed_students(student_scores):
   
   
    return sum(1 for reproved in student_scores if reproved <= 40)

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return list(student for student in student_scores if student >= threshold)

def letter_grades(highest):
   
    media_real = highest - 41
    acrescimo = round(media_real / 4)

    lista = []
    nota_de_corte = 41
    
    for i in range(4):
        
        lista.append(nota_de_corte)
        nota_de_corte += acrescimo
        
    return list(nota_de_corte + acrescimo for i in range(4))



#[41, 53, 65, 77]


def student_ranking(student_scores, student_names):
    list_ranks = []
    for i, (name, nota) in enumerate(zip(student_names, student_scores), start=1):
        rank = f'{i}. {name}  : {nota}'
        list_ranks.append(rank)
    return list_ranks


    

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    return next(student for student in student_info if student[1] == 100)
# 
# list(student[0] if student[1] == 100 else 'nsei' for student in student_info)



print(perfect_score([["Charles", 10], ["Tony", 10], ["Alex", 10]]))


