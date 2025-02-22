import random

baralho = [('copas', 10), ('espadas', 7), ('ouros', 5)]
jogador = []
pc = []
'''
def comprar_cartas():
    carta = random.choice(baralho)
    
    if escolha == 1:
        jogador.append({'naipe': carta[0], 'valor': carta[1]})
    if escolha_pc == 1:
        pc.append({'naipe': carta[0], 'valor': carta[1]})
    
    baralho.remove(carta)
    
    return carta  # Retorna a carta escolhida
'''
# Exemplo de uso
escolha = 1
escolha_pc = 0


 # Agora 'carta' existe fora da função

def comprar_cartas():
        carta = random.choice(baralho)
        if escolha == 1:
            jogador.append({
                'naipe': carta[0],
                'valor': carta[1]
            })
        if escolha_pc == 1:
            pc.append({
                'naipe': carta[0],
                'valor': carta[1]
            })
        baralho.remove(carta)

print(comprar_cartas())