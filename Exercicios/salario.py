sal=float(input('Qual o salário do Funcionário: R$'))
porc=float(input('Quantos % de aumento o funcionario irá receber: '))
aum= (sal*porc)/100
final= sal+aum

print(f'Um Funcionário que ganhava R${sal}, recebendo um aumento de {porc:.0f}%, passa a receber R${final:.2f}.')



# 15/1004