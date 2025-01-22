t = int(input('Digite o número para ver sua tabuada: '))

for c in range(1, 11):
    r = t * c
    print(f'{t} X {c:^2} = {r}')
