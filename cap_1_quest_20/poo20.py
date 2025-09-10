class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

    
    def esta_vivo(self):
        if self.hp > 0:
            print("A batalha continua! ")
            return True


class Arena:
    def __init__(self):
        pass
    
    def iniciar_batalha(self, personagem1, personagem2):
        return


heroi = Personagem("Herói", 100, 20)
vilao = Personagem("Vilão", 80, 15)

print(f"Batalha entre {heroi.nome} e {vilao.nome}!")


heroi.atacar_oponente(vilao)

vilao.atacar_oponente(heroi)

heroi.atacar_oponente(vilao)

print("Fim da batalha.")