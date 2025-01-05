salario = float(input('Digite o valor do salário do funcionário: R$'))
# superior = (salario * 10 / 100) + salario

if salario > 1250:
    aumento = (salario * 10 / 100) + salario

if salario <= 1250:
    aumento = (salario * 15 / 100) + salario

print(f'O funcionário que ganhava R${salario:.2f} passará a ganhar R${aumento:.2f}')