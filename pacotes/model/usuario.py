from .email import Email
from .nome_pessoa import NomePessoa


class Usuario:
    def __init__(self, nome, email, atributo='Nome Usuário'):
        self.nome = NomePessoa(nome, atributo)
        self.email = Email(email, 'E-mail usuário')

    def __str__(self):
        return f'Usuario: {self.nome}, Email: {self.email}'
