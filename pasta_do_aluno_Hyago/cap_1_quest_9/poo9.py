class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

e_commerce = Produto("Camiseta", 54.80 , 24 )
e_commerce2 = Produto("Peso Walter", 85.99, 12)
e_commerce3 = Produto("Perfume Cebolinha Turma da Mônica 25ml", 45.75, 3)

print(e_commerce.nome, ",", e_commerce.preco,",", e_commerce.estoque)
print(e_commerce2.nome,",", e_commerce2.preco,",", e_commerce2.estoque)
print(e_commerce3.nome,",", e_commerce3.preco,",",e_commerce3.estoque)