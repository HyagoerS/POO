class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0


velocidade_inicial = 0
aceleracao = int(input("Qual a velocidade que você deseja alcançar? "))
freagem = int(input("Qual foi o valor da sua freiada? "))

carro_partida = Carro(velocidade_inicial)
carro_partida.acelerar(aceleracao)
carro_partida.frear(freagem)

print(f"A velocidade após a freagem é: {carro_partida.velocidade}")