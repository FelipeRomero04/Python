import random
from os import system

system('cls')


baralho = [
    ('A♦️', 11), ('A♠️', 11), ('A♥️', 11), ('A♣️', 11),  
    ('2♦️', 2), ('2♠️', 2), ('2♥️', 2), ('2♣️', 2),
    ('3♦️', 3), ('3♠️', 3), ('3♥️', 3), ('3♣️', 3),
    ('4♦️', 4), ('4♠️', 4), ('4♥️', 4), ('4♣️', 4),
    ('5♦️', 5), ('5♠️', 5), ('5♥️', 5), ('5♣️', 5),
    ('6♦️', 6), ('6♠️', 6), ('6♥️', 6), ('6♣️', 6),
    ('7♦️', 7), ('7♠️', 7), ('7♥️', 7), ('7♣️', 7),
    ('8♦️', 8), ('8♠️', 8), ('8♥️', 8), ('8♣️', 8),
    ('9♦️', 9), ('9♠️', 9), ('9♥️', 9), ('9♣️', 9),
    ('10♦️', 10), ('10♠️', 10), ('10♥️', 10), ('10♣️', 10),
    ('J♦️', 10), ('J♠️', 10), ('J♥️', 10), ('J♣️', 10),  
    ('Q♦️', 10), ('Q♠️', 10), ('Q♥️', 10), ('Q♣️', 10), 
    ('K♦️', 10), ('K♠️', 10), ('K♥️', 10), ('K♣️', 10)]


jogador = []
pc = []

while True:
    while len(jogador) != 2 and len(pc) != 2:
        carta = random.choice(baralho)
        pc.append({
            'naipe': carta[0],
            'valor': carta[1]
        })
        valor_pc = sum(v['valor'] for v in pc )
        carta = random.choice(baralho)
        jogador.append({
            'naipe': carta[0],
            'valor': carta[1]
        })
        valor_jogador = sum(v['valor'] for v in jogador)    
        baralho.remove(carta) 
        
    
   
    # v é um dicionario a cada iteraçao, v['valor'] e a chave desse dicionario que quero

    print('Suas cartas: ')
    for cartas in jogador:
        print(f'[{cartas['naipe']}]',end=' ')
    print(f'Total: {valor_jogador}',end=' ')
    print(f'\nCarta visível do Dealer [{pc[0]['naipe']}]\n')
    
    #USAR FOR SEMPRE QUE FOR IMPRIMIR AS CARTAS, PARA N TER QUE USAR INDICES INEXISTENTES CASO MAIS CARTAS FOREM COMPRADAS(NO CASO ESSA OPÇÃO NÃO ESTA DISPONIVEL NO PROGRAMA)
    if valor_jogador == 21:
        print('Inacreditável! Suas cartas já formam 21!')
        break
    elif valor_jogador > 21:
        print('Que AZAR! Suas cartas ESTOURARAM o limite')
        break
    elif valor_pc > 21:
        print(f'Sorte sua! A carta escondida era um: [{pc[1]['naipe']}]\nTotal: {valor_pc}\nO Dealer ESTOROU!')
        break

    escolha = int(input('Escolha: (1)Pedir carta | (2) Parar\n> '))

    escolha_pc = random.randint(1,2)
    
    if escolha_pc == 1 and valor_pc > 16:
        escolha_pc = 2

    possibilidade = random.randint(9,14)

    if valor_pc < possibilidade:
        escolha_pc = 1

     
    
    def comprar_cartaspc():
        carta = random.choice(baralho)
        pc.append({
            'naipe': carta[0],
            'valor': carta[1]
        })
        baralho.remove(carta)
        return carta 
    
    def comprar_cartasjg():
            carta = random.choice(baralho)
            jogador.append({
                'naipe': carta[0],
                'valor': carta[1]
            })
            baralho.remove(carta)
            return carta #passando o retorno da funcão para reutilizar o valor
    
    #permanecer o valor fora da função

    if escolha == 1:
        newcard_jg = comprar_cartasjg()
        print(f'Voce comprou: [{newcard_jg[0]}]')
        while True:
            try:
                opcao = int(input('(1)Pedir mais uma carta | (2)Parar: '))
                if opcao == 1:
                    newcard_jg = comprar_cartasjg()
                    print(f'Você comprou: [{newcard_jg[0]}]')
                if opcao == 2:
                    valor_jogador += newcard_jg[1]
                    break
                print('Valor Incorreto. Tente Novamente!')

            except ValueError:
                print('Entrada Inválida.')

        
        print('Suas cartas: ')
        for cartas in jogador:
            print(f'[{cartas['naipe']}]',end=' ') #Mostra todas cartas dentro da lista(somente o naipe)
        print(f'Total: {valor_jogador}\n',end=' ')
        if valor_jogador == 21:
            print(f'Jogador Ganhou!')
            break
        elif valor_jogador > 21:  
            print('O Jogador ESTOROU!\n======= O Dealer Venceu! =======')
            break

        if escolha_pc == 1:
            newcard_pc = comprar_cartaspc()  #carta é removida do baralho
            valor_pc += newcard_pc[1]
            print('\nDealer resolveu comprar: ')
            print('Dealer revela suas cartas: ')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}\n', end=' ')
            if valor_pc > 21:
                print('O Dealer ESTOROU! Jogador vencedor') 
                break
            elif valor_pc > valor_jogador:
                print('O Dealer Ganhou!')
            elif valor_pc < valor_jogador:
                print('O jogador Ganhou!')
            else:
                print('Empate')
        
            #bug de jogador vencer e empatar ao msm tempo
    

        if escolha_pc == 2:
            print('\nO Dealer resolveu parar!')
            print(f'Dealer revela suas cartas: ')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}\n',end=' ')
            if valor_pc > valor_jogador:
                print('O Dealer Ganhou!')
            elif valor_pc < valor_jogador:
                print('O jogador Ganhou!')
            elif valor_jogador == valor_pc:
                print('Empataram')
        break

    if escolha == 2: # Mostrar naipe segunda [] sempre 0               
       
         #NESSA OPCAO O JOGADOR PARA, LOGO SOMENTE O DEALER TEM A OPCAO DE PARAR TBM OU CONTINUAR
        if escolha_pc == 1: #dealer compra
            newcard_pc = comprar_cartaspc()  #remove a carta do baralho pra não ter repetições
            print(f'Dealer compra mais uma carta: [{newcard_pc}')  
            valor_pc += newcard_pc[1]
            print('Dealer revela suas cartas: ')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}',end=' ')
            if valor_pc > 21:
                print('\nO Dealer ESTOROU!\n========= Você Ganhou ===========')
            elif valor_pc <= 21 and valor_pc < valor_jogador:
                print(f'\nO Jogador Venceu!\njogador {valor_jogador} X {valor_pc} Dealer\n')
            elif valor_pc <= 21 and valor_pc > valor_jogador:
                print(f'\n======== O Dealer Venceu! =======\n\nDealer {valor_pc} X {valor_jogador} Jogador2\n ')
            break
            
        if escolha_pc == 2: #dealer para
            print('Dealer resolveu parar!')
            print('Dealer revela suas cartas: ', end='')
            for c in pc:
                print(f'[{c['naipe']}]')
                
            if valor_pc > valor_jogador:
                print(f'\nO Dealer Venceu!\n\nDealer {valor_pc} X {valor_jogador} Jogador\n')
            elif valor_pc < valor_jogador:
                print(f'\nO Jogador Venceu!\n\nJogador {valor_jogador} X {valor_pc} Dealer\n')
            else:
                print(f'\nEMPATE!!\n\nJogador {valor_jogador} X {valor_pc} Dealer\n')
            break
    
    
   
    
    

    
    
    




#if jogador in 'JQKA' ou jogador == 'J'
#    jogador +=  10