pal1 = str(input('Digite uma palavra: ')).lower()
pal2 = str(input('Digite uma palavra: ')).lower()

if pal1 == pal2:
    print('As palavras são iguais.')

elif pal1 != pal2 and len(pal1) == len(pal2):
    print('As palavras são diferentes, mas possuem o mesmo comprimento.')

elif pal1 != pal2 and len(pal1) != len(pal2):
    print('São palavras diferentes, com comprimentos diferentes.')