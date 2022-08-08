class TV:
    ligada = False
    canal = 1
    volume = 50

    def ligar(self):
        self.ligada = True
        self.monitor()

    def desligar(self):
        self.ligada = False
        self.monitor()

    def mudar_canal(self, canal):
        if self.ligada:
            if 1 <= canal <= 10:
                self.canal = canal
                self.monitor()

    def def_volume(self, niv_volume):
        if self.ligada:
            if 1 <= niv_volume <= 100:
                self.volume = niv_volume
                self.monitor()

    def monitor(self):
        if self.ligada:
            print(f'Canal: {self.canal}')
            print(f'Volume: {self.volume}')
        return None


toshiba = TV()
toshiba.ligar()
toshiba.def_volume(80)
toshiba.mudar_canal(5)
