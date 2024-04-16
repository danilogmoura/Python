from senha_fraca_exception import SenhaFracaException


class SenhaForte:
    def __init__(self, valor):
        self.__valor = valor

        validacoes = [
            self.__tamanho_minimo(8),
            self.__tem_letras_maisculas(),
            self.__tem_letras_minusculas(),
            self.__tem_numeros(),
            self.__tem_caracteres_especiais()
        ]

        if not all(validacoes):
            raise SenhaFracaException("Senha fraca")

    @property
    def valor(self):
        return self.__valor

    def __tamanho_minimo(self, tamanho):
        return len(self.__valor) >= tamanho

    def __tem_letras_maisculas(self):
        return any(letra.isupper() for letra in self.__valor)

    def __tem_letras_minusculas(self):
        return any(letra.islower() for letra in self.__valor)

    def __tem_numeros(self):
        return any(letra.isdigit() for letra in self.__valor)

    def __tem_caracteres_especiais(self):
        return any(not letra.isalnum() for letra in self.__valor)


try:
    senha = SenhaForte('#Senha123!')
    print(senha.valor)
except ValueError as e:
    print(f"Ocorreu um erro: {e}")
finally:
    print("Programa finalizou!")
