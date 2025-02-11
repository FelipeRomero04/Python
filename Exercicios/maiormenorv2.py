from os import system

system('cls')

'''lista = []
cont = 1


while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    opcao = str(input('Quer continuar [S/N]? ')).upper()
    if opcao == 'N':
        break
    cont += 1

media = sum(lista) / len(lista)

print(f'Você digitou {cont} número e a média foi {media}')
print(f'O maior valor foi {max(lista)} e o menor foi {min(lista)}')'''

opcao = 'S'
cont = soma = maior = menor =0

while opcao in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    soma += num
    opcao = str(input('Quer continuar [S/N]? ')).strip()[0]

media = soma / cont

print(f'Você digitou {cont} números é a media foi {media}.')
print(f'O maior número é {maior} e o menor {menor}.')

