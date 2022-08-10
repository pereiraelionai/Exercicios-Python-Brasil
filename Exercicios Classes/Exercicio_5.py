class ContaCorrente:
    def __init__(self, nome, num_conta, saldo=0):
        self.nome = nome
        self.num_conta = num_conta
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor
        return 'Deposito realizado com sucesso!'

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return 'Saque realizado com sucesso!'
        else:
            return 'Saldo insuficiente'


maria = ContaCorrente('Maria', 584100, 150)
maria.alterar_nome('Maria de Castro')
print(maria.sacar(5000))
print(maria.deposito(6500))
print(maria.sacar(1800))
print(maria.nome)
print(maria.saldo)
