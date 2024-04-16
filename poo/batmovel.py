class Carro():
    def dirigir(self):
        return "Você está dirigindo"


class Barco():
    def navegar(self):
        return "Você está navegando"


class Aviao():
    def voando(self):
        return "Você está voando"


class CarroAnfibio(Carro, Barco):
    pass


class CarroVoador(Carro, Aviao):
    pass


class BatMovel(Carro, Barco, Aviao):
    pass


carro = CarroAnfibio()
print(carro.dirigir())
print(carro.navegar())

carro = CarroVoador()
print(carro.dirigir())
print(carro.voando())

carro = BatMovel()
print(carro.dirigir())
print(carro.voando())
print(carro.navegar())