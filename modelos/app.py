from restaurante import Restaurante
from item_cardapio import *

rest_pplace = Restaurante('Pizza Place', 'Italiana')
rest_mcd = Restaurante('McDonalds', 'Fast Food')


rest_mcd.receber_avaliacao('joao', 4)
rest_mcd.receber_avaliacao('joo', 2)
rest_mcd.receber_avaliacao('jo', 3)
rest_mcd.add_prato_cardapio('massa', 19, 'massa carbonara')
rest_mcd.add_bebida_cardapio('sucao', 12, 'grande')


def main():
    Restaurante.meus_rest()
    rest_mcd.menu_do_restaurante()


if __name__ == '__main__':
    main()

