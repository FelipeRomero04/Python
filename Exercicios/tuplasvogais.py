palavras = ('LINGUAGEM','APRENDER','SEXO')


for p in palavras:
    print(f'\nNa palavra {p} temos: ',end='')
    for v in p:
        if v in ('A','E','I','O','U'):
            print(v, end=' ')