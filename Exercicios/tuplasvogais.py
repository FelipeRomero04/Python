palavras = (
    'LINGUAGEM','APRENDER','MERCADO', 'CURSO',
    'GRATIS','PYTHON', 'TRABALHAR', 'MERCADO',
    'PRATICAR')

for p in palavras:
    print(f'Na palavra {p} temos: {' '.join(v for v in p if v in 'AEIOU')}')

#Forma com gerador de compreensão(acima)

#Meu metodo:
'''for p in palavras:
    print(f'Na palavra {p} temos: ',end='')
    for v in p:
        if v in ('A','E','I','O','U'):
            print(v, end=' ')
    print()'''


#FORMA INTERESSANTE DE ACESSAR OS CARACTERES DE UMA LISTA(ABAIXO)


'''lista = ('hoje', 'azul', 'parte', 'coragem', 'computador', 'carro',
         'cachorro', 'jabuticaba', 'jericoacoara', 'filtro')
for p in range(0, len(lista)): 
    for c in range(len(lista[p])): 

        if c == 0: 
            print(f'Na palavra \033[97m{lista[p].upper()}\033[m temos: ', end='')
        if lista[p][c] in 'aeiou': 
            print(f'{lista[p][c]}', end=' ')
    print()'''
