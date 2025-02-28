'''n = int(input('Informe um número: '))
p = ''
cont = 1
l = 1
for i in range(l):
    l += 1
    for c in range(n):
        i += cont
        p += str(i)
        print(p)'''

# MEU MÉTODO ACIMA

n = int(input('Digite um valor: '))

for i in range(1, n + 1):
    p = '' # Reiniciando a váriavel
    for c in range(1, i + 1):
        p += str(c)
    print(p)
   
# ANOTAÇÕES:

# importante o uso inteligente do range()! O for interno tem a var i dentro do range(), fazendo com que a cada iteração do for EXTERNO, mudasse a quantidade de iterações do for INTERNO. Fazendo com que p acumulasse a quantia correta, antes de passar para o proximo 'andar' da pirâmide.