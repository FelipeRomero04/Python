from os import system

system('cls')
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
print(f'{num}! = {fatorial} = {r}')

# Meu jeito:

'''num = int(input('Calcular seu fatorial: '))
cont = num
fatorial = ''
r = 1

while cont != 0:
    r *= cont
    if cont == num:
        fatorial += str(cont)

    else:
        fatorial += ' X ' + str(cont)
        
    cont -= 1

print(f'{num}! = {fatorial} = {r}')'''


# Com FOR

'''num = int(input('Calcular fatorial: '))
r = 1
fatorial = ''

for f in range(num, 0, -1):
    r *= f
    if fatorial:
        fatorial += ' x ' + str(f)
    else:
        fatorial += str(f)
print(f'{num}! = {fatorial} = {r}')'''



