
# DONE Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# Altere o valor do atributo nome para 'Bistrô'.
# TODO Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# TODO  se a categoria da instância restaurante_pizza é 'Fast Food'.
# TODO Mude o estado da instância restaurante_pizza para ativo.
# TODO Imprima no console o nome e a categoria da instância restaurante_praca.

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

rest_pplace = Restaurante('Pizza Place', 'Italiana')
rest_mcd = Restaurante('McDonalds', 'Fast Food')

print(Restaurante.meus_rest())

