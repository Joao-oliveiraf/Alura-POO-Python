class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
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

    def meus_rest():
        for i in Restaurante.restaurantes:
            print(f'{i.nome}, {i.categoria}, {i.status()}')


