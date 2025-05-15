
dados = {'nome': 'Felipe', 'Idade': 18}

dados2 = dados.setdefault('nome', 'Romero')
#Retorna o valor se a chave for encontrada!

#Caso não for encontrada, irá retornar o valor colocado em <default value> e inserido no dict. Caso o <default value> não seja definido, somente a key, o valor None será inserido junto a key ao dicionário


# print(dados2)


#


new_dict.fromkeys(['branco', 'preto', 'marrom', 'azul', 'roxo'], 'sexo')
# print(new_dict)

#Forma de criar um dicionario de rapidamente usando um iteravel e um valor fixo

#

dados1 = {'nome' : 'José', 'idade': 100, 'sexo': 'Trans'}
dados2 = {'email': 'joseperera@teste.com', 'endereco': 'Debaixo da ponte'}

dados_completos = dados1 | dados2

#print(dados_completos)

#Union - Cria um novo dict concatenando dois dicionarios 

#
 
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9}

set1 |= set2

print(set1)


#Operador de Union com atribuição. Não tem necessidade de criar um novo dict. Tem as mesmas regras que o operador de Union normal(chaves repetidas, o dict a ser unido(o da direta da |) o valor precede o valor do dict original)

#Ao fazer a união com atribuição o dict principal(a esquerda) e tem o valor substituido pelo valor concatenado dos dois dict)