num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fatorial = ''
r = 1

while cont != 0:
    r *= cont
    if cont == 1:  #se cont == 1 é por que é o ultimo numero
        fatorial += str(cont) 
    else:
        fatorial += str(cont) + ' x '
    cont -= 1
    


print(f'Calculando {num}! = {fatorial} = {r}')