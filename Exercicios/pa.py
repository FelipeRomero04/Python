print('='*22)
print('10 TERMOS DE UMA PA')
print('='*22)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
fim = (razao * 10) + termo # SOMANDO AO TERMO O PROGRAMA GARANTE Q SEMPRE CHEGARA AO DECIMO E NAO PASSARÁ DISSO, JÁ QUE O SEGUNDO PARAMETRO(fim), PARA 1 NUMERO ANTES
cont = 0

for c in range(termo, fim, razao):
    print(f'{c} => ', end='')
    cont += 1
print('ACABOU')
print(f'Esses são os {cont} número de sua PA')


