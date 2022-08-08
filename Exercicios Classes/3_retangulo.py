class Retangulo:
    def __init__(self, base_ret, altura_ret):
        self.base_ret = base_ret
        self.altura_ret = altura_ret

    def mudar_altura(self, base, altura):
        self.base_ret = base
        self.altura_ret = altura
        return self.base_ret, self.altura_ret

    def tamanho_ret(self):
        print(f'Base: {self.base_ret}')
        print(f'Atura: {self.altura_ret}')

    def area_ret(self):
        area = self.base_ret * self.altura_ret
        return area

    def perimetro_ret(self):
        perimetro = (self.base_ret * 2) + (self.altura_ret * 2)
        return perimetro


construcao = Retangulo(20, 60)
construcao.mudar_altura(10, 30)
construcao.tamanho_ret()
print(construcao.area_ret())
print(construcao.perimetro_ret())
