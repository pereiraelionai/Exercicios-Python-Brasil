class ContaCorrente:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alt_nome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo = valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor


conta = ContaCorrente(34560, 'Elionai')
conta.saque(500)
print(conta.conta)
print(conta.nome)
print(conta.saldo)
conta.alt_nome('Ligia')
conta.deposito(10000)
conta.saque(800)
print(conta.conta)
print(conta.nome)
print(conta.saldo)
