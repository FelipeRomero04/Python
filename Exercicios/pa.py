print('='*22)
print('10 TERMOS DE UMA PA')
print('='*22)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
fim = (10 * termo) + 1

if fim == 1:
    fim = razao * 10

for c in range(termo, fim, razao):
    print(f'{c} => ', end='')
print('ACABOU', end='')
