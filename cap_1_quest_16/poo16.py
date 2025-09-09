class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

class CatalogoLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"'{livro.titulo}' foi adicionada ao catálogo.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"'{titulo}' está no catálogo. Autor: {livro.autor}")
                return
        print(f"'{titulo}' não está no catálogo.")

    def mostrar_catalogo(self):
        if not self.livros:
            print("O catálogo está vazio.")
        else:
            print("Catálogo de Livros:")
            for i, livro in enumerate(self.livros, 1):
                print(f"{i}. {livro.titulo} - {livro.autor} ({livro.ano_publicado})")



catalogo = CatalogoLivros()


livro1 = Livro("Drácula de Brastronk", "Autor Desconhecido", 1897)
livro2 = Livro(" O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro3 = Livro("Noites Brancas", "Fiódor Dostoiévski", 1848)


catalogo.adicionar_livro(livro1)
catalogo.adicionar_livro(livro2)
catalogo.adicionar_livro(livro3)


catalogo.mostrar_catalogo()


catalogo.buscar_livro("Crepúsculo")
catalogo.buscar_livro("Harry Potter") 