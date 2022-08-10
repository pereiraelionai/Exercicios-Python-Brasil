class Tv:
    def __init__(self, canal=2, volume=50):
        self.canal = canal
        self.volume = volume

    def altera_canal(self, canal):
        if 1 <= canal <= 20:
            self.canal = canal

    def aumenta_volume(self, volume=1):
        self.volume += volume
        if self.volume > 100:
            self.volume = 100
            return 'Volume máximo permitido 100'

    def diminui_volume(self, volume=1):
        self.volume -= volume
        if self.volume < 0:
            self.volume = 0
            return 'Volume mínimo permitido 0'


toshiba = Tv()
toshiba.aumenta_volume(100)
toshiba.altera_canal(180)
print(toshiba.canal, toshiba.volume)
