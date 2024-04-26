class ItemCardapio:
    def __int__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
