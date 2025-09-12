class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)
        print(f"'{produto.nome}' foi adicionado a produtos.")

    def buscar_produto(self, nome):
        for produto in self.itens:
            if produto.nome == nome:
                print(f"'{nome}' está no estoque.")
                return
        print(f"'{nome}' não está no estoque.")

    def mostrar_estoque(self):
        if not self.itens:
            print("O estoque está vazio.")
        else:
            print("Estoque de produtos:")
            for i, item in enumerate(self.itens, 1):
                print(f"{i}., {pedido.cliente} fez pedidos desses produtos - {item.nome} - R$ {item.preco:.2f} ({item.estoque} unidades)")

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total



pedido = Pedido("POO")

produto1 = Produto("Garrafa térmica", 54.65, 23)
produto2 = Produto("Celular", 1334.69, 19)
produto3 = Produto("Mouse Gamer", 54.00, 48)



pedido.adicionar_item(produto1)
pedido.adicionar_item(produto2)
pedido.adicionar_item(produto3)


pedido.mostrar_estoque()


pedido.buscar_produto("Sabre de luz")
pedido.buscar_produto("Garrafa térmica")


print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")
