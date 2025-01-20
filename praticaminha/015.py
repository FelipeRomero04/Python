from string import ascii_lowercase, ascii_uppercase

print('''Defina uma senha, ela deve conter:
! Pelo menos 8 caracteres
! Conter uma letra minúscula
! Conter uma letra Maiúscula
! Conter um número
! Conter um caractere especial(@ , #, $, &...)''')

senha = str(input('Senha: ')).strip()
confirmacao = str(input('Senha novamente: ')).strip()

minusculo = list(ascii_lowercase)
maiusculo = list(ascii_uppercase)
numeros = ['1', '2', '3', '4', '5', '6', '7', '8','9','0']
simbolos = ['!', '@', '#', '$', '&', '%', '(', ')', ':', '*'] 

if len(senha) < 8 and len(confirmacao) < 8:
    print('Senha incorreta. A senha deve ter pelo menos 8 digitos!')

elif senha != confirmacao:
    print('Senha Incorreta. A duas senhas não são iguais!')

elif not any(letra_m in senha for letra_m in minusculo) and not any(letra_m in confirmacao for letra_m in minusculo):
    print('Senha Incorreta. A senha deve conter pelo menos uma letra minúscula!')

elif not any(letra_M in senha for letra_M in maiusculo) and not any(letra_M in confirmacao for letra_M in maiusculo):
    print('Senha Incorreta. A senha deve conter pelo menos uma letra maiúscula!')

elif not any(num in senha for num in numeros) and not any(num in confirmacao for num in numeros):
    print('Senha Incorreta. A senha deve conter pelo menos um número!')

elif not any(simb in senha for simb in simbolos) and not any(simb in confirmacao for simb in simbolos):
#se nao tiver nenhum simb em senha, pra cada simb em simbolo
    print('Senha Incorreta. A senha deve conter pelo menos um caractere especial!')

else:
    print('Login bem-sucedido')
