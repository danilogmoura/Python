from pacotes.utils import Validador


class NomePessoa:
    def __init__(self, completo, atributo='Nome'):
        self.__completo = (Validador(completo, atributo)
                           .nao_nulo()
                           .tamanho_minimo(4)
                           .tamanho_maximo(120)
                           .quantidade_minima_palavras(2).valor)

    @property
    def completo(self):
        return self.__completo

    @property
    def primeiro_nome(self):
        return self.__completo.split()[0]

    @property
    def ultimo_sobrenome(self):
        return self.__completo.split()[-1]

    def __str__(self):
        return self.__completo
