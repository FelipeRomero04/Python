lista = []

while True:
    while True:
        try:
            num = int(input('Digite um valor: '))
            lista.append(num)
            break
        except ValueError:
            print('Entrada incorreta. Tente Novamente!')
   
    while True:
        opcao = str(input('Deseja continuar[S/N]: ')).upper().strip()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
    if opcao in ('N', 'NAO', 'NÃO'):
        break

print('=-' * 25)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse= True)}')
if 5 in lista:
    print(f'O valor 5 está na posição {lista.index(5)} da sua lista')
else:
    print('O valor 5 não foi encontrado!')