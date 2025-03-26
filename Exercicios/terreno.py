def area(l, c):
    a_total = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a_total}m².')

print('Controle de Terreno')
print('-' * 30)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

#Outro metodo

def area(larg, comp):
    a_total = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a_total}m².')

print('Controle de terreno.')
print('-' * 30)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)