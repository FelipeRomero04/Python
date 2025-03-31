
tasks = []
tasks_end = []

while True:
    print('Gerenciador de Tarefas')
    print('''
1. Adicionar Tarefas
2. Concluir Tarefas
3. Listar Tarefas
4. Remover Tarefas
''')

    while True:
        try:
            opcao = int(input('Digite uma das opções acima[ENTER p/]sair]: '))
            if opcao in (1, 2, 3, 4) or not opcao:
                break 
            print('Opção não encontrada.')
        except ValueError:
            print('Entrada incorreta')

    if opcao == 1:

        new_task = input('Adicione uma Tarefa: ')
        if new_task in tasks:
            print('Esta tarefa ja esta na sua lista!')
            continue
        tasks.append(new_task)
    
    if opcao == 2:
        completed = int(input('Digite o número da tarefa concluída: '))
        tasks_end.append(completed)

    if opcao == 3:
        print('Mostando a lista: ')
        for t, e in zip(tasks, tasks_end):
            if tasks[e] in tasks:
                print(f'[V] {t}')
                continue
            print(f'[ ] {t}')

    if opcao == 4:
        task_remove = int(input('Digite o número da tarefa: '))
        tasks.remove(tasks[task_remove])
        print('Tarefa Removida!')
    



#for c in task:
#
#
#
#
#
#