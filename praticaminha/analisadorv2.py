lista = []

for info in range(1,4):
    print(f'-------{info}ª PESSOA-------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    lista.append(idade)

media = sum(lista) / len(lista)

print(f'A media da idade das pessoas é de {media:.2f}')
print(f'O homem mais velho tem {max(lista)} anos. ')
