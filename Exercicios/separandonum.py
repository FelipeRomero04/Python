'''num = int((input('Digite um número: ')))
n2 = str(10000 + num)

print(f'Analisando o número {num}')
print(f'Unidades: {n2[4]}')
print(f'Dezenas: {n2[3]}')
print(f'Centenas: {n2[2]}')
print(f'Milhar: {n2[1]}')'''



#Se quer selecionar somente um caractere de uma cadeia, e so voce selecionar com []

#METODO GUANABARA

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o seu número {num}')
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')