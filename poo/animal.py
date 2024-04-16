class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def expressar(self):
        return f"O {self.__nome} está fazendo um som"


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def expressar(self):
        return f"{super().expressar()}... Au Au Au Au"


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


animal1 = Animal("Animal")
print(animal1.expressar())

animal1 = Cachorro("Rex")
print(animal1.expressar())

animal1 = Gato("Mel")
print(animal1.expressar())
