class Quadrado:
    def __init__(self, tamanholado):
        self.tamanholado = tamanholado

    def mudar_valor_lado(self, valor):
        self.tamanholado = valor
        return self.tamanholado

    def retorna_valor_lado(self):
        print(f'O tamanho do lado é: {self.tamanholado}')

    def calcula_area(self):
        area = self.tamanholado * 2
        return area

quadrado = Quadrado(5)
quadrado.retorna_valor_lado()
quadrado.mudar_valor_lado(8)
quadrado.retorna_valor_lado()
print(quadrado.calcula_area())
