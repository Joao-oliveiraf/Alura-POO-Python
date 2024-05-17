from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    @abstractmethod
    def aplicar_desconto(self, desconto):
        pass


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def aplicar_desconto(self, desconto):
        if desconto > 0:
            self.preco = self.preco - (self.preco * (desconto / 100))


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao, desconto=0):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.desconto = desconto

    def aplicar_desconto(self, desconto):
        if desconto > 0:
            self.preco = self.preco - (self.preco * (desconto / 100))


class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho

    def aplicar_desconto(self, desconto):
        if desconto > 0:
            self.preco = self.preco - (self.preco * (desconto / 100))
