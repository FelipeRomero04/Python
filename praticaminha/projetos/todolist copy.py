from time import sleep
from os import system

system('cls')

def menu():
    print('=== Gerenciador de Tarefas ===')
    print('''
    1. Adicionar Tarefas
    2. Concluir Tarefas
    3. Listar Tarefas
    4. Remover Tarefas
    5. Sair
    ''')

def add_task():
    print('=-' * 20)
    print('ENTER P/ VOLTAR AO MENU.')
    print('=-' * 20)
    
    while True:
        new_task = input(f'Digite a {len(tasks) + 1}ª tarefa: ').strip().capitalize()
        if not new_task:
            break
        if any(l for l in new_task if l.isdigit()):
            print('Não são permitidos números nesse campo.')
            continue    
        if new_task in tasks:
            print(f'Tarefa já incluida à lista.')
            continue  
        tasks.append(new_task)
    print('Tarefas adicionadas a lista.')

def end_task(lista): #concluida
    show_tasks(tasks, num_tasks_end)    
    while True:
        completed = int(input('Nº da tarefa à concluir: '))

        for i in range(len(lista)):
            if completed != i:
                continue
            print('Tarefa concluida!')
            num_tasks_end.append(completed)
            break

        if not num_tasks_end:
            print('Essa Tarefa não existe')
            continue
        break

def show_tasks(lista1, lista2):
    print('~' * 30)
    print('Mostrando a lista: ')
    for i in range(len(lista1)):
        if i in lista2:
            print(f'{i}. [v]{lista1[i]}')
            continue
        print(f'{i}. [ ]{lista1[i]}')    
    if not lista1:
        print('Sua Lista de Tarefas está vazia!')
    print('~' * 30)
    sleep(2)
    

def remove_task(lista):
    show_tasks(tasks, num_tasks_end)
    while True:
        try:
            excluir = int(input('Número da Tarefa à ser removida: '))
            if 0 > excluir > len(lista):
                print('Essa Tarefa não existe')
                continue
        except ValueError:
            print('Somente números são permitidos nesse campo.')
        for i in range(len(lista)):
            if i != excluir:
                continue
        print('Tarefa Removida!')
        tasks.remove(tasks[excluir])
        break

tasks = []
num_tasks_end = []

while True:
    print('=-' * 30)
    menu()
    while True:
        try:
            opcao = int(input('Selecione uma das opções acima: '))
            if 0 < opcao < 6:
                break
            print('Entrada inválida. Tente novamente.')
        except ValueError:
            print('Digite o Nº das opções acima! ')

    if opcao == 1:
       add_task() 
    if opcao == 2:
        end_task(tasks)
    if opcao == 3:
        show_tasks(tasks, num_tasks_end)    
    if opcao == 4:
        remove_task(tasks)
    if opcao == 5:
        opcao = input('ENTER P/SAIR: ')
        if not opcao:
            break
        continue



