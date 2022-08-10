class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []


macaco_1 = Macaco('Carlos')
macaco_2 = Macaco('Felix')
macaco_1.comer('Maça')
macaco_1.comer('Banana')
macaco_1.comer(macaco_2.nome)
print(macaco_1.ver_bucho())
macaco_1.digerir()
print(macaco_1.ver_bucho())
