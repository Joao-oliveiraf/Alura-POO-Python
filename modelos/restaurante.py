from avaliacao import Avaliacao
from item_cardapio import *


class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = []
        self.cardapio = []
        if categoria.lower() == 'fast food':
            self.ativo = True
        else:
            self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.status()}'

    def status(self):
        if self.ativo:
            return 'Restaurante Ativo!'
        else:
            return 'Restaurante Inativo!'

    def receber_avaliacao(self, cliente: str, nota: int):
        if 0 < nota < 5:
            avaliador = Avaliacao(cliente, nota)
            self.avaliacao.append(avaliador._nota)

    def media_de_avaliacoes(self):
        if not self.avaliacao:
            return 'Sem avaliações!'
        else:
            return f"{sum(self.avaliacao) / len(self.avaliacao):.1f}"

    def add_item_cardapio(self, item: object):
        self.cardapio.append(item)

    @classmethod
    def meus_rest(cls):
        for i in cls.restaurantes:
            print(f'{i.nome} - {i.categoria} - {i.status()} - {i.media_de_avaliacoes()}')

    def menu_do_restaurante(self):
        print(f'Menu do restaurante: {self.nome}')
        for pratos in self.cardapio:
            if pratos.__class__ == Prato:
                msg = f"{pratos.nome.title()} - R${pratos.preco:.2f} - {pratos.descricao.title()}"
                print(msg.replace(".", ","))
            elif pratos.__class__ == Bebida:
                msg = f"{pratos.nome.title()} - R${pratos.preco:.2f} - {pratos.tamanho.title()}"
                print(msg.replace(".", ","))
            else:
                msg = f"{pratos.nome.title()} - R${pratos.preco:.2f} - {pratos.tipo.title()} - {pratos.tamanho.title()}"
                print(msg.replace(".", ","))
