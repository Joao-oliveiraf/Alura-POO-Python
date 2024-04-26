from restaurante import *
from cardapio.bebida import Bebida
from cardapio.prato import Prato


rest_pplace = Restaurante('Pizza Place', 'Italiana')
rest_mcd = Restaurante('McDonalds', 'Fast Food')

def main():
    print(Restaurante.meus_rest())

if __name__ == '__main__':
    main()