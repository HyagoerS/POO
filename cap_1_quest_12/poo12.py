class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

        def depositar(self, valor):
            self.saldo += valor
            if saldo > 0:
                True

        def sacar(self, valor):
            self.saldo -= valor
            if saldo <= 0:
                False


conta_banco = 10

depositar_conta = float(input("Digite o valor que vacê deseja depositar: "))
sacar_conta = float(input("Digite o valor que você deseja sacar: "))

valor_banco = ContaBancaria(conta_banco)
valor_banco.depositar(depositar_conta)
valor_banco.sacar(sacar_conta)

print(f"Situação da sua conta {valor_banco}")


