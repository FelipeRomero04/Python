# dados = [{'valor': 6} , {'valor': 7}, {'valor': 9}]

# for v in dados:
#     print(v['valor'])

# dados = [{'nome': 'felipe', 'idade': 18, 'cidade': 'Tr'}, {'nome': 'felipe', 'idade': 18, 'cidade': 'Tr'}]

# for v in dados:
#     print(v['nome'])



# a = '234'

# if len(a) <= 3:
#     print('sim')

# Correto
# tupla = (42, 32)
# x, = tupla  # x recebe o valor 42
# print(x)
# #E possivel atribuir um valor da tupla a uma variavel usando ,

# import time

# Lista
# inicio = time.time()
# for _ in range(1000000):
#     x = [1, 2, 3, 4, 5]
# fim = time.time()
# print("Lista:", fim - inicio)

# # Tupla
# inicio = time.time()
# for _ in range(1000000):
#     x = (1, 2, 3, 4, 5)
# fim = time.time()
# print("Tupla:", fim - inicio)

# livro1 = ("1984", "George Orwell", 1949)
# livro2 = ("Dom Casmurro", "Machado de Assis", 1899)

# biblioteca = [livro1, livro2]

# for livro in biblioteca:
#     print(livro)
    # titulo, autor, ano = livro
    # print(f"{titulo} de {autor}, publicado em {ano}")

# tupla = ()

# for i in range(5):
#     tupla += i,
#     print(tupla)

# livro1 = ('1984', 'George Orwell', 2001)
# titulo, autor, ano = livro1

# print(f'O titulo é {titulo}, o autor se chama {autor}, foi lançado no ano de {ano}')

# lista = [{'nome': 'Felipe', 'idade': 18, 'cidade': 'Tr'}, {'nome': 'Felipe', 'idade': 28, 'cidade': 'Tr'}, {'nome': 'Felipe', 'idade': 48, 'cidade': 'Tr'}]


# lista = {'nome': 'Felipe'}

# cont = (t for t in lista.items())

# print(cont)

# for n in lista.values():
#     for l in n:
#         print(l)


# lista1 = [1, 3, 5, 2, 6]
# lista2 = [ 3, 4, 5, 2]

# correto = filter(lambda n: n in lista1, lista2)

# print(list(correto))


# lista = ["a", "b", "c"]
# dict_lista = {i+1: v for i, v in enumerate(lista)}

# print(dict_lista) 


# dict = [{'tarefa': 'cagar', 'status' : 'caguei'}, {'tarefa': 'sla', 'status' : 'tbmnsei' }] 

# # for t in dict:
# #     for v in t.items():
#         if v[0] == 'status':
#             continue
#         print(v[1]) #ANOTAR Q QUANDO DICT E PERCORRIDO COM .ITEMS(), OS VALORES SE TORNAM TUPLAS, PODENDO SER MANIPULADAS PELO INDÍCE. (PELO MENOS QND E UMA LISTA DE DIC, TESTA DICT NORMAL)


# dict = [{'tarefa': 'cagar', 'status' : 'caguei'}, {'tarefa': 'sla', 'status' : 'tbmnsei' }] 

# dict[0]['status'] = 'Sim'

# print(dict)

# for i , t in enumerate(dict):
#     for k, v in t.items():
#         print(v['tarefa'])

import tkinter as tk

# def esperar_com_after():
#     label.config(text="Esperando 3 segundos...")
#     root.after(3000, lambda: label.config(text="Pronto!"))  # NÃO trava

root = tk.Tk()

root.geometry('300x300')

for i in range(3):
    botao = tk.Button(root, text=f"Botão {i}", command=lambda:print(i))
    botao.pack()

# root.geometry("300x150")

# label = tk.Label(root, text="Clique no botão", font=("Arial", 12))
# label.pack(pady=10)

# botao = tk.Button(root, text="Usar after()", command=esperar_com_after)
# botao.pack()

root.mainloop()

