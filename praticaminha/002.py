n = float(input('Informe Um número: '))
numb = str(n)

print(f'Parte inteira: {int(n)}')
print(f'Parte decimal: {numb[2:4]}')

if '.' in numb:
    inteiro, decimal = numb.split('.')
else:
    inteiro = numb
    decimal = ''
    #ESSA PARTE NAO E RELEVANTE, O CODIGO FUNCIONARA MESMO SEM. POREM E IMPORTANTE ATRIBUIR UM VALOR A TODAS AS VARIAVEIS EM CASO QUE O PROJETO E MAIS LONGO.

if len(decimal) == 2:
    print('Duas casas decimais? Sim!')
else:
    print('Duas casas decimais? Não!')










