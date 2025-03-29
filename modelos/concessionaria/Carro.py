class Carro:
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def liga(self):
        print(f'O carro modelo {self.modelo} está ligado')