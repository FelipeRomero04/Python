from time import localtime

sexo = str(input('Digite \033[34m(M)\033[97m se for do sexo mascúlino, \033[31m(F)\033[97m do feminino: ')).upper()

if sexo == 'M':
    print('Preencha as informações a seguir.')
elif sexo == 'F':
    print('Você não precisa se alistar')
    exit()
else:
    print('Iformação inválida')
    exit()

nascimento = int(input('Digite seu ano de nascimento: '))

print()

ano_atual = localtime().tm_year
idade = localtime().tm_year - nascimento

print(f'Quem nasceu em \033[32m{nascimento}\033[97m tem \033[33m{idade} anos\033[97m em \033[35m{localtime().tm_year}\033[97m')

#\033[33m{18 - idade} ano para o alistamento'

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} {'ano' if (saldo) == 1 else 'anos'} para o alistamento')
    print(f'Seu alistamento sera em {ano_atual + saldo}.')

#{ idade - 18} ano\033

elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} {'ano' if (saldo) == 1 else 'anos'}' )
    print(f'Seu alistamento foi em \033[32m{ano_atual - saldo}\033[97m')

else: 
    print('Você tem que se alistar IMEDIATAMENTE!')


#O PROGRAMA ABAIXO E 100% original, O ACIMA SO FOI MUDADO A CONDIÇAO SIMPLIFICADA PARA FICAR MAIS OTIMIZADO(A LOGICA E A MESMA VOCE E PIKA LEK)


''' from time import localtime

sexo = str(input('Digite \033[34m(M)\033[97m se for do sexo mascúlino, \033[31m(F)\033[97m do feminino: ')).upper()

if sexo == 'M':
    print('Preencha as informações a seguir.')
elif sexo == 'F':
    print('Você não precisa se alistar')
    exit()
else:
    print('Iformação inválida')
    exit()

nascimento = int(input('Digite seu ano de nascimento: '))

print()

ano_atual = localtime().tm_year
idade = localtime().tm_year - nascimento

print(f'Quem nasceu em \033[32m{nascimento}\033[97m tem \033[33m{idade} anos\033[97m em \033[35m{localtime().tm_year}\033[97m')

if idade < 18:
    print(f'Ainda falta \033[33m{18 - idade} ano\033[97m para o alistamento' if (18 - idade) == 1 else f'Ainda faltam \033[33m{18 - idade} anos\033[97m para o alistamento')
    print(f'Seu alistamento sera em {ano_atual + (18 - idade )}.')

elif idade > 18:
    print(f'Você ja deveria ter se alistado há \033[33m{ idade - 18} ano\033[97m.'if (idade - 18) == 1 else f'Você já deveria ter se alistado há \033[33m{idade - 18} anos\033[97m.' )
    print(f'Seu alistamento foi em \033[32m{ano_atual - (idade - 18)}\033[97m')

else: 
    print('Você tem que se alistar IMEDIATAMENTE!')
'''


    
   
    






