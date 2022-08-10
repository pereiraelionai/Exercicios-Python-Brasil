class Tamagushi:
    def __init__(self, nome, idade, fome=False, saude=True):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def altera_nome(self, nome):
        self.nome = nome

    def altera_idade(self, idade):
        self.idade = idade

    def altera_fome(self):
        if self.fome:
            self.fome = False
            return f'{self.nome} sem fome'
        else:
            self.fome = True
            return f'{self.nome} com fome'

    def altera_saude(self):
        if self.saude:
            self.saude = False
            return f'{self.nome} doente'
        else:
            self.saude = True
            return f'{self.nome} saudável'

    def mostra_nome(self):
        return self.nome

    def mostra_idade(self):
        return self.idade

    def mostra_saude(self):
        if self.saude:
            return 'Saudável'
        else:
            return 'Doente'

    def mostra_fome(self):
        if self.fome:
            return 'Com fome'
        else:
            return 'Sem fome'

    def mostra_humor(self):
        if self.saude and not self.fome:
            return 'Feliz'
        else:
            return 'Triste'


leao = Tamagushi('Lion', 12)
print(leao.mostra_humor())
print(leao.altera_fome())
print(leao.mostra_humor())
