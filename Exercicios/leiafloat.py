def leiaint(msg):
    while True:
       
        try:
            n = int(input(msg))
            return n
        except Exception:
            print('ERRO! Por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar esse número')
            return 0

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except Exception:
            print('Erro! Por favor, retorne um número real válido')
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar esse número')
            return 0

n_int = leiaint('Digite um número inteiro: ')
n_float = leiafloat('Digite um número real: ')

print(f'O valor inteiro foi {n_int} e o real foi {n_float}')




        