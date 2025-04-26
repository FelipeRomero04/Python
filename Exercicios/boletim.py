from time import sleep

dados = []
media = []

while True:
    nome = input('Nome: ')
    if any(num for num in nome if num in ('1','2','3','4','5','6','7','8','9','0')):
        print('Nome Invalido')
        continue
    while True:
        try:
            nt1 = float(input('Nota 1: '))
            nt2 = float(input('Nota 2: '))
            if nt1 > 0 and nt2 > 0:
                break
            print('Valor Inválido! Digite Novamente...')
        except ValueError:
            print('Entrada não norrespondente! Tente Novamente...')

    dados.append([nome, nt1, nt2])

    ntgeral = (nt1 + nt2) / 2
    media.append(ntgeral)

    while True:
        opcao = input('Quer continuar[S/N]: ').upper().strip()
        if opcao in ('S', 'SIM', 'NAO', 'NÃO', 'N'):
            break
    if opcao in ('N', 'NAO', 'NÃO'):
        break

print(f'{'No.':<5}{'Nome':<15}{'MÉDIA'}')

print('==' * 20)
for i, n in enumerate(media):
    print(f'{i:<5}{dados[i][0]:<15}{media[i]}')
print('==' * 20)

while True:
    aluno = input('Mostrar notas de qual aluno? [ENTER p/sair]: ')

    if not aluno:
        break

    aluno = int(aluno)
    print(f'Notas de {dados[aluno][0]} são: {dados[aluno][1:]}')
    print('==' * 30)

sleep(0.5)
print('FINALIZANDO...')
print('<< VOLTE SEMPRE >>')
    

#ANOTAR A LISTA INTERNA DE NOTAS E COMO ELA FUNCIONA



