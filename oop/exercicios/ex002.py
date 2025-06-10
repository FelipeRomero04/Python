class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depostitar(self,valor):
        try:
            self.saldo += valor
            print(f'{self.titular} fez um deposito no valor de {valor} reais.')
        except Exception:
            print('Valor inserido inválido')
       
    
    def sacar(self, valor):
        try:
            self.saldo -= valor
            print(f'{self.titular} fez um saque no valor de {valor} reais.')
        except Exception:
            print('Valor inserido inválido.')

    def mostrar_saldo(self):
        print(f'O seu saldo é de {self.saldo}')



conta = ContaBancaria('Felipe', 1000)
