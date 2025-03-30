def ad_tarefa(lista):
    if opcao == '1':
        name_task = input('Adicione uma tarefa: ')
        if name_task in lista:
            print('Essa tarefa já esta na lista')
    tasks.append(name_task)


tasks = []

while True:
    print('Gerenciador de Tarefas')

    print('''
    1. Adicionar Tarefas 
    2. Listar Tarefas
    3. Remover Tarefas
    4. Concluir Tarefas
    ''')

    opcao = input('Selecione uma das opções acima[ENTER p/sair]: ')
    if not opcao:
        exit()

    

    ad_tarefa(tasks)

    print(tasks)
