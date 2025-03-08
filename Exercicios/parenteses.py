expr = str(input('Digite uma expressão: '))
pilha = []

for i in expr:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if pilha: #Se a pilha nao estiver vazia, elimina o ultimo item da lista
            pilha.pop()
        else:
            pilha.append(')')
            break
            
if not pilha: #Se a pilha estiver vazia, sua expressão esta correta
    print('Sua expressão esta correta')
else:
    print('Sua expressão está incorreta')


#Logica do programa(Equilibrio):

'''
O programa e validado baseado na quantidade de itens na lista, a cada '(' o item e adicionado, e a cada ')' esse item é removido. Assim, é preciso que a lista se mantenha vazia para que a expressão esteja correta.

O for percorre a expr, e a cada '(' ele é adcionado a lista pilha.
Caso a expr já comece com ')' ele irá passar para o elif e se tiver algo dentro da pilha(Não vai ter) ele é adicionado dentro da lista.

Tendo algo dentro da pilha, significa um parentes que nao foi aberto ou fechado, resultando na mensagem de erro

'''