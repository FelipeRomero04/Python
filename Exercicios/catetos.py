from math import hypot

ca = float(input('Defina um comprimento para o cateto adjacente: '))
co = float(input('Defina um comprimento para o cateto oposto: '))
hip = hypot(ca, co)

print(f'O comprimento da hipotenusa é {hip:.2f}')


















#MEU METODO ABAIXO, MELHOR METODO ACIMA



'''import math

adj = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do cateto oposto: '))

hip = math.sqrt(op**2 + adj**2)

print(f'A hipotenusa é {hip:.2f}')'''

