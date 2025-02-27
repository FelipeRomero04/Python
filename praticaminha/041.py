from os import system

system('cls')

f1 = 0
f2 = 1
total = 0

for i in range(0,15):
    total = f1
    if i == 14:
        print(f'{total} ', end='')
    else:
        print(f'{total}, ', end='')

    f1 = f2
    f2 = total + f1
