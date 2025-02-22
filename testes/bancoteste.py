print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)
sacar = float(input('Que valor você quer sacar? R$'))
cédulas = int(sacar // 50), int((sacar % 50) // 20), int(((sacar % 50) % 20) // 10), int(((sacar % 50) % 20) % 10)
valorescédulas = [50, 20, 10, 1]
for c in range(0,4):
    if cédulas[c] != 0:
        print(f'{cédulas[c]}') #ao usar Range, e possivel percorrer listas e tuplas(eu acho) usando c com indicie, ao inves de somente criar linhas, ex. 0,1,2,3... Assim o 'c' assume um valor na tupla a cada iteração
        
       
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


'''print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)
sacar = float(input('Que valor você quer sacar? R$'))
cédulas = int(sacar // 50), int((sacar % 50) // 20), int(((sacar % 50) % 20) // 10), int(((sacar % 50) % 20) % 10)
valorescédulas = [50, 20, 10, 1]
for c in range(0,4):
    if cédulas[c] != 0:
        print(f'Total de {cédulas[c]} cédulas de R${valorescédulas[c]}.00')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''