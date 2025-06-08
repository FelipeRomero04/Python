class ControleRemoto:
    def __init__(self, cor, comprimento, largura):
        self.cor = cor
        self.comprimento = comprimento
        self.largura = largura


obj_controle = ControleRemoto('branco', '10cm', '5cm')

print(obj_controle.cor)


'''
Por convenção as classes são criadas com letras maiúsculas

criar uma instância - atribuir a classe a uma variavel


O param Self de todas as funções dentro da class(obrigatorio) serve para referenciar o objeto/class, para assim, atribuir uma caracteristica/atributo desse objeto  

Tudo dentro da classe, que for usado self. para criar uma caracteristica, poderá ser acessada quando for usar essa class, como explicado abaixo 


Quando um atributo / característica e criado dentro de init, para se referir a esse atributo da instância, deve seguir a seguinte estrutura:

instancia.atributo    - sem parênteses!!!

Seguindo o trecho de código acima, seria:

obj_controle.cor   -   Como não é uma função, e sim uma caracteristica do objeto, os parentes não são necessários

funções dentro de classes são consideradas métodos.

Quando necessario usar um métedo (função interna da class(sem ser o init)), para chama-la deve usar a seginte estrutura:

instancia.função(param)

seguindo o trecho de código acima, seria:

obj_controle.vendeu(1000)



o '.vendeu()' é a forma de se referenciar a uma função interna dentro da class


Todos atributos de uma Class, deve ser declarada dentro do init(recomendado apenas, não obrigatório).


Por que Classes são uteis:

As classes são muito utilizadas em sistemas web. Isso por que um de seus beneficios e poder regrar o que cada cliente pode fazer criando classes que permitem isso. Em sistemas com tráfego, é impossivel programar cada ação de um cliente individualmente, não so dos cliente, mas as de um administrador, o que cada produto tem que conter...

'''