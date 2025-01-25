palavra = str(input('Digite uma palavra: '))
vogais = 'aeiouAEIOU'
estrela = ''

for i in range(len(palavra)): #analisa cada letra invidualmente
    if palavra[i] in vogais:
        estrela += '*' 
    
    else:
        estrela += palavra[i]

print(estrela)


