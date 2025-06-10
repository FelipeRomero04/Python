class Retangulo:
    
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura
    
    def area(self):
        area_retang = self.largura * self.altura
        return f'A área do retangulo é {area_retang}cm²'
    
    def perimetro(self):
        perim_retang = 2 * (self.largura + self.altura)
        return f'O perímetro do retangulo é {perim_retang}cm²'


retangulo = Retangulo(400, 250)

print(retangulo.area())
print(retangulo.perimetro())