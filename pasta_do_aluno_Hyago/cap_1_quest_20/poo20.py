class Personagem:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

    def esta_vivo(self):
        return self.hp > 0

    def atacar(self, inimigo):
        inimigo.hp -= self.ataque
        if inimigo.hp < 0:  
            inimigo.hp = 0
        print(f"{self.nome} ataca {inimigo.nome}! Vida de {inimigo.nome} agora é {inimigo.hp}.")


class Arena:
    def __init__(self):
        pass
    
    def iniciar_batalha(self, personagem1, personagem2):
        rodada = 1
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            print(f"Rodada {rodada} ")
            
            personagem1.atacar(personagem2)
            if not personagem2.esta_vivo():
                print(f"{personagem2.nome} foi derrotado! {personagem1.nome} é o vencedor!")
                break

            personagem2.atacar(personagem1)
            if not personagem1.esta_vivo():
                print(f"{personagem1.nome} foi derrotado! {personagem2.nome} é o vencedor!")
                break
            
            rodada += 1



heroi = Personagem("Herói", 100, 20)
vilao = Personagem("Vilão", 80, 15)


print(f"Batalha entre {heroi.nome} e {vilao.nome}!")
arena = Arena()
arena.iniciar_batalha(heroi, vilao)

print("Fim da batalha.")
