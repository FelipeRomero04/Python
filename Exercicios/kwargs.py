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
    
def media(*args):
    return sum(args) / len(args) #Arrumar essa def sou burro putaqpariu


def notas(*args):
    list = [len(args), max(args), min(args)]
    list2 = ['total', 'maior', 'menor']
    dados = {}
    for k, v in zip(list2, list):
        dados[k] = v
    return dados


print(notas(5.5, 9.5, 10, 6.5))