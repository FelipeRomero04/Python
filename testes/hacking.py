

def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")

dados = {'nome': 'Fernando', 'idade': 21}


# Equivale a: apresentar(nome='Fernando', idade=21)


lista = [1, 2, 4, 2]
item1, item2 = 4 , 1

for x in (item1, item2):
    print(x)

# for i in range(len(lista), 2):
#     print(i)

    #  for i in range(0, len(hand), 2):
    #     num_par.append(hand[i])

    # media_par = sum(num_par) / len(num_par)


lista = [["Charles", 90], ["Tony", 80], ["Alex", 100], ["Alex", 100]]

# for x in lista:
#     print(x)


letra = '324'
tupla = []

tupla.extend(letra)

print(tupla)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return tuple(azara_record[2]) == rui_record[1]


dicionario = {'nome': 'Felipe'}

dict = {'madeira': 1, 'Ferro': 4}
adicionar = {'madeira' : 4}



tupla = [valor for valor in range(5)]
print(tupla)  # (0, 1, 2, 3, 4)