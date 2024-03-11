# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
# Inicie o atributo ativo como False por padrão.
#
# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada
# com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
#
# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
#
# Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos.
# Utilize propriedades, se necessário.
#
# Crie uma instância da classe e imprima o valor da propriedade titular.
#
# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#
# Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Nome: {self._titular} ---- Saldo: R${float(self._saldo):,.2f} {self.ativado_desativado}'

    def ativar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativado_desativado(self):
        return f'Conta ativa' if self._ativo else 'Conta desativada'

pessoa1 = ContaBancaria('John', saldo=0)
pessoa2 = ContaBancaria('Riquinho Rico', saldo=156498456151)
pessoa2.ativar_conta()
print(pessoa2)
