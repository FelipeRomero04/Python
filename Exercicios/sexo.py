s = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]

while s != 'M' and s != 'F':
    s = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {s} registrado com sucesso.')