'''email = str(input('Digite seu email: '))

if '@' in email:
    print(f'O nome de usúario do seu email é {email[:email.find('@')]} ') # A string termina qnd chega no '@', não incluindo o '@'.
    print(f'O seu domínio é {email[email.find('@') + 1:]}') # A string comeca no '@' e vai ate o final, porem ao começar, tbm o inclui. Adicionando +1 ao fatiamento, o '@' é eliminado.
else:
    print('Email inválido! Tente novamente.')
    

    
-----------------------------------Outro METODO-------------------------------------

    email = str(input('Digite seu email: '))

    if '@' in email:
    email = email.split('@')
    if len(email) == 2:
        usuario = email[0]
        dominio = email[1]

else: 
    print('Email inválido. Tente novamente.')
    exit()

print(f'O nome do seu usuário é {usuario}')
print(f'O dominio do seu email é {dominio}')


    
    
    
 ================================================================================
    
    
    elif usuario - usuario.count('') not in email and
    
    
    
    
    '''


'''email = str(input('Digite seu email: '))
partes = email.split('@')
usuario = partes[0]
dominio = partes[1]

if '@' not in email:
    print('Email invalido. Tente novamente!')

elif '.com' not in email:
    print('Email Invalido. Tente novamente!')
elif usuario == '':
    print('Email invalido. Tente novamente!')
elif dominio == '':
    print('Email invalido. Tente novamente!')

else:
    print(f'Usuário: {usuario}')
    print(f'Dominio: {dominio}')'''






email = str(input('Digite seu email: '))
usuario = ''
dominio = ''
partes = email.split('@')

if len(partes) == 2:
    usuario = partes[0]
    dominio = partes[1]
else: 
    print('invalido')
if usuario == '':
    print('invaldio')
elif dominio == '':
    print('invalido')
elif '.com' not in email:
    print('invalido')

else:
    print(usuario)
    print(dominio)







'''if '@' in email:
    email = email.split('@')
    if len(email) == 2:
        usuario = email[0]
        dominio = email[1]
    elif usuario == '':
        print('Email inválido. Tente novamente')
    elif dominio == '':
        print('Email inválido. Tente novamente')
    elif '.com' not in email:
        print('Email inválido. Tente novamente')
    else:
        print(f'O nome do seu usuário é {usuario}')
        print(f'O dominio do seu email é {dominio}')'''
















