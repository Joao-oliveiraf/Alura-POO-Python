# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com
# base na profissão da pessoa.

class Pessoa:
    galera = []

    def __init__(self, nome, idade, profissao=None):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self._trabalhando = True if profissao else False
        Pessoa.galera.append(self)

    def __str__(self):
        return f'Nome: {self.nome} -- Idade: {self.idade} -- Profissão: {self.profession} - {self.working}'

    @property
    def profession(self):
        return 'Vagabundo' if self.profissao is None else self.profissao

    @property
    def working(self):
        return 'Trabalhando no momento!' if self._trabalhando else 'Desempregado :('

    @classmethod
    def minha_galera(cls):
        for gente in Pessoa.galera:
            print(f'Nome:{gente.nome.ljust(10)}  Idade:{str(gente.idade).ljust(10)} '
                  f'Profissão:{gente.profession.rjust(10)} Situação profissional:{gente.working.rjust(10)}')

    def saudacao(self):
        print(f'Saudações {self.nome}!, sua profissão de {self.profession} é muito legal!')

    def aniversário(self):
        self.idade += 1


jp = Pessoa('João Pedro', 28)
jp_20 = Pessoa(nome='John Oliveira', idade=30, profissao='Software Engineer')
jp.saudacao()
jp_20.aniversário()
Pessoa.minha_galera()

