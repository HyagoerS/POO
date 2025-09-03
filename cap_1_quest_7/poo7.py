class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

login = Usuario("POO", "POO@email.com")
print(login.nome, ",", login.email)
        