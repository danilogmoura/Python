class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("Bia", 34)
pessoa1.nome = "Pedro"
pessoa2 = Pessoa("Ana", 24)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
