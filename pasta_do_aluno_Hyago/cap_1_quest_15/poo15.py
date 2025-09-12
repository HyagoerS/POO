class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"'{musica}' foi adicionada à playlist '{self.nome}'.")

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"'{musica}' foi removida da playlist '{self.nome}'.")
        else:
            print(f"'{musica}' não está na playlist '{self.nome}'.")

    def listar_musicas(self):

        print(f" Músicas da Playlist '{self.nome}'")
        if not self.musicas:
            print("A playlist está vazia.")
        else:
            for i, musica in enumerate(self.musicas):
                print(f"{i}. {musica}")



minha_playlist = Playlist("Internacional")

minha_playlist.adicionar_musica("Diet moiunt dew")
minha_playlist.adicionar_musica("We burn")
minha_playlist.adicionar_musica("Sweather weather")


minha_playlist.listar_musicas()

minha_playlist.remover_musica("Sweather weather")

minha_playlist.listar_musicas()