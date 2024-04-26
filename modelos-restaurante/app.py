from restaurante import *
from cardapio.item_cardapio import *
from cardapio.bebida import *
from cardapio.prato import *


rest_pplace = Restaurante('Pizza Place', 'Italiana')
rest_mcd = Restaurante('McDonalds', 'Fast Food')

def main():
    print(Restaurante.meus_rest())

if __name__ == '__main__':
    main()