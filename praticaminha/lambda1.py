'''preco = [100, 500, 10, 25] 

for i in preco:
    imposto = lambda x: x * 0.3
    print(imposto(i), end='')'''

# Ouuuu usando a funçao map

preco = [100, 500, 10, 25]

imposto = list(map(lambda x: x * 0.3 , preco))

print(imposto)

#map: pega cada item de uma lista(ou qlqr iteravel) e aplica a função(ou outra estrutura) q esta armazenada dentro para cada item
#Quando precisar executar uma função para cada item de uma lista USE MAP 

#map(funcao, lista)

#É NECESSARIO ESPECIFICAR O ITERAVEL(LIST,TUPLE,SET) PARA EXIBIR, ANTES DE USAR MAP OU ANTES DE PRINTAR A VARIAVEL
