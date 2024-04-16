class Validador:
    def __init__(self, valor, atributo):
        self.__valor = valor
        self.__atributo = atributo
        self.__erros = []

    @property
    def valor(self):
        if self.__erros:
            raise ValueError(self.__erros)
        return self.__valor

    def nao_nulo(self):
        if not self.__valor:
            self.__erros.append(f'{self.__atributo}: não pode ser nulo')
        return self

    def nao_vazio(self):
        if not self.__valor:
            return self

        if not self.__valor.strip():
            self.__erros.append(f'{self.__atributo}: não pode ser vazio')
        return self

    def tamanho_minimo(self, minimo):
        if self.__valor is None:
            return self

        if len(self.__valor) < minimo:
            self.__erros.append(f'{self.__atributo}: deve possuir no mínimo {minimo} caracteres')
        return self

    def tamanho_maximo(self, maximo):
        if self.__valor is None:
            return self

        if len(self.__valor) > maximo:
            self.__erros.append(f'{self.__atributo}: deve possuir no máximo {maximo} caracteres')
        return self

    def quantidade_minima_palavras(self, quantidade):
        if self.__valor is None:
            return self

        if len(self.__valor.split()) < quantidade:
            self.__erros.append(f'{self.__atributo}: deve possuir pelo menos {quantidade} palavras')
        return self

    def email(self):
        if self.__valor is None:
            return self

        if '@' not in self.valor:
            self.__erros.append(f'{self.__atributo}: deve ser uma e-mail válido')
        return self


if __name__ == '__main__':
    resposta = Validador('teste', 'E-mail').nao_vazio().tamanho_minimo(4).valor
    print(resposta)
