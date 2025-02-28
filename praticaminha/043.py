for n in range(1,6):
    print(f'Tabudade de {n}:\n{'=' * 20}')
    for t in range(1,11):
        produto = n * t
        print(f'{n} x {t} = {produto}')
    print('=' * 20)
