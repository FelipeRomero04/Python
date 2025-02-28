from os import system

system('cls')


ex = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
      'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
      'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
      'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
      'Dezenove', 'Vinte')

while True:
    while True:
        try:
            
            num = int(input('Digite um número de 0 a 20: '))
            if 0 <= num <= 20:
                break
            print('Tente Novamente! ',end='')
        except ValueError:
            print('Valor incorreto.')
    
    print(f'Você digitou o número {ex[num]}')
    
    print('=' * 20)

    while True:
        opcao = str(input('Quer continuar?[S/N] ')).upper().strip()
        if opcao in ('S', 'SIM', 'N', 'NAO', 'NÃO'):
            break
        else:
            print('Tente Novamente! ',end='')
    print('=' * 20)
    if opcao in ('N', 'NAO', 'NÃO'):
        break

