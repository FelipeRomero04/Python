import random
from os import system
from time import sleep

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
    print(f'Total: {valor_jogador}')
    print(f'Carta visível do Dealer [{pc[0]['naipe']}]')
    print('=' * 40)
    
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
    print('=' * 40)

    escolha_pc = random.randint(1,2)
    
    if escolha_pc == 1 and valor_pc > 16:
        escolha_pc = 2

    possibilidade = random.randint(10,15)

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
    
    

    if escolha == 1:
        newcard_jg = comprar_cartasjg() #permanecer o valor fora da função
        valor_jogador += newcard_jg[1]
        print(f'Voce comprou: [{newcard_jg[0]}]')
        sleep(1)
        while True:
            try:
                opcao = int(input('(1)Pedir mais uma carta | (2)Parar: '))
                if opcao == 1:
                    newcard_jg = comprar_cartasjg()
                    print(f'Você comprou: [{newcard_jg[0]}]')
                if opcao == 2:
                    break
                valor_jogador += newcard_jg[1]

            except ValueError:
                print('Entrada Inválida.')

        print('Suas cartas: ')
        for cartas in jogador:
            print(f'[{cartas['naipe']}]',end=' ') #Mostra todas cartas dentro da lista(somente o naipe)
        print(f'Total: {valor_jogador}')
        print('=' * 40)
        sleep(1.5)
        if valor_jogador == 21:
            print(f'Jogador Ganhou!')
            break
        elif valor_jogador > 21:  
            print('O Jogador ESTOROU!\n======= O Dealer Venceu! =======')
            break

        if escolha_pc == 1:
            newcard_pc = comprar_cartaspc()  #carta é removida do baralho
            valor_pc += newcard_pc[1]
            print('Dealer resolveu comprar! Ele revelou suas cartas:')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}')
            if valor_pc > 21:
                print('O Dealer ESTOROU! Jogador vencedor') 
                break
            elif valor_pc > valor_jogador:
                print('O Dealer Ganhou!')
            elif valor_pc < valor_jogador:
                print('O jogador Ganhou!')
            else:
                print('Empate')
    
        if escolha_pc == 2:
            print('O Dealer resolveu parar!')
            print(f'Dealer revela suas cartas: ')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}')
            print('=' * 40)
            if valor_pc > valor_jogador:
                print('O DEALER GANHOU!')
            elif valor_pc < valor_jogador:
                print('O JOGADOR GANHOU!')
            elif valor_jogador == valor_pc:
                print('Empataram')
        break

    if escolha == 2: # Mostrar naipe segunda [] sempre 0               
       
         #NESSA OPCAO O JOGADOR PARA, LOGO SOMENTE O DEALER TEM A OPCAO DE PARAR TBM OU CONTINUAR
        if escolha_pc == 1: #dealer compra
            newcard_pc = comprar_cartaspc()  #remove a carta do baralho pra não ter repetições
            print(f'Dealer compra mais uma carta: [{newcard_pc[0]}]')  
            valor_pc += newcard_pc[1]
            sleep(1)
            print('Dealer revela suas cartas: ')
            for cartas in pc:
                print(f'[{cartas['naipe']}]',end=' ')
            print(f'Total: {valor_pc}')
            print('=' * 40)
    
            if valor_pc > 21:
                print('O Dealer ESTOROU!\n========= Você Ganhou ===========')
            elif valor_pc <= 21 and valor_pc < valor_jogador:
                print(f'O Jogador GANHOU!\njogador {valor_jogador} X {valor_pc} Dealer\n')
            elif valor_pc <= 21 and valor_pc > valor_jogador:
                print(f'======== O Dealer Venceu! =======\n\nDealer {valor_pc} X {valor_jogador} Jogador2\n ')
            break
            
        if escolha_pc == 2: #Situação em que o dealer para
            print('Dealer resolveu parar!')
            sleep(1)
            print('Dealer revela suas cartas: ')
            for c in pc:
                print(f'[{c['naipe']}]', end=' ')
            print(f'Total: {valor_pc}')
            print('='*40)
            print('Suas cartas: ')
            for c in jogador:
                print(f'[{c['naipe']}]', end=' ') 
            print(f'Total: {valor_jogador}')
            sleep(2)  
            if valor_pc > valor_jogador:
                print(f'\nO Dealer GANHOU!\nDEALER {valor_pc} X {valor_jogador} JOGADOR\n')
            elif valor_pc < valor_jogador:
                print(f'\nO Jogador GANHOU!\n{'=' * 40}\nJOGADOR {valor_jogador} X {valor_pc} DEALER\n')
            else:
                print(f'\nEMPATE!!\n\JOGADOR {valor_jogador} X {valor_pc} DEALER\n')
            break