# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
#  2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
#  3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
#  4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
#  5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Carro:  # 1
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo.title()
        self.cor = cor.title()
        self.ano = int(ano)


class Restaurante:  # 2
    meus_restaurantes = []

    def __init__(self, nome, categoria, cep):  # 3
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._delivery = False

        # Tratar CEP somente numeros
        def tratar(cep_tratar):
            endereco = [i for i in cep_tratar]
            for i in endereco:
                if len(endereco) != 8 or not i.isnumeric():
                    return 'CEP Invalido!'
                else:
                    endereco.insert(5, '-')
                    return ''.join(endereco)

        self.cep = tratar(cep)  # 91740-820
        Restaurante.meus_restaurantes.append(self)

    def __str__(self):  # 3
        return f'{self.nome} - {self.categoria} - {self.cep}'

    @classmethod
    def listar_restaurantes(cls):
        for rest in cls.meus_restaurantes:
            print(f'{rest.nome} - {rest.cep} - {rest.ativo}')

    @property
    def ativo(self):
        return f'Funcionando' if self._ativo else 'Desativado!'

    @property
    def delivery(self):
        return f'Funcionando' if self._delivery else 'Desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo


class Cliente:
    def __init__(self, nome, idade, sexo, salario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario

    def __str__(self):
        return f'Cliente: {self.nome}, {self.idade} anos, sexo: {self.sexo}, remuneração: R${self.salario}'


pizza = Restaurante('pizza', 'Italiana', '91740820')
pizza.alternar_estado()
cliente1 = Cliente('João Pedro', 21, 'Masculino', '0,00')
Restaurante.listar_restaurantes()
