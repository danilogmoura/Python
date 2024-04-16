class FuncionarioV1:
    def __init__(self, salario):
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 1300:
            raise ValueError("O salário não pode ser menor que o salário mínimo")
        self.__salario = novo_salario


funcionario = FuncionarioV1(1000)
print(funcionario.get_salario())
funcionario.salario = 1301
print(funcionario.salario)
