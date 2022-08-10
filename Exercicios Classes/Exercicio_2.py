class Quadrado:
    def __init__(self, tam_lado):
        self.tam_lado = tam_lado

    def mudar_lado(self, tam):
        self.tam_lado = tam

    def valor_lado(self):
        return self.tam_lado

    def calc_area(self):
        area = self.tam_lado * 2
        return area
