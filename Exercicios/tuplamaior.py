from os import system
import random

system('cls')

#for range faz com que um numero aleatorio seja gerado 5 vezes

#sorte = tuple(random.randint(1,11) for c in range(5))
#metodo com compreensao de gerador acima

sorte = tuple(random.sample(range(11), 5))
#retorna uma uma tupla com 5 elementos de 0 a 10
print(f'{' '.join(str(r) for r in sorte)}')
print(f'O maior número é: {max(sorte)}')
print(f'O menor número é: {min(sorte)}')

#Forma reduzida acima

'''
tupla = ()

for r in range(5):
    r = random.randint(1, 10)
    tupla += (r,)

print(f'Os valores sorteados foram: {' '.join(str(r) for r in tupla)}')#Le de tras pra frente
# para cada r em tupla, transforme r em str, e junte usando join


print(f'O maior número é {max(tupla)}')
print(f'O menor número é {min(tupla)}')


sobre a compressão de gerador:
O join() vai pegando um valor de cada vez, convertendo em str e concatenando, sem armazenar tudo de uma vez na memória.
'''


