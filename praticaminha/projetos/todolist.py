def ad_tarefa(lista):
    
    name_task = input('Adicione uma tarefa: ')
    if name_task in lista:
        print('Essa tarefa já esta na lista')
    tasks.append(name_task)
    return name_task

def task_end():
    
    show_tasks(tasks)
    escolha = input('Número da tarefa concluida: ')
    return escolha

def show_tasks(lista):
    
    for i, v in enumerate(lista, start=1):
        if i == task_end():
            print(f'{i}. [V] {v}')
        else:
            print(f'{i}. [ ] {v}')

tasks = []

while True:
    print('Gerenciador de Tarefas')

    print('''
    1. Adicionar Tarefas 
    2. Concluir Tarefas
    3. Listar Tarefas
    4. Remover Tarefas
    ''')

    opcao = input('Selecione uma das opções acima[ENTER p/sair]: ')
    if not opcao:
        break
    opcao = int(opcao)
    if opcao == 1:
        ad_tarefa(tasks)
    if opcao == 2:
        task_end()
    if opcao == 3:
        show_tasks(tasks)

