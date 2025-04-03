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

def add_task(): #Tentar polir mais
    while True:
        tasks = {'tarefa': input('Digite uma tarefa: ')}
        
        if not tasks['tarefa']:
            break
        if any(l for v in tasks.values() for l in v if l.isdigit()):
            print('Não são permitidos números nesse campo.')
            continue

        copy = False
        for t in list_tasks:
            for v in t.items():
                if v[0] == 'status':
                    continue 
                if tasks['tarefa'] in v[1]:
                    print('Tarefa já incluída.')
                    copy = True
                    break
        if copy:
            continue

        tasks['status'] = False
        list_tasks.append(tasks)
    print('Tarefas Adicionadas!')
    print(list_tasks)


def end_task(lista, lista2): #concluida
    
    completed = input('Nº da tarefa à concluir: ')
    lista2.append(completed)
    for i, t in enumerate(lista):
        for k, v in t.items():
            if k == 'status' and v 
            if v[0] == 'status' and i in coi          
            print()
         
        
        print(v)
    #if completed #for igual ao numero do dict, status = True

def show_tasks(lista):
    print('~' * 30)
    print('Mostando à lista: ')
    

list_tasks = []
list_end_tasks = []

add_task()
end_task(list_tasks, list_end_tasks)
# end_task(tasks)
