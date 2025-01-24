from time import localtime

atual = localtime().tm_year
maioridade = 21
menor = 0
maior = 0

for c in range(1,8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    if atual - nasc >= maioridade:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')
