class Musica:
    playlist = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome.title()
        self.artista = artista.title()
        self.duracao = f'{duracao / 60:.2f}'
        Musica.playlist.append(self)

    def __str__(self):
        return f'{self.nome} - {self.artista} - {self.duracao}'

    def minha_playlist():
        for musicas in Musica.playlist:
            print(f'{musicas.nome} - {musicas.artista} - {musicas.duracao}', end=' ')



walk = Musica('Walk', 'Pantera', 316)
beat_it = Musica('Beat it', 'michael jackson', 632)

print(Musica.playlist)