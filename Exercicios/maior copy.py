from time import sleep

def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados: ')
   
    for n in num:
        if num == (0,):
            break
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    
    # print(f'Foram informados {len(num) if num != (0,) else 0} {'valor' if len(num) == 1 else 'valores'} ao todo.')
    # print(f'O maior número informado foi {max(num)}.') #ARRUMAR UMA FORMA DE TIRAR

    #ACIMA FUNCIONAL SO ARRUMAR O IF COM VALOR
    
    print(f'Foram informados {len(num)} {'valor' if len(num) == 1 else 'valores'} ao todo.')
    print(f'O maior número informado foi {max(num)}.') #ARRUMAR UMA FORMA DE TIRAR
    #Por que o zero n é imprimido no print?
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(0, 2)
maior(6)
maior(0)


# def maior(*num):
#     print('Analisando os valores passados: ')

#     if num == (0,):
#         print('Foi informado 0 valores ao todo. ')
#     else:
#         print(f'{' '.join(str(n) for n in num)} Foram informados {len(num)} valores ao todo.')
#     print(f'O maior número informado foi {max(num)}.')


