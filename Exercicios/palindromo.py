frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letras in range(len(junto) - 1, -1, -1): #Parametro pra inverter as letras

# Para pegar a ultima palavra tem de usar len, como len faz a contagem a partir do UM, mas a numeração de caracteres do python do ZERO, para selecionar o ultimo caractere é necessario subtrair - 1.
    inverso += junto[letras]

# Acumuluando as letras invetidas na var 'inverso', formando uma string invertida.

print(f'A Palavra {junto} invertida é {inverso}')
if junto == inverso:
    print('São iguais, logo é um palindromo.')
else:
    print('São diferentes, logo não é um palindromo')
