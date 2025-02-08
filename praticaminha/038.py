num = int(input('Calcular seu fatorial: '))
cont = num
fatorial = ''
r = 1

while cont != 0:
    r *= cont
    if cont == num:
        fatorial += str(cont)
        cont -= 1
    else:
        fatorial += ' X ' + str(cont)
        cont -= 1
    
    
print(f'{num}! = {fatorial} = {r}')