n = float(input('Informe Um número: '))
numb = str(n)

print(f'Parte inteira: {int(n)}')
print(f'Parte decima: {numb[2:4]}')
print(f'Duas casa decimais? {len(numb) <= 7 == 'True'}')


