class Area:
    PI = 3.14

    @staticmethod
    def circulo(raio):
        return Area.PI * raio ** 2

    @staticmethod
    def triagulao(base, altura):
        return (base * altura) / 2

    @staticmethod
    def retangulo(base, altura):
        return base * altura

    @classmethod
    def alterar_pi(cls, novo_pi):
        cls.PI = novo_pi


print(Area.PI)
Area.alterar_pi(3.1415)
print(Area.circulo(2.5))
print(Area.triagulao(6, 10))
print(Area.retangulo(4, 5))
