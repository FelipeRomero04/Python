def fatorial(num, show=False):
    """
    Calcula o fatorial de num
    param - num: Valor fatorial
    param - show(opcional): True - Imprimi o calculo completo / False - Imprimi o resultado
    return: Retorna o valor, pu a expressão completa
    """

    expressao = ''
    f = 1

    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print('__' * 14)
                expressao += f'{c} = {f}'
                return expressao
            expressao += f'{c} x '
        
    return f

        
  

    

print((fatorial(4, show=True)))
        

