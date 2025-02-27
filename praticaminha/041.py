f1 = 0
f2 = 1
total = ''

for i in range(0,15):
    total += f1
    print(f'{total},', end='')
    f1 += f2
    f2 = total
