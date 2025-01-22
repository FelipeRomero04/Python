'''for c in range(8, 0, -1):  # A segunda declaração é ignorada, mostrando um numero abaixo
print('FIM')

---------------------------------------------------------------------------------------------

i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

for c in range(i, f, p):
    print(c)'''

# A segunda declaração é ignorada de acordo com o 'passo' que é definido:
# Uma contagem de (0, 100 , 10) o 100 será ignorado, aparecendo até 90

s = 0

for c in range(0, 4):
    n = int(input('Digite um número: ')) 
    s += n
print(s)
# Para fzr uma somatoria, a soma deve estar dentro da estrutura de repetição
