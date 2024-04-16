class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

    def buzinar(self, quantidade=1):
        for i in range(quantidade):
            print(f"{self.marca} {self.modelo} => Beeeeeeeeeeeep")


carro1 = Carro("Fiat", "Uno")
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.buzinar()
print(carro1.marca, carro1.modelo, carro1.velocidade)

carro2 = Carro("Ford", "Fusion")
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.buzinar(4)
print(carro2.marca, carro2.modelo, carro2.velocidade)
carro2.frear()
carro2.frear()
print(carro2.marca, carro2.modelo, carro2.velocidade)
