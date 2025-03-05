lista = [1, 3, 5, 7, 9]

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1

        else:
            baixo = meio + 1
    return None

print(pesquisa_binaria(lista, 9))

#TENTAR FAZER UMA PESQUISA BINÁRIA, SO QUE COM NOMES


#Como o codigo funciona? !!LEMBRANDO A LISTA DEVE SER ORDENANDA!!

'''Os extremos da lista sao guardados nas var 'alto' e 'baixo', o chute recebe o numero do meio da lista(no caso acima 5) 

caso o chute seja igual o item, ele retorna o meio, que seria o indice que o número que voce quer está

caso o chute seja menor o que o item, é adicionado +1 ao meio(indice), o contrario -1 ao meio, ate que o chute == item, ou o numero não seja encontrado retornando None
 '''


