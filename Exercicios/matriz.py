matriz = []

for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz += str(n)
    print()

print(matriz)