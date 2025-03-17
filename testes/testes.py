# nomes = ['Carlos', 'Ana', 'Beatriz', 'Daniel']

# # Ordenar pelo tamanho das palavras
# ordenado = sorted(nomes, key=lambda nome: len(nome))
# print(ordenado)
# # ['Ana', 'Carlos', 'Daniel', 'Beatriz']

nomes = ['Ana', 'Carlos', 'Beatriz', 'Daniel']

# Ordenar pelos últimos caracteres do nome
ordenado = sorted(nomes, key=lambda x: x[-1])
print(ordenado)
# ['Beatriz', 'Carlos', 'Daniel', 'Ana']


