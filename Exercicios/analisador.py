'''nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()



print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')}')
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')'''


#Repetindo tudo pra fixar e de outros modos

nome = str(input('Digite seu nome completo: ')).strip()
nospace = nome.replace(' ', '')



print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
#print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')}')
print(f'Seu nome ao todo tem {len(nospace)}')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')

