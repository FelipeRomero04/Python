tasks = []
num_tasks_end = []

while True:
    print('Gerenciador de Tarefas')
    print('''1. Adicionar Tarefas
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
        num_tasks_end.append(completed)

    if opcao == 3:
        print('Mostando a lista: ')
        max_len = max(len(tasks), len(num_tasks_end))

        for i in range(max_len):
            if i in num_tasks_end:
                print(f'{i}. [v]{tasks[i]}')
                continue
            print(f'{i}. [ ]{tasks[i]}')
        

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



 # for i in range(max_len):
        #     for n in num_tasks_end:
        #         if tasks[i] == tasks[n]:
        #             print(f'[ V ] {tasks[i]}')
        #             continue
        #         print(f'[ ] {tasks[i]}')

# for t, n in zip(tasks, num_tasks_end):
        #     if tasks[n]:
        #         print(f'[V] {t}')
        #     else:
        #         print(f'[ ] {t}')