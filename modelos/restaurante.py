from avaliacao import Avaliacao
from item_cardapio import *


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
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

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliador = Avaliacao(cliente, nota)
            self.avaliacao.append(avaliador._nota)

    def media_de_avaliacoes(self):
        if not self.avaliacao:
            return 'Sem avaliações!'
        else:
            return f"{sum(self.avaliacao) / len(self.avaliacao):.1f}"

    def add_prato_cardapio(self, nome, preco, descricao):
        novo_prato = Prato(nome, preco, descricao)
        self.cardapio.append(novo_prato)

    def add_bebida_cardapio(self, nome, preco, tamanho):
        novo_bebida = Bebida(nome, preco, tamanho)
        self.cardapio.append(novo_bebida)

    @classmethod
    def meus_rest(cls):
        for i in cls.restaurantes:
            print(f'{i.nome} - {i.categoria} - {i.status()} - {i.media_de_avaliacoes()}')

    def menu_do_restaurante(self):
        print(f'Menu do restaurante: {self.nome}')
        for pratos in self.cardapio:
            if pratos.__class__ == Prato:
                print(pratos.nome.title(), pratos.preco, pratos.descricao.title())
            else:
                print(pratos.nome.title(), pratos.preco, pratos.tamanho.title())
