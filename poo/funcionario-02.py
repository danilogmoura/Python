class FuncionarioV2:
    def __init__(self, salario):
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def movimentacao_salarial(self, percentual):
        if percentual <= 0:
            raise ValueError("Percentual inválido, deve ser maior que 0")
        self.__salario = self.__salario + (self.salario * percentual / 100)


funcionario = FuncionarioV2(1300)
print(funcionario.salario)
funcionario.movimentacao_salarial(10)
print(funcionario.salario)
