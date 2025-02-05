num = int(input('Digite um valor: '))
r = 1
fatorial = ''

for f in range(num, 0 ,-1):
    r *= f
    if num == f:   #O primeiro número não recebe o X antes, somente no proximo loop
        fatorial += str(f)
    else: 
        fatorial += ' x ' + str(f)

#Para poder armazenar os números gerados pelo loop, fora do loop(ja que so é mostrado  o valor final) é necessario cria uma var vazia que vá armazenando - os, ao decorrer do loop
    
print(f'{num}! = {fatorial} = {r}')


    
        
   