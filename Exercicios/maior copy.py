from time import sleep

def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados: ')
    
    if num:
        for n in num:
            print(f'{n} ', end='', flush=True)
            sleep(0.5)

        print(f'Foram informados {len(num)} {'valores' if len(num) != 1 else 'valor'} ao todo.')

    else:
        print('Nenhum valor foi encontrador.')
    print(f'O maior número informado foi {max(num) if num else 0}.')


maior(2, 9, 4, 5, 7, 1) 
maior(4, 7, 0)
maior(0, 2)
maior(6)
maior()


# def maior(*num):
#     print('Analisando os valores passados: ')

#     if num == (0,):
#         print('Foi informado 0 valores ao todo. ')
#     else:
#         print(f'{' '.join(str(n) for n in num)} Foram informados {len(num)} valores ao todo.')
#     print(f'O maior número informado foi {max(num)}.')


