idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Você é uma criança')

elif idade < 18:
    print('Você é um adolescente')

elif idade < 65:
    print('Você é um adulto')

else:
    print('Você é um idoso')

'''elif é essencial para que não ocorra o erro de duas condições acabarem sendo verdadeiras. exemplo:

idade = 13
if idade < 18:
    adolescente
if idade < 65:
    adulto

13 e menor que 18, logo seria adolescente, no entanto, também é menor que 65. fazendo com que as duas sentenças sejam verdadeiras, mostrando no terminal dois valores. o que não seria o desejado.
'''