import random

class RoloDeDados:

    def rolar_d6():
        return random.randint(1, 6)
    
    def rolar_d12():
        return random.randint(1, 12)
    
    def rolar_d20():
        return random.randint(1, 20)


rolar_dados1 = RoloDeDados.rolar_d6()
rolar_dados2 = RoloDeDados.rolar_d12()
rolar_dados3 = RoloDeDados.rolar_d20()

print(rolar_dados1)
print(rolar_dados2)
print(rolar_dados3)