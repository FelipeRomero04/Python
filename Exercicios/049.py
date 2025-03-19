def regressivo(num):
    for c in range(num, 0, -1):
        if c == 1:
            print(f'{c} ',end='')
        else:
            print(f'{c}, ',end='')
    




def maior_list(lista_numeros):
    maior = max(lista_numeros)
    return maior

lista = [5, 67, 3, 2, 7, 4]
maior = maior_list(lista)

print(f'O maior da lista é {maior}')    




