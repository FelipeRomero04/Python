from time import sleep
# from os import system

# system('cls')

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
    while True:
        new_task = input(f'Digite uma tarefa: ').strip().capitalize()
        if not new_task:
            break
        if any(l for l in new_task if l.isdigit()):
            print('Não são permitidos números nesse campo.')
            continue
        if new_task in tasks:
            print('Tarefa já incluída.')
        tasks.append({ #criando dict dentro da lista
            'tarefa': new_task, 
            'completa': False
        })
    print('Tarefas Adicionadas!')

def end_task(lista): #concluida
    for i, v in enumerate(lista.values()):
        print(i, v)


list_tasks = []
tasks = {i + 1: v for i, v in enumerate(list_tasks)} #ANOTAR

add_task()
end_task(tasks)
