lista = []
impar = []
par = []

for i in range(5):
    n = int(input('Digite um valor: '))
    (lista, par if n % 2 == 0 else lista, impar).append(n) 

print(lista)
print(par)
print(impar)