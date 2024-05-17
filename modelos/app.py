from restaurante import Restaurante
from item_cardapio import *

rest_pplace = Restaurante('Pizza Place', 'Italiana')
rest_mcd = Restaurante('McDonalds', 'Fast Food')

rest_mcd.receber_avaliacao('joao', 4)
rest_mcd.receber_avaliacao('joo', 2)
rest_mcd.receber_avaliacao('jo', 3)

sucao = Bebida('sucao', 12, 'grandao')
pratinho = Prato('Massa', 35, 'Massa carbonara')
bolo = Sobremesa('bolo de chocolate', 15, 'com cobertura', 'médio')


def main():
    Restaurante.meus_rest()
    sucao.aplicar_desconto(10)
    rest_mcd.add_item_cardapio(sucao)
    bolo.aplicar_desconto(2)
    rest_mcd.add_item_cardapio(bolo)
    rest_mcd.menu_do_restaurante()
    rest_pplace.ativo = True
    Restaurante.meus_rest()


if __name__ == '__main__':
    main()
