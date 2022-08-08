class Tamagushi:
    def __init__(self, nome, idade):
        self.nome = nome
        self.fome = False
        self.saude = True
        self.idade = idade
        self.humor = 'Feliz'

    def alt_nome(self, nome):
        self.nome = nome

    def alt_idade(self, idade):
        self.idade = idade

    def alt_fome(self):
        if self.fome:
            self.fome = False
            return
        self.fome = True

    def alt_saude(self):
        if self.saude:
            self.saude = False
            return
        self.saude = True

    def def_humor(self):
        if not self.fome and self.saude:
            self.humor = 'Feliz'
            return
        self.humor = 'Triste'

    def monitor(self):
        self.def_humor()
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print('Saudável' if self.saude else 'Doente')
        print('Com fome' if self.fome else 'Sem fome')
        print(f'Humor: {self.humor}')


blue = Tamagushi('Blue', 2)
blue.monitor()
blue.alt_fome()
blue.monitor()
blue.alt_fome()
blue.alt_nome('Azul')
blue.alt_idade(12)
blue.monitor()
