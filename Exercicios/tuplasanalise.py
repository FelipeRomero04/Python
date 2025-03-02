'''analise = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input())
)'''

dados = ()
cont = 0
for i in range(1,5):
    num = (int(input(f'Digite o {i}º número:')))
    if num % 2 == 0:
        cont += 1
    dados += (num,)


print(f'Você digitou os valores {', '.join(str(d) for d in dados)}')
print(f'O valor 9 apareceu {dados.count(9)} vezes') 
try:
    print(f'O valor 3 apareceu na {dados.index(3) + 1}ª posição.')
except ValueError:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram {cont}')
#forma comprimida
#print(f'Os valores pares digitados foram {sum(1 for d in dados if d % 2 == 0)}')
#some 1, para cada d em dados se d for resto 0(par)