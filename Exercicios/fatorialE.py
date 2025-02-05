num = int(input('Digite um valor: '))
r = 1
cont = num 
fatorial = ''

while cont > 0:
    if fatorial: #Se a string ja tem algo dentro
        fatorial += ' x ' + str(cont)  
    else:         #Forma reduzida = fatorial += f" x {cont}" if fatorial else str(cont)
        fatorial += str(cont)
    
    r *= cont    
    cont -= 1
print(f'{num}! = {fatorial} = {r}', end='')



    

