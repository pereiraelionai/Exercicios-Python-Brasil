class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def altera_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def retorna_tamanho(self):
        return self.base, self.altura

    def calcula_area(self):
        return self.base * self.altura

    def calcula_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro


# Criando programa
lado_a = int(input('Digite o tamanho do primeiro lado: '))
lado_b = int(input('Digite o tamanho do segundo lado: '))

retangulo = Retangulo(lado_a, lado_b)

print(f'Pisos necessários(1x1): {retangulo.calcula_area()}')
print(f'Rodapés necessários(1 metro): {retangulo.calcula_perimetro()}')
