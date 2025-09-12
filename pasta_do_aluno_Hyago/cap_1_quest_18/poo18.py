class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplina_lecionada = [] 

    def lecionar_disciplina(self, disciplina):
        self.disciplina_lecionada.append(disciplina)
        print(f" A disciplina'{disciplina.nome}' foi adicionado.")

        
nova_disciplina = Professor("Jales")

disciplina1 = Disciplina("Historia")
disciplina2 = Disciplina("Arte")
disciplina3 = Disciplina("Desing")

nova_disciplina.lecionar_disciplina(disciplina1)
nova_disciplina.lecionar_disciplina(disciplina2)
nova_disciplina.lecionar_disciplina(disciplina3)