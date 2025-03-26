from time import sleep

def cont(inc, fim , pas):
    
    if inc < fim:
        print('=-' * 30)
        print(f'Contagem de {inc} até {fim} de {pas} em {pas}.')
        for i in range(inc, fim + 1, pas):
            print(f'{i} ', end='', flush=True)
            sleep(0.3)

    else:
        print(f'Contagem de {inc} até {fim} de {pas} em {pas}.')
        for i in range(inc, fim, -pas):
            print(f'{i} ', end='', flush= True) 
            sleep(0.3)
    print('FIM!')
    

    print('=-' * 30)




cont(1, 10, 1)
cont(10, 0, 2)


'''from time import sleep
from os import system

system('cls')

def cont(inc, fim, pas):
    print('=-' * 30)
    print('Contagem de 1 ate 10 de 1 em 1.')
    for i in range(inc, fim, pas):
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
    print('FIM!')
    print('=-' * 30)

def r_cont(inc, fim, pas):
    print('=-' * 30)
    print(f'Contagem de 10 á 0, de 2 em 2')
    for i in range(inc, fim, -pas):
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
    print('FIM!')
    print('=-' * 30)

def my_cont(inc, fim, pas):
    print('=-' * 30)
    print(f'Contagem de {inc} até {fim} de {pas} em {pas}')
    if inc > fim and pas > 0:
        fim -= 1
        pas = -abs(pas)
    else:
        fim += 1
    for i in range(inc, fim, pas):
        print(f'{i} ', end='', flush=True)
        sleep(0.3)
    print('FIM!')
    print('=-' * 30)

cont(1, 10, 1)
r_cont(10, 0, 2)

print('Agora é sua vez de personalizar!')

i = int(input('Início: '))
f = int(input('Fim: ')) 
p = int(input('Passo: ')) 
if p == 0:
    p = 1
if p < 0: #Fica positivo
    p = abs(p)
    
my_cont(i, f, p)'
'''