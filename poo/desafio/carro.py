class Carro:
    def __init__(self, marca, nome):
        self.marca = marca
        self.nome = nome


carro = Carro("Fiat", "Uno")
print(carro.marca, carro.nome)
