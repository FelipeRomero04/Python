palavras = ('LINGUAGEM','APRENDER','SEXO')

while True:
    for p in range(len(palavras)):
        print(f'Na palavra {palavras[p]}')
        for v in palavras[p]:
            if v.lower() in ('a','e','i','o','u'):
                print(v, end='' )

    break
'''for v in palavras:
    if v.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(v)'''
 
