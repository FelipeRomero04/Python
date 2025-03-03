palavras = ('LINGUAGEM','APRENDER','SEXO')

while True:
    for p in range(len(palavras)):
        print(f'Na palavra {palavras[p]} temos {' '.join(palavras for p in palavras if p in ('a','e','i','o','u'))}')
    break
'''for v in palavras:
    if v.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(v)'''
 
