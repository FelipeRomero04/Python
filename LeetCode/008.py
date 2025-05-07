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
   

    media_real = highest - 40
    limite = media_real // 4

    lista = []
    nota = highest
    for i in range(4):
        lista.append(nota)
        nota = nota - limite
        
    return lista

print(letter_grades(87))

#[41, 56, 71, 86]