class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque


    def atacar_oponente(self, alvo):
        dano_causado = self.ataque
        print(f"{self.nome} ataca {alvo.nome} causando {dano_causado} de dano!")
        alvo.receber_dano(dano_causado)

    def receber_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.hp}.")
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.hp}.")


heroi = Personagem("Herói", 100, 20)
vilao = Personagem("Vilão", 80, 15)

print(f"Batalha entre {heroi.nome} e {vilao.nome}!")


heroi.atacar_oponente(vilao)

vilao.atacar_oponente(heroi)

heroi.atacar_oponente(vilao)

print("Fim da batalha.")