class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade < 21:
            self.idade += anos
            crescer = anos * 0.05
            self.altura += crescer
            return
        self.idade += anos

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


carlos = Pessoa('Carlos', 15, 68, 1.62)
carlos.envelhecer(5)
carlos.engordar(2)
carlos.emagrecer(0.5)
carlos.crescer(1)
print(carlos.idade)
print(carlos.altura)
print(carlos.peso)
