class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

Saber_paginas = Livro("Carmilla a vampira de karnstein","Joseph Sheridan Le Fanu",1872 )
print(Saber_paginas.titulo, ",",Saber_paginas.autor,"," ,Saber_paginas.ano_publicado)