class ControleRemoto:
    def __init__(self, cor, comprimento, largura):
        self.cor = cor
        self.comprimento = comprimento
        self.largura = largura


obj_controle = ControleRemoto('branco', '10cm', '5cm')

print(obj_controle.cor)

