
num = int(input('Digite um numero inteiro: '))

print('Escolha umas das bases de Conversões:')
print('[1] converter em BINÁRIO')
print('[2] converter em OCTAL')
print('[3] converter em HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao > 3:
    print('Essa opção não existe. Escolha baseado na numeração acima!')

elif opcao == 1:
    num_binar = bin(num)
    print(f'O número {num} em BINÁRIO é {num_binar[2:]}')

elif opcao == 2:
    num_octal = oct(num)
    print(f'O número {num} em OCTAL é {num_octal[2:]}')

elif opcao == 3:
    num_hexa = hex(num)
    print(f'O número {num} em HEXADECIMAL é {num_hexa[2:]}')



