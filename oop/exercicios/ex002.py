from decimal import Decimal

class ContaBancaria:
    def __init__(self,titular, saldo=0):
        self.titular = titular
        self.saldo = Decimal(saldo)

    def depositar(self,valor):
        try:
            self.saldo += Decimal(valor)
            print(f'{self.titular} fez um deposito no valor de {valor:.2f} reais.')
        except Exception:
            print('Valor inserido inválido')
       
    
    def sacar(self, valor):
        try:
            self.saldo -= Decimal(valor)
            print(f'{self.titular} fez um saque no valor de {valor:.2f} reais.')
        except Exception:
            print('Valor inserido inválido.')

    def mostrar_saldo(self):
        print(f'O seu saldo total é de {self.saldo:.2f}')



conta = ContaBancaria('Felipe', -100)

conta.depositar(250.10)
conta.mostrar_saldo()
