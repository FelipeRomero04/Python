from random import randint

computador = randint(1, 10)
usuario = int(input('Adivinhe o número que o computador está pensando: '))
tentativa = 0


while True: 
    if computador == usuario:
        print(f'Eu pensei no número {computador} também! Você acertou!')
        print(f'--------//---------\nVocê errou {tentativa} vezes')
        exit()
    if computador != usuario:
        usuario = int(input('Você ERROU! Tente novamente: '))
        tentativa += 1
        if computador < usuario:
            print('O numero que eu pensei É MENOR\n----------//----------')
        if computador > usuario: 
            print('O número que eu pensei É MAIOR\n----------//---------')
        
            
# A FORMA ACIMA E ABAIXO SAO ORIGINAIS. IREI TENTAR UMA FORMA MAIS OTIMIZADA ULTILIZANDO O CODIGO DO CHATGPT COMO BASE NO 034.py


'''from random import randint

computador = randint(1, 50)
usuario = int(input('Adivinhe o número que o computador está pensando: '))
tentativa = 0

while True:
    for x in range(10):
        if computador == usuario:
            print(f'Eu pensei no número {computador} também! Você acertou!')
            print(f'--------//---------\nVocê errou {tentativa} vezes')
            exit()
        if computador != usuario and computador < usuario:
            print('O numero que eu pensei É MENOR\n----------//----------')
            usuario = int(input('Você ERROU! Tente novamente: '))
            tentativa += 1
        if computador != usuario and computador > usuario:
            print('O número que eu pensei É MAIOR\n----------//---------')
            usuario = int(input('Você ERROU! Tente novamente: '))
            tentativa += 1'''



# Gera um número aleatório entre 1 e 100
'''numero_secreto = random.randint(1, 100)

tentativas = 0
acertou = False

print("🎯 Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while not acertou:
    # Usuário faz um palpite
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1  # Conta mais uma tentativa
    
    # Verifica se o palpite é correto
    if palpite < numero_secreto:
        print("🔼 O número secreto é maior!")
    elif palpite > numero_secreto:
        print("🔽 O número secreto é menor!")
    else:
        acertou = True  # Sai do loop quando acertar

print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")'''



            
       
        