
tasks = []

while True:
    print('Gerenciador de Tarefas')
    print('''
1. Adicionar Tarefas
2. Concluir Tarefas
3. Listar Tarefas
4. Remover Tarefas
''')

    opcao = input('Digite uma das opções acima[ENTER p/]sair]: ')
    if not opcao:
        break

    opcao = int(opcao)

    if opcao == 1:
        new_task = input('Adicione uma Tarefa: ')
        if new_task in tasks:
            print('Esta tarefa ja esta na sua lista!')
            continue
        tasks.append(new_task)
    
    if opcao == 2:
        task_end = int(input('Digite o número da tarefa     concluída: '))

    if opcao == 4:
        task_remove = input('Digite o número da tarefa: ')
        tasks.remove(tasks[task_remove])
    
    if opc



    print(tasks)