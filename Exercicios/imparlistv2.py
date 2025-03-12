
# Melhoria para simplificar o codigo

num = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    num[n % 2].append(n)  

print(f'Os valores pares digitados foram {sorted(num[0])}.')
print(f'Os valores ímpares digitados foram {sorted(num[1])}.')

#É feito uma operação no indice, com resto de divisão sendo 0 ou 1, alocando diretamente nas posições da lista(Metodo perfeito para exercicios de impar, par)


#Solução original da minha mente abaixo

'''num = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
        
print(f'Os valores pares digitados foram {sorted(num[0])}')     
print(f'Os valores imapares digitados foram {sorted(num[1])}')  

'''