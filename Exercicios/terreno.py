print('Controle de Terreno')
print('-' * 30)

def area(l, c):
    total = l * c 
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {total}m².')

area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))