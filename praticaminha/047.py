
#Gera números pares

'''print(f'{list(x for x in range(21) if x % 2 == 0)}')'''

#Gera numeros ao quadrado

'''print(list(x**2 for x in range(1,11)))'''


#Mosta as vogais da string

'''str = 'COMPREENSÃO'
print(', '.join(v for v in str if v in 'ÃEIOU'))'''

#Mosta palavras de 3 ou menos letras

'''palavras = ['python', 'é', 'incrível', 'e', 'poderoso']

print(', '.join(l for palavra in palavras for l in palavra if len(palavra) <= 3))'''

#Filtrar numeros divisiveis por 3 e 5

'''print(list(n for n in range(1,51) if n % 3 == 0 and n % 5 == 0))'''


#Transforma numeros em par ou impar

'''print(list('Par' if n % 2 == 0 else 'impar' for n in range(0,11)))'''
#Por ter else, o for fica apos ele


f1, f2 = 0, 1

for n in range(0,11):
    print(f1, end=' ')
    soma = f1 + f2
    f1 = f2 
    f2 = soma

