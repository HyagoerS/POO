class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class CarrinhoDeCompras:
    def __init__(self, itens):
        self.itens = itens

    def adicionar_produto(self, produto, quantidade):
        self.produto.append(produto)
        print(f"{produto.nome}' foi adicionado a produtos.")

        if quantidade > quantidade_pedido:
            print("Erro quantidade indesejada")
            return
        else:
            print("Erro quantidade indesejada")

    def finalizar_compra(self):
        total = sum(item.preco for item in self.itens)
        return total
    
quantidade_pedido = int(input("Quantidade que deseja comprar do produto: "))

pedido = CarrinhoDeCompras("Pedidos")

produto1 = Produto("Garrafa térmica", 54.65, 23)
produto2 = Produto("Celular", 1334.69, 19)
produto3 = Produto("Mouse Gamer", 54.00, 48)

pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)
pedido.adicionar_produto(produto3)



print(f"Total do pedido: R$ {pedido.calcular_total():.2f}")