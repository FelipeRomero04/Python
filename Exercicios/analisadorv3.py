from os import system 

system('cls')

maioridade = homem = mulher_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 0: #comecar pela possibilidade correta
                break
            print('Idade não permitida. Insira novamente!')
        except ValueError:
            print('Valor inválido. Tente novamente!')
    if idade >= 18:
        maioridade += 1
    while True:
        sexo = str(input('Sexo[F/M]: ')).strip().upper()
        if sexo in ('F', 'FEMININO', 'M', 'MASCULINO'):
            break
        print('Informacao Inválida!')
    print('-' * 20)
    if sexo in ('M', 'MASCULINO'):
        homem += 1
    if idade < 20 and sexo in ('F', 'FEMININO'):
        mulher_20 += 1

    opcao = ' '
    while opcao not in ('N', 'NAO','NÃO', 'S','SIM' ):
        opcao = str(input('Quer continuar[S/N]: ')).strip().upper()
    if opcao in ('N', 'NAO', 'NÃO'):
        break
        
print('=====FIM DO PROGRAMA=====\n')
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homem} {'homem' if homem == 1 else 'homens'} {'cadastrado' if homem == 1 else 'cadastrados'}\nE temos {mulher_20} {'mulher' if mulher_20 == 1 else 'mulheres'} com menos de 20 anos.')

    
    
    


#Use try para garantir que o valor de int seja um inteiro, evitar que seja um numero negativo, Use while ate que a resposta correta seja digitada
