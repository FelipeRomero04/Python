# nome=input('Qual o seu nome? ')

# print('Prazer em te conhecer {:20}!'.format(nome))
# Escreve em 20 caracteres

# print('Prazer em te conhecer {:>20}!'.format(nome))
# Alinhamento a direita

# print('Prazer em te conhecer {:=^20}!'.format(nome))
# Centralizado e com = ao redor


n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
r = n1%n2

print('A soma dos produtos é {}, a subtração é {}, a multiplicação é {}'.format(a, s, m), end=' ')
# end - PARA CONTINUAR NA MESMA LINHA
# NAO ESQUEÇA DA VIRGULA

print(f'a divisão é {d:.0f} \na divisão inteira é {di}, a potencia é {p}, e o resto é {r}')
