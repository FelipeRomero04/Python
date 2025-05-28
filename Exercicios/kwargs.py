# def notas(*args, sit):
#     list = [len(args), max(args)]
#     dados = {'total': len(args)}
#     dados['maior'] = max(args)
#     dados['menor'] = min(args)
#     dados['media'] = sum(args) / dados['total']
#     if sit:
#         if 6 >= dados['media'] <= 7.5:
#             dados['sit'] = 'Razoável'
#         elif dados['media'] < 6:
#             dados['sit'] = 'Ruim'
#         else:
#             dados['sit'] = 'Ótimo'
#     return dados

# resp = notas(5.5, 9.5, 10, 6.5, sit=True)

# print(resp)
    
def media(tuple_num):
    media = sum(tuple_num) / len(tuple_num)
    return media #Arrumar essa def sou burro putaqpariu


def notas(*args, sit : bool = False):
    """
    Função notas analisa as notas e a situação dos alunos.

    :Param - args: notas dos alunos (aceita varias)
    :Param - sit: (OPCIONAL) Imprimi a situação do aluno
    :return - dados: retorno um dicionário
    """

    list = [len(args), max(args), min(args), media(args)]
    list2 = ['total', 'maior', 'menor', 'media']
    dados = {}
    for k, v in zip(list2, list):
        dados[k] = v 
    if sit:
        if 6 <= dados['media'] <= 7.5:
            dados['sit'] = 'Razoável'
        elif dados['media'] < 6:
            dados['sit'] = 'Ruim'
        else:
            dados['sit'] = 'Ótimo'
    return dados


resp = notas(5.5, 9.5, 3, 6.5, sit=True) 

print(resp)

