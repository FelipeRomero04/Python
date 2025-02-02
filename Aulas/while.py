'''c = 0

while c < 10:
    print(c)
    c += 1'''

'''n = 1
r = 'S'

while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n >= 1:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} {'pares' if par > 1 else 'par'} e {impar} {'impares' if impar > 1 else 'impar'}.')
