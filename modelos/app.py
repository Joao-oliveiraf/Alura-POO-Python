from restaurante import Restaurante
from item_cardapio import Bebida, ItemCardapio

# rest_pplace = Restaurante('Pizza Place', 'Italiana')
# rest_mcd = Restaurante('McDonalds', 'Fast Food')
suco = Bebida('sucao', 12, 'large')


def main():
    print(Restaurante.meus_rest())
    print(suco)


if __name__ == '__main__':
    main()
