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
