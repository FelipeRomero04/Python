from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
sleep(3)
print(f'Seu nome em MAIÚSCULAS é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primerio nome é {nome.split()[0]} e ele tem {len(nome.split()[0])}')