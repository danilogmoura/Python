class Calculadora():
    def __init__(self, valor=0):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def somar(self, valor):
        self.__valor += valor
        return self

    def subtrair(self, valor):
        self.__valor -= valor
        return self

    def multiplicar(self, valor):
        self.__valor *= valor
        return self

    def dividir(self, valor):
        self.__valor /= valor
        return self

    def __add__(self, other):
        return Calculadora(self.__valor).somar(other.valor)

    def __str__(self):
        return f"A calculadora tem valor em memória de {self.__valor}"

    def __eq__(self, other):
        return self.__valor == other.valor


calculadora1 = Calculadora()

calculadora1.somar(100)
calculadora1.subtrair(20)
calculadora1.dividir(4)
calculadora1.multiplicar(10)

print(calculadora1.valor)

calculadora2 = Calculadora(1000).multiplicar(3.1415)
print(calculadora2.valor)

calculadora3 = calculadora1 + calculadora2
print(calculadora3)

print(calculadora1 == calculadora3)
