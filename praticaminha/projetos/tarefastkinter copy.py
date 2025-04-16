from time import sleep
from os import system
from tkinter import * 


system('cls')

def menu():
    print('=== Gerenciador de Tarefas ===')
    print('''
    1. Adicionar Tarefas
    2. Concluir Tarefa
    3. Editar Tarefa
    4. Listar Tarefas
    5. Remover Tarefas
    6. Sair
    ''')

# def add_task(lista_tarefas):
#     print('=-' * 20)
#     print('ENTER P/ VOLTAR AO MENU.')
#     print('=-' * 20)

#     tarefas_adicionadas = 0

#     while True:
#         task = input(f'Digite a {len(lista_tarefas) + 1}ª tarefa: ').strip().capitalize()
#         if not task:
#             break
        
#         if any(l for l in task if l.isdigit()):
#             print('Não são permitidos números nesse campo.')
#             continue    
#         if task in tasks:
#             print(f'Tarefa já incluida à lista.')
#             continue  
#         tasks.append(task)
#         tarefas_adicionadas += 1

#     if tarefas_adicionadas == 0:
#         print('Nada foi adicionado à lista.')
#         return
  
#     print('Tarefas adicionadas a lista.')

# def edit_task(lista):
#     while True:
#         try: 
#             num_edit = input('Nº da tarefa à ser editada: ').strip()
#             if not num_edit:
#                 return
#             if not any(l for l in num_edit if l.isdigit()):
#                 print('Somente número são permitidos nesse campo.')
            
#             num_edit = int(num_edit) - 1

#             if 0 > num_edit > len(lista):
#                 print('Essa tarefa não existe')
#                 continue
#             break
#         except ValueError:
#             print('Valor Inválido. Preencha o campo corretanente!')
        
#     while True:
#         if lista[num_edit]:
#             new_task = input('Digite a nova tarefa: ').strip()
#             if not new_task:
#                 print('Nenhuma Tarefa foi editada.')
#                 return
#             lista[num_edit] = new_task
#             print('Tarefa editada com sucesso!')
#             break
#         else:
#             print('Essa Tarefa não esta presente na lista.')


# def complete_task(lista): #concluida
#     show_tasks(tasks, num_tasks_end)    
#     while True:
#         if not lista:
#             return
#         try:
#             completed = input('Nº da tarefa à concluir: ').strip()
#             if not completed:
#                 return
#             completed = int(completed) - 1
#             if  0 > completed > len(lista):
#                 print('Essa Tarefa não existe.')
#                 continue

#         except ValueError:
#             print('O campo foi preenchido com valores inválidos.')    
#             continue

#         print('Tarefa concluida!')
#         num_tasks_end.append(completed)
#         break

# def show_tasks(lista1, lista2):
#     print('~' * 30)
#     print('Mostrando a lista: ')

#     for i in range(len(lista1)):
#         if i in lista2:
#             print(f'{i + 1}. [v]{lista1[i]}')
#             continue
#         print(f'{i + 1}. [ ]{lista1[i]}')    

#     if not lista1:
#         print('Sua Lista de Tarefas está vazia!')
#     print('~' * 30)
#     sleep(2)
    

# def remove_task(lista_tarefas, num_tarefas_concluidas):
#     show_tasks(tasks, num_tasks_end)
#     while True:
#         try:
#             num_excluir = input('Número da Tarefa à ser removida[ENTER P/SAIR ]: ').strip()
#             if not num_excluir:
#                 return
#             num_excluir = int(num_excluir) - 1
#             if 0 > num_excluir > len(lista_tarefas):
#                 print('Essa Tarefa não existe')
#                 continue
#         except ValueError:
#             print('Somente números são permitidos nesse campo.')
#             continue

#         print('Tarefa Removida!')
#         lista_tarefas.pop(num_excluir)

#         if num_excluir in num_tarefas_concluidas: 
#             num_tarefas_concluidas.remove(num_excluir)#Remove o numero dentro de tarefas concluidas
#         break




# while True:
#     menu()
#     while True:
#         try:
#             opcao = int(input('Selecione uma das opções acima: '))
#             if 0 < opcao < 6:
#                 break
#             print('Entrada inválida. Tente novamente.')
#         except ValueError:
#             print('Digite o Nº das opções acima! ')

#     if opcao == 1:
#        add_task(tasks) 
#     if opcao == 2:
#         complete_task(tasks)
#     if opcao == 3:
#         edit_task(tasks)
#     if opcao == 4:
#         show_tasks(tasks, num_tasks_end)
#     if opcao == 5:
#         remove_task(tasks, num_tasks_end)
#     if opcao == 6:
#         opcao = input('ENTER P/SAIR')
#         if not opcao:
#             print('FINALIZANDO A LISTA...')
#             sleep(0.5)
#             break
#         continue

from time import sleep

def add_task():
    repeat_task['text'] = ''
    valor = digit_task.get()
    if not valor:
        repeat_task['text'] = 'Nenhuma Tarefa foi adicionada.'
        return
    if valor in tasks:
        repeat_task['text'] = 'Tarefa já incluida na lista'
        return
    if valor.isdigit():
        repeat_task['text'] = 'Não são permitidos apenas números nesse campo.'
        return
    tasks.append(valor)

    def show_task(lista):  #Criando um Label para cada item adicionado ao chamar a função add_task
        for i in range(len(lista)):   
            button_remove(i)

            global is_pressed
            is_pressed = False

            remove_task = Button(retangulo_menor, text='X', bg='red', font=('Arial', 10), fg='white', command=lambda i=i: pressionar(i)) #Ler sobe 'congelar' a var no chatgpt
            remove_task.place(relx=0.90, y=11*i*2.1, relwidth=0.06, relheight=0.09)

    show_task(tasks)

def button_remove(indice):
    label_tasks = Label(retangulo_menor, bg='#1e2b30', text=f'{tasks[indice]}', fg='white', font=('Arial', 10), anchor='nw', highlightbackground='#1a1f22',highlightthickness=0.8 )
    label_tasks.place(x=1, y=11*indice*2.1, relwidth=0.46)
    list_label.append(label_tasks)

#IMPORTANTE
#Botar o codigo dos botões dentro de um loop
           

#Pra cada Label um botão de apagar e criado, então talvez não seja preciso se referenciar ao label especifico ao apaga-lo


def pressionar(indice):
    print(indice)
    list_label[indice].destroy()
    tasks.pop(indice)
    print(tasks)








          
    



  # 
            # remove_task.place(relx=0.90, y=11*i*2.1, relwidth=0.06, relheight=0.09)
            # remove_task.bind('<ButtonPress-1>', removed_task)
            # if is_pressed:
            #    
# def removed_task(lista):
#     for i in range(len(lista)):
#         remove_task = Button(retangulo_menor, text='X', bg='red', font=('Arial', 10), fg='white')
#         
    
#     is_pressed = True
#     print(is_pressed)
    



    

#O label reconhece diferentes valores da lista pelo 'i' do for, logo para excluir um elemento deve se usar a mesma lógica
            


# for dentro para usar o valor do i para remover o widget

tasks = []
num_tasks_end = []   
list_label = []        
       
#O Label so suporta um texto, logo não mostra todas iterações de um loop, somente o atual. Devo criar um Label para cada tarefa adicionada?

#janela principal

janela = Tk()
janela.title('Lista de Tarefas')
janela.config(background='#253034')
janela.geometry('1440x900')
janela.minsize(width=720, height=405) #Aumentar dps
janela.resizable(True, True) #largura e altura responsivos

#Retangulo
retangulo = Frame(janela, background='#2e3a3f', highlightbackground='#1c2429', highlightthickness=1)
retangulo.place(relx=0.2 , rely=0.24, relwidth=0.6 , relheight=0.5 ) #rel torna as proporções responsivas

#Entrada
digit_task = Entry(retangulo, background='white')
digit_task.place(relx=0.13, rely=0.24, relwidth=0.7, relheight=0.07)

#Adicionar
adic_task = Button(retangulo, command=add_task,text='Adicionar',fg='white',background='#1e2a2e',relief='flat')
adic_task.place(relx=0.84, rely=0.24, relwidth=0.1, relheight=0.07)

#texto se o valor for repetido
repeat_task = Label(retangulo, text='', background='#2e3a3f', font=('Roboto', 10), fg='white', anchor='nw')
#anchor = ancora o texto e uma pos especifica da caixa d/Label
repeat_task.place(relx=0.13 , rely=0.33, relwidth=0.6, relheight=0.06 )

#Retangulo menor para lista de tarefas
retangulo_menor = Frame(retangulo, background='#1c2429', highlightbackground='#1a1f22', highlightthickness=1)
retangulo_menor.place(relx=0.25 , rely=0.4 , relwidth=0.5 , relheight=0.58 )




janela.mainloop()


#Uma variavel pra cada Label
#Como foi feito no exemplo da cotação0




#Criar um label dentro do retangulo menor, Mostrando a lista, assim que o botão 'Adicionar' foi disparado(COMO? FUDEU)





#Cores

#2e3a3f - Cor do traingulo interno







#Retangulo

# campo = Frame(janela, bg='#2a3439', width=600, height=350)
# campo.pack(padx=20)


# # canvas = Canvas(janela, width=600, height=350, bg='#2a3439')
# # canvas.create_rectangle(0, 0, 500, 300, outline='#2a3439')
# # canvas.grid(column=5, row=10, pady=145)


# #Campo pra escrever a tarefa

# digit_task = Entry(janela, bg='white', width=40)
# digit_task.insert(0,'')
# digit_task.pack()

# #Criando botão adicionar
# add_button = Button(janela, text='Adicionar', bg='#253034', fg='white', relief='groove')
# add_button.pack(padx=30)


