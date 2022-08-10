class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

        self.contador = 0

    def envelhecer(self, anos):
        for n in range(anos):
            if self.idade < 21:
                self.contador += 1
                self.idade += 1
                self.altura += (0.5 / 100)
        else:
            self.idade += (anos - self.contador)

    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        self.peso -= kilos

    def crecer(self, cm):
        self.altura += (cm / 100)


elionai = Pessoa('Elionai', 15, 72.5, 1.73)
elionai.envelhecer(10)
elionai.engordar(5)
elionai.emagrecer(2)
print(elionai.nome)
print(elionai.idade)
print(elionai.peso)
print(f'{elionai.altura:.3f}')
