from random import randint
from time import sleep

print('-=-'*35)
print('Vou pensar em um numero de 0 a 5. Você consegue adivinhar?')
print('-=-'*35)

result = int(input('Qual número eu pensei? '))
n = randint(0, 5)

print('PROCESSANDO...')
sleep(3)

if n == result:
    print(f'VOCÊ GANHOU! Eu pensei no numero {n}')
else:
    print(f'GANHEI! Eu pensei no {n} não no {result}. PERDEDOR')






