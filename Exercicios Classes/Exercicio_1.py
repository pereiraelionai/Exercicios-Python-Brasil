class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor
        return self.cor

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')


bola = Bola('Amarela', 0.6, 'couro')
bola.mostra_cor()
bola.troca_cor('Azul')
bola.mostra_cor()
