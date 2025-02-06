import random

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
    carta = random.choice(baralho)
    jogador.append(carta)
    baralho.remove(carta) 
    carta = random.choice(baralho)
    jogador.append(carta)

    carta = random.choice(baralho)
    pc.append(carta)
    baralho.remove(carta)#A carta sorteada é removida do baralho
    carta = random.choice(baralho)
    pc.append(carta)

    valor_jogador  = jogador[0][1] + jogador[1][1]
    valor_pc = pc[0][1] + pc[1][1]
    print(f'Suas cartas: [{jogador [0][0]}] e [{jogador[1][0]}] -> valor: {valor_jogador} ')
    print(f'Carta visível do Dealer {pc[0]}')

    escolha = int(input('Escolha: (1)Pedir carta | (2) Parar\n> '))
    escolha_pc = random.randint(1,2)

    print(escolha_pc)
    
    if escolha == 1:
        carta = random.choice(baralho)
        jogador.append(carta)
        baralho.remove(carta)
        print(f'Voce comprou {jogador[2][0]}')
        valor_jogador += jogador[2][1]
        print(f'Suas cartas [{jogador[0][0]}] ,[{jogador[1][0]}] ,[{jogador[2][0]}], Total: {valor_jogador}')
        if valor_jogador > 21:
            print('O Jogador ESTOROU!\n======= O Dealer Venceu! =======')
        break
        #se nao o dealer escolhe e as cartas sao mostadas
    '''if escolha == 2:
        print('Jogador Resolveu parar!')
        print('Dealer')'''


                                      
       

       #CENARIO EM QUE EU PARO
        
    if escolha_pc == 1: #dealer pede carta e o jogador para
        carta = random.choice(baralho) 
        pc.append(carta)
        baralho.remove(carta)  #remove a carta do baralho pra não ter repetições
        print(f'Dealer compra mais uma carta: [{pc[2][0]}]')  
        valor_pc += pc[2][1]
        print(f'Dealer revela suas cartas: [{pc[0][0]}], [{pc[1][0]}], [{pc[2][0]}],Total: {valor_pc}')
        if valor_pc > 21:
            print('O Dealer ESTOROU!\n========= Você Ganhou ===========')
        elif valor_pc <= 21 and valor_pc < valor_jogador:
            print(f'O Jogador Venceu! // jogador {valor_jogador} X {valor_pc} Dealer')
        elif valor_pc <= 21 and valor_pc > valor_jogador:
            print(f'======== O Dealer Venceu! =======\n\nDealer {valor_pc} X{valor_jogador} Jogador2\n ')
        break
    
    if escolha == 1 and escolha_pc == 1:
        carta = random.choice(baralho)
        jogador.append(carta)
        baralho.remove(carta)
        valor_jogador += jogador[2][1]
        print(f'Jogador compra mais uma carta: [{jogador[2][0]}]')
        carta = random.choice(baralho)
        pc.append(carta)
        baralho.remove(carta)
        valor_jogador += pc[2][1]
        print(f'Dealer compra mais uma carta: [{pc[2][0]}]')
        print(f'Cartas Jogador: [{jogador[0][0]}],[{jogador[1][0]}],[{jogador[2][0]}]\n Dealer: [{pc[0][0]}],[{pc[1][0]}],[{pc[2][0]}]\n')
        if valor_jogador > 21 and valor_pc > 21:
            print('Os dois ESTOURARAM! EMPATE')
        

        # print(f'Jogador {valor_jogador} X {valor_pc} Dealer')
    



    if escolha_pc == 2: #dealer para e o jogador para
        print('Dealer resolveu parar!')
        print(f'Dealer revela suas cartas: [{pc[0][0]}], [{pc[1][0]}], Total: {valor_pc}')
        print(f'Suas cartas: [{jogador[0][0]}], [{jogador[1][0]}], Total: {valor_jogador}')
        if valor_pc > valor_jogador:
             print(f'\nO Dealer Venceu!\n\nDealer {valor_pc} X {valor_jogador} Jogador\n')#Botar dentro de função
        elif valor_pc < valor_jogador:
            print(f'\nO Jogador Venceu!\n\nJogador {valor_jogador} X {valor_pc} Dealer\n')
        else:
            print(f'\nEMPATE!!\n\nJogador {valor_jogador} X {valor_pc} Dealer\n')
        break
    
    
   
    
    

    
    
    




#if jogador in 'JQKA' ou jogador == 'J'
#    jogador +=  10