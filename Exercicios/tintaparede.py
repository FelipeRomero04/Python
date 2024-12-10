lar=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
area= lar*alt
tinta= area/2

print(f'Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.1f}L de tinta.')

