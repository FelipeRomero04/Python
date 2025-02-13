from os import system

system('cls')

r = 1

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('-'*40)
        break
    print('-'*40)
    for i in range(1, 11):
        r = num * i
        print(f'{num} x {i} = {r}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre')
print('-'*40)

'''r = 1
num = 1

while True:
    t = 0    #reiniciando t para que o 2º while rode novamente(ja q no 1º loop ele ja sera 10)
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*40)
    if num < 0:
        break
    while t != 10:
        t += 1
        r = num * t
        print(f'{num} x {t} = {r}')
    print('-' * 40)
    
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('-' * 40)'''
        
    