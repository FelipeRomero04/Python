# lista = [4, 5, 2, 5, 2, 4]

# pares = list(filter(lambda x: x % 2 == 0, lista))

# print(pares)


valores = [None, "Python", "", "Código", None, " ", "Filter"]

nao_vazios = filter(lambda v: v and v.strip(), valores)

print(list(nao_vazios))  # Saída: ['Python', 'Código', 'Filter']
    