km = int(input('Qual é a velocidade tua do carro? '))
#(80 - var(km)) * 7

if km > 80:
    print(f'MULTADO! Você excedeu o limete que é de 80Km/h\nVocê deve pagar uma multa de R${(km - 80) * 7:.2f}')
    print('PRESTE MAIS ATENÇÃO! ISSO PODE CAUSAR UM ACIDENTE!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
