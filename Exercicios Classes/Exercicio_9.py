class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostra_ponto(self):
        return self.x, self.y


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro_retangulo(self):
        return self.largura / 2, self.altura / 2


ponto_1 = Ponto(5, 8)
ponto_2 = Ponto(10, 18)

objeto_1 = Retangulo(ponto_1, ponto_2)
objeto_2 = Retangulo(10, 16)

print(objeto_1.altura.x)