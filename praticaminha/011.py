from time import sleep

palavra = str(input('Digite uma palavra: ')).lower()

print('VERIFICANDO SE É UM PALINDROMO...')
sleep(2)

if palavra == palavra[::-1]:
    print(f'A palavra {palavra} é um polindromo.')
else:
    print(f'A palavra não é um polindromo. Veja:\n{palavra} = {palavra[::-1]} ')

