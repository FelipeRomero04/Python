nome = str(input('Digite seu nome: ')).title()

if nome == 'Felipe':
    print('Que nome pika')
elif nome == 'João' or nome == 'Matheus' or nome == 'Jorge':
    print('Seu nome é bem comum na angola')
else:
    print('Seu nome é um lixo')

print(f'Tenha um bom dia, {nome}!!!')