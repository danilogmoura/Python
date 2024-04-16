from abc import ABC, abstractmethod


class Atendente(ABC):
    @abstractmethod
    def saudacao(self):
        pass


class AtendentePortugues(Atendente):

    def saudacao(self):
        return "Bom dia"


class AtendenteIngles(Atendente):

    def saudacao(self):
        return "Good morning"


class AtendenteJapones(Atendente):

    def saudacao(self):
        return "おはよう"


atendente1 = AtendentePortugues()
print(atendente1.saudacao())

atendente1 = AtendenteIngles()
print(atendente1.saudacao())

atendente1 = AtendenteJapones()
print(atendente1.saudacao())
