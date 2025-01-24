num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1):
    if num % c != 0:
        print(f'\033[31m{c} ', end='')
    if num % c == 0: # Testar o ELSE sempre pra vê se adequado ou não(Explicação abaixo)
        cont += 1
        print(f'\033[33m{c} ', end='')
        
print(f'\n\033[97mO número {num} foi divisivel {cont} vezes.') 
      
if cont == 2:
    print('\033[97mE por isso ele é primo')
else:
    print('\033[97mE por isso ele não é primo')
    
    #LER IMPORTANTE

'''Pensei que o uso do ELSE não seria adequado ja que, se o IF nao fosse verdadeiro apenas os numeros do ELSE ficariam coloridos. ERREI FUI MLK. Cada elemento dentro do range é individual,portanto, cada número passa por todas as condições, ganhando a cor definida e passando para o proximo.'''

