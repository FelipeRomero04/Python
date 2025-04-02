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
    print('=-' * 30)
    new_task = input('Digite uma tarefa: ').strip().capitalize()
    if new_task in tasks:
        print('Tarefa ja incluida!')
        return
    tasks.append(new_task)
    print('Tarefa adiciona a lista.')

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
    max_len = max(len(lista1), len(lista2))
    for i in range(max_len):
        if i in lista2:
            print(f'{i}. [v]{lista1[i]}')
            continue
        print(f'{i}. [ ]{lista1[i]}')    
    if not lista1:
        print('Sua Lista de Tarefas está vazia!')
    print('~' * 30)
    menu()

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


menu()

while True:
    print('=-' * 30)
    opcao = input('Selecione uma das opções acima: ')
    opcao = int(opcao)
    
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

#Tratar ValueError e finalizações(deixa bunitin)

#Ver onde posso chamar o menu novamente

