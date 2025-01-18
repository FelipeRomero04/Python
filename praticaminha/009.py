usuario =str(input('Digite o nome de usuário: '))
senha = str(input('Digite sua senha: '))



if usuario == 'admin' and senha == '12345':
    print('Login bem sucedido!')
elif usuario == 'admin' and senha != '12345':
    print('Senha Incorreta.')
elif usuario != 'admin' and senha == '12345':
    print('Usuário não encontrado.')
else:
    print('Usuário e senha não correspondem. Tente novamente.')




# elif usuario != 'admin' and senha != '12345':
    # print('Usuário e senha não correspondem. Tente novamente.')