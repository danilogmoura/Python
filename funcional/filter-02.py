class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f'Cliente(Nome: {self.nome}, Email: {self.email})'


lista_clientes = [
    Cliente("João", "joao@email.com.br"),
    Cliente("Maria", "maria@gmail.com"),
    Cliente("Pedro", "pedro@email.com.br"),
    Cliente("Ana", "ana@email.com.br"),
]

resultado = filter(lambda cliente: "email.com.br" in cliente.email, lista_clientes)
clientes_filtrados = list(resultado)

for cliente in clientes_filtrados:
    print(cliente)
