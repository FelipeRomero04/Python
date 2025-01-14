nt1 = float(input('Primera nota: '))
nt2 = float(input('Segunda nota: '))
m = (nt1 + nt2) / 2

if m >= 7:
    print(f'Tirando {nt1} e {nt2}, a média do aluno é {m}')
    print('O aluno está APROVADO!')

elif m >= 5 and m< 7: # ou 7 < media >= 5:
    print(f'Tirando {nt1} e {nt2}, a média do aluno é {m}')
    print('O aluno está de RECUPERAÇÂO!')

elif m < 5:
    print(f'Tirando a média de {nt1} e {nt2}, a média do aluno é {m}')
    print('O aluno está REPROVADO!')
