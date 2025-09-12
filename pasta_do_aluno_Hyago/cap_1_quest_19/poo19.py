class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        if quantidade > produto.estoque:
            print(f"Não há estoque suficiente para adicionar {quantidade} unidades de {produto.nome}.")
        else:
            self.itens.append({'produto': produto, 'quantidade': quantidade})
            print(f"{quantidade} unidade(s) de '{produto.nome}' foi(ram) adicionada(s) ao carrinho.")
            produto.estoque -= quantidade
            print(f"Estoque atual de {produto.nome}: {produto.estoque}")

    def finalizar_compra(self):
        total = sum(item['produto'].preco * item['quantidade'] for item in self.itens)
        return total

produto1 = Produto("Garrafa térmica", 54.65, 20)
produto2 = Produto("Celular", 1334.69, 19)
produto3 = Produto("Mouse Gamer", 54.00, 8)


carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(produto1, 2)
carrinho.adicionar_produto(produto2, 1)
carrinho.adicionar_produto(produto3, 5)
carrinho.adicionar_produto(produto1, 25)


print(f"Total do pedido: R$ {carrinho.finalizar_compra():.2f}")