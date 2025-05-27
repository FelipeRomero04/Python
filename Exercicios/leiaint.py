def leiaint(msg):
    while True:
        r = input(msg)
        if r.isnumeric():
            return r
        print('ERRO! Digite um número inteiro válido.')
    

n = leiaint('digite um número: ')
print(f'Você acabou de digitar o número {n}: ')
    