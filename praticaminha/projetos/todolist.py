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

def add_task(lista_tarefas):
    print('=-' * 20)
    print('ENTER P/ VOLTAR AO MENU.')
    print('=-' * 20)

    tarefas_adicionadas = 0

    while True:
        new_task = input(f'Digite a {len(lista_tarefas) + 1}ª tarefa: ').strip().capitalize()
        if not new_task:
            break
        
        if any(l for l in new_task if l.isdigit()):
            print('Não são permitidos números nesse campo.')
            continue    
        if new_task in tasks:
            print(f'Tarefa já incluida à lista.')
            continue  
        tasks.append(new_task)
        tarefas_adicionadas += 1

    if tarefas_adicionadas == 0:
        print('Nada foi adicionado à lista.')
        return
  
    print('Tarefas adicionadas a lista.')

def complete_task(lista): #concluida
    show_tasks(tasks, num_tasks_end)    
    while True:
        if not lista:
            return
        try:
            completed = input('Nº da tarefa à concluir: ').strip()
            if not completed:
                return
            completed = int(completed)
            if  0 > completed > len(lista):
                print('Essa Tarefa não existe.')
                continue

        except ValueError:
            print('O campo foi preenchido com valores inválidos.')    
            continue

        if not num_tasks_end:
            print('Essa Tarefa não existe')
            continue

        print('Tarefa concluida!')
        num_tasks_end.append(completed)
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
    

def remove_task(lista_tarefas, num_tarefas_concluidas):
    show_tasks(tasks, num_tasks_end)
    while True:
        try:
            num_excluir = input('Número da Tarefa à ser removida[ENTER P/SAIR ]: ').strip()
            if not num_excluir:
                return
            num_excluir = int(num_excluir)
            if 0 > num_excluir > len(lista_tarefas):
                print('Essa Tarefa não existe')
                continue
        except ValueError:
            print('Somente números são permitidos nesse campo.')
            continue

        print('Tarefa Removida!')
        lista_tarefas.pop(num_excluir)

        if num_excluir in num_tarefas_concluidas: #
            num_tarefas_concluidas.remove(num_excluir)#Remove o numero dentro de tarefas concluidas
        break

tasks = []
num_tasks_end = []

while True:
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
       add_task(tasks) 
    if opcao == 2:
        complete_task(tasks)
    if opcao == 3:
        show_tasks(tasks, num_tasks_end)    
    if opcao == 4:
        remove_task(tasks, num_tasks_end)
    if opcao == 5:
        opcao = input('ENTER P/SAIR')
        if not opcao:
            print('FINALIZANDO A LISTA...')
            sleep(0.5)
            break
        continue




