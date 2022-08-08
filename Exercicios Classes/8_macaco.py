class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = None

    def comer(self, comida):
        self.bucho = comida
        print(f'{self.nome} está comendo {self.bucho}')

    def digerir(self):
        self.bucho = None

    def ver_bucho(self):
        print(self.bucho)


m_1 = Macaco('Stuart')
m_2 = Macaco('Zé')

m_1.comer('Banana')
m_1.digerir()
m_1.ver_bucho()

m_2.comer(m_1.nome)
