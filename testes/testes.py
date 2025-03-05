lista = []
for c in range(0, 5):
    num = int(input(f'Digite um número para a posição {c+1}: '))
    lista.append(num)
nummax = max(lista)
nummin = min(lista)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi: {max(lista)} e a sua posição é: {lista.index(nummax)+1}')
print(f'O menor valor digitado foi: {min(lista)} e a sua posição é: {lista.index(nummin)+1}')