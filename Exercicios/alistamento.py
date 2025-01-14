import time

# time.localtime().tm_year
nascimento = int(input('Digite seu ano de nascimento: '))

print(f'Quem nasceu em {nascimento} tem {nascimento - time.localtime()}')



