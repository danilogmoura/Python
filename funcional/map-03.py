class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


lista_clientes = [
    Cliente("João", "joao@email.com.br"),
    Cliente("Maria", "maria@email.com.br"),
    Cliente("Pedro", "pedro@email.com.br"),
    Cliente("Ana", "ana@email.com.br"),
]

resultado_clientes = map(lambda cliente: cliente.email, lista_clientes)
print(list(resultado_clientes))
