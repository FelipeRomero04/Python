from os import system 

system('cls')

maioridade = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = str(input('Sexo[F/M]: ')).strip().upper()
    if sexo in ('M', 'MASCULINO'):
        

    opcao = str(input('Quer continuar[S/N]: ')).strip().upper()
    if opcao in ('N', 'NAO', 'NÃO'):
        break


#Use try para garantir que o valor de int seja um inteiro, evitar que seja um numero negativo, Use while ate que a resposta correta seja digitada
