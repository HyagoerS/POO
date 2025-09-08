class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            print("Saldo insuficiente.")


conta = ContaBancaria("POO", 100.00)

print(f"Saldo inicial da conta de {conta.titular}: R${conta.saldo:.2f}")


depositar_conta = float(input("Digite o valor que você deseja depositar: "))
sacar_conta = float(input("Digite o valor que você deseja sacar: "))


conta.depositar(depositar_conta)
conta.sacar(sacar_conta)

print(f"Saldo final da conta de {conta.titular}: R${conta.saldo:.2f}")